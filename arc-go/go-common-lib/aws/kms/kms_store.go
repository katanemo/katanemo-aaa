package kms

import (
	"context"

	awsconfig "github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/kms"
	"github.com/aws/aws-sdk-go-v2/service/kms/types"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/config"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/keystore"
	katlogger "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/logger"
)

const SigningAlgorithm = types.SigningAlgorithmSpecRsassaPkcs1V15Sha256

var AlgToJwtMap = map[types.SigningAlgorithmSpec]string{
	types.SigningAlgorithmSpecRsassaPkcs1V15Sha256: "RS256",
}

type KmsKeyStore struct {
	client   *kms.Client
	settings *config.Settings
}

func (k *KmsKeyStore) GetPublicKey(keyId string) ([]byte, error) {
	publicKeyResp, err := k.client.GetPublicKey(context.Background(), &kms.GetPublicKeyInput{
		KeyId: &keyId,
	})
	if err != nil {
		return nil, err
	}
	return publicKeyResp.PublicKey, nil
}

func NewKmsKeyStore(settings *config.Settings) keystore.KeyStore {
	return &KmsKeyStore{
		client:   createKmsClient(settings),
		settings: settings,
	}
}

func (k *KmsKeyStore) CreatePrivateKey(email string) (*string, error) {
	input := &kms.CreateKeyInput{
		KeySpec:  types.KeySpecRsa4096,
		KeyUsage: types.KeyUsageTypeSignVerify,
		Tags: []types.Tag{
			{
				TagKey:   aws.String("Environment"),
				TagValue: aws.String(string(k.settings.Environment)),
			},
			{
				TagKey:   aws.String("AccountEmail"),
				TagValue: aws.String(email),
			},
		},
	}
	resp, err := k.client.CreateKey(context.Background(), input)
	if err != nil {
		return nil, err
	}
	katlogger.Logger().Infof("Creating private key with key id :%v", resp.KeyMetadata.KeyId)
	return resp.KeyMetadata.KeyId, nil
}

func (k *KmsKeyStore) Sign(keyId, message string) ([]byte, error) {
	signInput := &kms.SignInput{
		Message:          []byte(message),
		KeyId:            &keyId,
		SigningAlgorithm: SigningAlgorithm,
	}
	resp, err := k.client.Sign(context.Background(), signInput)
	if err != nil {
		return nil, err
	}
	return resp.Signature, nil
}

func createKmsClient(settings *config.Settings) *kms.Client {
	if settings.Environment == common.EnvironmentDev {
		return kms.NewFromConfig(*createLocalKmsConfig())
	}
	cfg, err := awsconfig.LoadDefaultConfig(context.TODO())
	if err != nil {
		panic(err)
	}
	return kms.NewFromConfig(cfg)
}
