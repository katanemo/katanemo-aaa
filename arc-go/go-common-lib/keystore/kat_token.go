package keystore

import (
	"encoding/base64"
	"fmt"
	"time"

	"github.com/golang-jwt/jwt/v5"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib"
)

const DefaultTokenExpiry = time.Hour * 12

type KatToken interface {
	GetKeyId() string
	Validate(token string) (jwt.MapClaims, error)
	ValidateWithKey(token string, publicKeyDer []byte) (jwt.MapClaims, error)
	ValidateWithRsaKey(token string, publicKeyPem string) (jwt.MapClaims, error)
	GenerateToken(sub, iss, aud, accountId, keyId string, scp []string, tags map[string][]string, defaultServiceId string) (string, error)
}

func KatTokenFromKeyId(keyId string, keyStore KeyStore) KatToken {
	return &katToken{
		keyId:    keyId,
		keyStore: keyStore,
	}
}

type katToken struct {
	keyId    string
	keyStore KeyStore
}

// ValidateWithRsaKey implements KatToken
func (*katToken) ValidateWithRsaKey(token string, publicKeyPem string) (jwt.MapClaims, error) {
	key, err := jwt.ParseRSAPublicKeyFromPEM([]byte(publicKeyPem))
	if err != nil {
		return nil, fmt.Errorf("validate: parse key: %w", err)
	}
	tok, err := jwt.Parse(token, func(jwtToken *jwt.Token) (interface{}, error) {
		if _, ok := jwtToken.Method.(*jwt.SigningMethodRSA); !ok {
			return nil, fmt.Errorf("unexpected method: %s", jwtToken.Header["alg"])
		}

		return key, nil
	})
	if err != nil {
		return nil, fmt.Errorf("validate: %w", err)
	}

	claims, ok := tok.Claims.(jwt.MapClaims)
	if !ok || !tok.Valid {
		return nil, fmt.Errorf("validate: invalid")
	}

	return claims, nil
}

// GetKeyId implements KatToken
func (k *katToken) GetKeyId() string {
	return k.keyId
}

func (k *katToken) GenerateToken(sub, iss, aud, accountId, keyId string, scp []string, tags map[string][]string, defaultServiceId string) (string, error) {
	now := time.Now().UTC()
	exp := now.Add(DefaultTokenExpiry)

	claims := make(jwt.MapClaims)
	claims["sub"] = sub
	claims["iss"] = iss
	claims["aud"] = aud
	claims["scp"] = scp
	claims[common.TokenClaimAccountId] = accountId
	claims["exp"] = exp.Unix()
	claims["iat"] = now.Unix()
	claims["nbf"] = now.Unix()

	// For subscribers, add default service id to the token so authorizer can use it for paths etc.
	if defaultServiceId != aud {
		claims[common.KatanemoDefaultServiceId] = defaultServiceId
	}
	for k, v := range tags {
		claims[k] = v
	}

	token := jwt.NewWithClaims(jwt.SigningMethodRS256, claims)
	token.Header["kid"] = keyId

	signingString, err := token.SigningString()
	if err != nil {
		return "", nil
	}
	signature, err := k.keyStore.Sign(k.keyId, signingString)
	if err != nil {
		return "", fmt.Errorf("create: sign token: %w", err)
	}
	encodedSig := base64.RawURLEncoding.EncodeToString(signature)
	signedToken := fmt.Sprintf("%v.%v", signingString, encodedSig)
	return signedToken, nil
}

func (k *katToken) Validate(token string) (jwt.MapClaims, error) {
	publicKeyDer, err := k.keyStore.GetPublicKey(k.keyId)
	if err != nil {
		return nil, err
	}

	return k.ValidateWithKey(token, publicKeyDer)
}

func (k *katToken) ValidateWithKey(token string, publicKeyDer []byte) (jwt.MapClaims, error) {

	publicKeyPem := ConvertDerToPem(publicKeyDer)

	return k.ValidateWithRsaKey(token, publicKeyPem)

}

func ParseTokenUnsafe(token string) (jwt.MapClaims, error) {

	parsed, _, err := new(jwt.Parser).ParseUnverified(token, jwt.MapClaims{})
	if err != nil {
		return nil, err
	}
	claims, ok := parsed.Claims.(jwt.MapClaims)

	if !ok {
		return nil, fmt.Errorf("validate: invalid")
	}

	return claims, nil
}
