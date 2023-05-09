package kms

import (
	"context"
	"os"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/credentials"
)

func createLocalKmsConfig() *aws.Config {
	awsRegion := "us-west-1"
	if awsRegionEnv := os.Getenv("AWS_REGION"); awsRegionEnv != "" {
		awsRegion = awsRegionEnv
	}

	cfg, err := config.LoadDefaultConfig(context.TODO(),
		config.WithRegion(awsRegion),
		config.WithEndpointResolverWithOptions(aws.EndpointResolverWithOptionsFunc(
			func(service, region string, options ...interface{}) (aws.Endpoint, error) {
				// TODO: temporary hack for running our service in docker container or on host machine
				// if running on host machine then use loclhost, if running in a docker container then use host.docker.internal
				kmsHostEndpoint := os.Getenv("KMS_HOST")
				if kmsHostEndpoint == "" {
					kmsHostEndpoint = "http://localhost:8082"
				}
				return aws.Endpoint{URL: kmsHostEndpoint}, nil
			})),
		config.WithCredentialsProvider(credentials.StaticCredentialsProvider{
			Value: aws.Credentials{
				AccessKeyID: "dummy", SecretAccessKey: "dummy", SessionToken: "dummy",
				Source: "Hard-coded credentials; values are irrelevant for local DynamoDB",
			},
		}),
	)
	if err != nil {
		panic(err)
	}
	return &cfg
}
