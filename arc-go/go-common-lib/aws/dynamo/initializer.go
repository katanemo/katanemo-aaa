package dynamo

import (
	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/config"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/db"
)

type DynamodbDbLayer struct {
	settings       *config.Settings
	dynamoDbClient *dynamodb.Client
}

func NewDynamodbDbLayer(settings *config.Settings, dynamoDbClient *dynamodb.Client) db.CoreDataAccess {
	return &DynamodbDbLayer{
		dynamoDbClient: dynamoDbClient,
		settings:       settings,
	}
}
