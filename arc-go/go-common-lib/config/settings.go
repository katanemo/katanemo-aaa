package config

import (
	"fmt"

	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib"
)

type Settings struct {
	ApiPort           int                `env:"API_PORT" envDefault:"8090"`
	ApiEndpoint       string             `env:"API_ENDPOINT" envDefault:"http://localhost:8090"`
	WwwEndpoint       string             `env:"WWW_ENDPOINT" envDefault:"http://localhost:4000"`
	AuthPort          int                `env:"AUTH_PORT" envDefault:"8081"`
	AuthArcPort       int                `env:"AUTH_ARC_PORT" envDefault:"8082"`
	CoreMetricPort    int                `env:"CORE_METRIC_PORT" envDefault:"2112"`
	AuthMetricPort    int                `env:"AUTH_METRIC_PORT" envDefault:"2113"`
	AuthArcMetricPort int                `env:"AUTH_METRIC_PORT" envDefault:"2114"`
	AuthEndpoint      string             `env:"AUTH_ENDPOINT" envDefault:"http://localhost:8081"`
	Environment       common.Environment `env:"ENVIRONMENT" envDefault:"dev"`
	AwsRegion         string             `env:"AWS_REGION" envDefault:"us-west-2"`
	AwsAccountId      string             `env:"AWS_ACCOUNT_ID" envDefault:"000000000000"`
	DbHost            string             `env:"DB_HOST" envDefault:"http://localhost:8000"`
	SnsHost           string             `env:"SNS_HOST" envDefault:"http://localhost:4566"`
	SqsHost           string             `env:"SQS_HOST" envDefault:"http://localhost:4566"`
	StsHost           string             `env:"STS_HOST" envDefault:"http://localhost:4566"`
	S3Host            string             `env:"S3_HOST" envDefault:"http://localhost:9000"`
	CognitoUrl        string             `env:"COGNITO_URL" envDefault:"http://localhost:9229"`
	SpecBucketName    string             `env:"SPEC_BUCKET" envDefault:"service-api-specs"`
	ApiYamlFile       string             `env:"API_YAML_FILE" envDefault:"../../go-common-lib/pkg/api/openapi/katanemo-aaa-api.yml"`
	SlackPanicWebhook string             `env:"SLACK_PANIC_WEBHOOK" envDefault:""`
	ArcAssumeRoleArn  string             `env:"ARC_ASSUME_ROLE_ARN" envDefault:"arn:aws:iam::264380604816:role/role-sqs-access-rafay"`
}

func (s *Settings) GetPerEnvTable(tableName string) string {
	if s.Environment == common.EnvironmentDev {
		return tableName
	}
	return fmt.Sprintf("%s-%s", tableName, s.Environment)
}
