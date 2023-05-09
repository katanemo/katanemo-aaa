package aws

import (
	"context"

	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib"
	katconfig "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/config"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/credentials"
	"github.com/aws/aws-sdk-go-v2/service/s3"
	"github.com/aws/aws-sdk-go-v2/service/sns"
	"github.com/aws/aws-sdk-go-v2/service/sqs"
	"github.com/aws/aws-sdk-go-v2/service/sts"
)

func CreateAWSSnsClientConfig(settings *katconfig.Settings) *aws.Config {
	if settings.Environment == common.EnvironmentDev {
		return CreateLocalAWSClient(settings.AwsRegion, settings.SnsHost)
	}

	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		panic(err)
	}
	return &cfg
}

func CreateSnsClient(settings *katconfig.Settings) *sns.Client {
	cfg := CreateAWSSnsClientConfig(settings)
	return sns.NewFromConfig(*cfg)
}

func CreateAWSDDBClientConfig(settings *katconfig.Settings) *aws.Config {
	if settings.Environment == common.EnvironmentDev {
		return CreateLocalAWSClient(settings.AwsRegion, settings.DbHost)
	}

	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		panic(err)
	}
	return &cfg
}

func CreateLocalAWSClient(awsRegion, host string) *aws.Config {
	customResolver := aws.EndpointResolverWithOptionsFunc(func(service, region string, options ...interface{}) (aws.Endpoint, error) {
		return aws.Endpoint{
			PartitionID:   "aws",
			URL:           host,
			SigningRegion: awsRegion,
		}, nil
	})

	cfg, err := config.LoadDefaultConfig(context.TODO(), config.WithEndpointResolverWithOptions(customResolver))
	if err != nil {
		panic(err)
	}
	return &cfg
}

func CreateLocalS3ClientConfig(settings *katconfig.Settings) *aws.Config {
	staticResolver := aws.EndpointResolverWithOptionsFunc(func(service, region string, options ...interface{}) (aws.Endpoint, error) {
		return aws.Endpoint{
			PartitionID:       "aws",
			URL:               settings.S3Host,
			SigningRegion:     settings.AwsRegion,
			HostnameImmutable: true,
		}, nil
	})

	s3Config := &aws.Config{
		Credentials:                 credentials.NewStaticCredentialsProvider("minioadmin", "minioadmin", ""),
		EndpointResolverWithOptions: staticResolver,
	}

	return s3Config
}

func CreateS3ClientConfig(settings *katconfig.Settings) *aws.Config {
	if settings.Environment == common.EnvironmentDev {
		return CreateLocalS3ClientConfig(settings)
	} else {
		cfg, err := config.LoadDefaultConfig(context.TODO())
		if err != nil {
			panic(err)
		}
		return &cfg
	}
}

func CreateS3AccessLogsClientConfig(settings *katconfig.Settings) *aws.Config {
	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		panic(err)
	}
	return &cfg
}

func CreateS3Client(settings *katconfig.Settings) *s3.Client {
	cfg := CreateS3ClientConfig(settings)
	return s3.NewFromConfig(*cfg)
}

func CreateS3AccessLogsClient(settings *katconfig.Settings) *s3.Client {
	cfg := CreateS3AccessLogsClientConfig(settings)
	return s3.NewFromConfig(*cfg)
}
func CreateAWSSqsClientConfig(settings *katconfig.Settings) *aws.Config {
	if settings.Environment == common.EnvironmentDev {
		return CreateLocalAWSClient(settings.AwsRegion, settings.SqsHost)
	}

	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		panic(err)
	}
	return &cfg
}

func CreateSqsClient(settings *katconfig.Settings) *sqs.Client {
	cfg := CreateAWSSqsClientConfig(settings)
	return sqs.NewFromConfig(*cfg)
}

func CreateAWSStsClientConfig(settings *katconfig.Settings) *aws.Config {
	if settings.Environment == common.EnvironmentDev {
		return CreateLocalAWSClient(settings.AwsRegion, settings.StsHost)
	}

	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		panic(err)
	}
	return &cfg
}

func CreateStsClient(settings *katconfig.Settings) *sts.Client {
	cfg := CreateAWSStsClientConfig(settings)
	return sts.NewFromConfig(*cfg)
}
