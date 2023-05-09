package dynamo

import (
	"context"
	"fmt"
	"time"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/db"
	katlogger "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/logger"
)

func (ddb *DynamodbDbLayer) AddMetadata(metadata *common.Metadata) error {
	now := time.Now().UnixMilli()
	metadata.CreatedAt = now
	metadata.UpdatedAt = now
	metadata.Version = 1
	item, err := attributevalue.MarshalMap(metadata)

	if err != nil {
		panic(err)
	}

	tableName := ddb.settings.GetPerEnvTable(MetaTableName)
	_, err = ddb.dynamoDbClient.PutItem(context.TODO(), &dynamodb.PutItemInput{
		TableName: aws.String(tableName), Item: item,
		ConditionExpression: aws.String("attribute_not_exists(attributeName)"),
	})
	if err != nil {
		katlogger.Logger().Warnf("Couldn't add item to table. Here's why: %v", err)
	} else {
		katlogger.Logger().Infof("Successfully added metadata: key: %v", metadata.AttributeName)
	}
	return err
}

func (ddb *DynamodbDbLayer) UpdateMetadata(metadata *common.Metadata) error {
	now := time.Now().UnixMilli()
	metadata.UpdatedAt = now

	tableName := ddb.settings.GetPerEnvTable(MetaTableName)
	_, err := ddb.dynamoDbClient.UpdateItem(context.TODO(), &dynamodb.UpdateItemInput{
		TableName: aws.String(tableName),
		Key: map[string]types.AttributeValue{
			"attributeName": &types.AttributeValueMemberS{Value: metadata.AttributeName},
		},
		ExpressionAttributeValues: map[string]types.AttributeValue{
			":attributeValue": &types.AttributeValueMemberS{Value: metadata.AttributeValue},
			":updatedAt":      &types.AttributeValueMemberN{Value: fmt.Sprintf("%v", metadata.UpdatedAt)},
			":version":        &types.AttributeValueMemberN{Value: fmt.Sprintf("%v", metadata.Version)},
			":newVersion":     &types.AttributeValueMemberN{Value: fmt.Sprintf("%v", metadata.Version+1)},
		},
		ConditionExpression: aws.String("version = :version"),
		UpdateExpression:    aws.String("set attributeValue = :attributeValue, updatedAt = :updatedAt, version = :newVersion"),
	})
	if err != nil {
		katlogger.Logger().Warnf("Couldn't add item to table. Here's why: %v", err)
	} else {
		katlogger.Logger().Infof("Successfully added metadata: key: %v", metadata.AttributeName)
	}
	return err
}

func (ddb *DynamodbDbLayer) GetMetadata(key string) (*common.Metadata, error) {

	metadataObj := &common.Metadata{}

	tableName := ddb.settings.GetPerEnvTable(MetaTableName)
	response, err := ddb.dynamoDbClient.GetItem(context.TODO(), &dynamodb.GetItemInput{
		TableName: aws.String(tableName),
		Key: map[string]types.AttributeValue{
			"attributeName": &types.AttributeValueMemberS{Value: key},
		},
	})

	if err != nil {
		katlogger.Logger().Warnf("Couldn't get item from table. Here's why: %v", err)
	} else {
		if response.Item == nil {
			return nil, db.ErrMetadataNotFound
		}
		err = attributevalue.UnmarshalMap(response.Item, &metadataObj)
	}

	return metadataObj, err
}
