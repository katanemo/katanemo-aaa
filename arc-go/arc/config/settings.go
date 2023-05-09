package config

import (
	"fmt"

	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib"
)

type Settings struct {
	ApiEndpoint   string             `env:"API_ENDPOINT" envDefault:"http://localhost:8090"`
	Environment   common.Environment `env:"ENVIRONMENT" envDefault:"dev"`
	ArcMetricPort int                `env:"AUTH_METRIC_PORT" envDefault:"2115"`
	AuthArcPort   string             `env:"AUTH_ARC_PORT" envDefault:"8083"`
	ClientKey     string             `env:"CLIENT_KEY"`
	ClientSecret  string             `env:"CLIENT_SECRET"`
	AccountId     string             `env:"ACCOUNT_ID"`
	ServiceId     string             `env:"SERVICE_ID"`
}

func (s *Settings) GetPerEnvTable(tableName string) string {
	if s.Environment == common.EnvironmentDev {
		return tableName
	}
	return fmt.Sprintf("%s-%s", tableName, s.Environment)
}
