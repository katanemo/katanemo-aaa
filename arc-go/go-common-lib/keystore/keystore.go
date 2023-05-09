package keystore

import (
	"encoding/base64"
	"fmt"
)

type KeyStore interface {
	CreatePrivateKey(accountEmail string) (*string, error)
	GetPublicKey(keyId string) ([]byte, error)
	Sign(keyId, message string) ([]byte, error)
}

func ConvertDerToPem(derKey []byte) string {
	encodedPublicKey := base64.StdEncoding.EncodeToString(derKey)
	pemFormat := fmt.Sprintf("-----BEGIN PUBLIC KEY-----\n%v\n-----END PUBLIC KEY-----", encodedPublicKey)
	return pemFormat
}
