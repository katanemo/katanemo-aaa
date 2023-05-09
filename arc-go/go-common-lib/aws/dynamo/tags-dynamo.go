package dynamo

import (
	"context"
	"fmt"
	"time"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
	katlogger "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/logger"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/core/openapi"
)

func (db *DynamodbDbLayer) AddTags(tags *openapi.Tags) (*openapi.Tags, error) {
	nowMilli := time.Now().UnixMilli()
	tags.UpdatedAt = &nowMilli
	tags.CreatedAt = &nowMilli
	tags.Version = aws.Int(1)
	item, err := attributevalue.MarshalMap(tags)

	if err != nil {
		panic(err)
	}
	tableName := db.settings.GetPerEnvTable(TagsTableName)
	_, err = db.dynamoDbClient.PutItem(context.TODO(), &dynamodb.PutItemInput{
		TableName: aws.String(tableName), Item: item,
		ConditionExpression: aws.String("attribute_not_exists(serviceIdPath) AND attribute_not_exists(resourceId)"),
	})
	if err != nil {
		katlogger.Logger().Warnf("Couldn't add item to table. Here's why: %v", err)
	}
	return db.GetTags(tags.ServiceId, *tags.AccountId, tags.Name, tags.ResourceId)
}

func (ddb *DynamodbDbLayer) UpdateTags(tags *openapi.Tags) (*openapi.Tags, error) {
	nowMilli := time.Now().UnixMilli()
	tags.UpdatedAt = &nowMilli
	item, err := attributevalue.MarshalMap(tags)
	if err != nil {
		return nil, fmt.Errorf("could not update tags: %w", err)
	}

	// ensure that the tags exist
	_, err = ddb.GetTags(tags.ServiceId, *tags.AccountId, tags.Name, tags.ResourceId)
	if err != nil {
		return nil, fmt.Errorf("could not get tags from db: %w", err)
	}

	key := fmt.Sprintf("%v_%v", tags.ServiceId, tags.Name)

	tableName := ddb.settings.GetPerEnvTable(TagsTableName)

	_, err = ddb.dynamoDbClient.UpdateItem(context.TODO(), &dynamodb.UpdateItemInput{
		TableName: aws.String(tableName),
		Key: map[string]types.AttributeValue{
			"serviceIdPath": &types.AttributeValueMemberS{Value: key},
			"resourceId":    &types.AttributeValueMemberS{Value: tags.ResourceId},
		},
		ExpressionAttributeValues: map[string]types.AttributeValue{
			":tags":       item["tags"],
			":updatedAt":  &types.AttributeValueMemberN{Value: fmt.Sprintf("%v", *tags.UpdatedAt)},
			":version":    &types.AttributeValueMemberN{Value: fmt.Sprintf("%v", *tags.Version)},
			":newVersion": &types.AttributeValueMemberN{Value: fmt.Sprintf("%v", *tags.Version+1)},
		},
		ConditionExpression: aws.String("version = :version"),
		UpdateExpression:    aws.String("set tags = :tags, updatedAt = :updatedAt, version = :newVersion"),
	})

	if err != nil {
		katlogger.Logger().Warnf("Couldn't add item to table. Here's why: %v", err)
		return nil, err
	}
	return ddb.GetTags(tags.ServiceId, *tags.AccountId, tags.Name, tags.ResourceId)
}

func (db *DynamodbDbLayer) GetTags(serviceId, accountId, name, resourceId string) (*openapi.Tags, error) {
	tagsObj := &openapi.Tags{}
	key := fmt.Sprintf("%v_%v", serviceId, name)
	tableName := db.settings.GetPerEnvTable(TagsTableName)
	response, err := db.dynamoDbClient.GetItem(context.TODO(), &dynamodb.GetItemInput{
		TableName: aws.String(tableName),
		Key: map[string]types.AttributeValue{
			"serviceIdPath": &types.AttributeValueMemberS{Value: key},
			"resourceId":    &types.AttributeValueMemberS{Value: resourceId},
		},
	})

	if err != nil {
		katlogger.Logger().Warnf("Couldn't get item from table. Here's why: %v", err)
	} else {
		err = attributevalue.UnmarshalMap(response.Item, &tagsObj)
	}
	return tagsObj, err
}

func (ddb *DynamodbDbLayer) GetTagsForService(serviceId string, limit int) ([]openapi.Tags, error) {
	var tags []openapi.Tags

	filterExpr := expression.Key("serviceId").Equal(expression.Value(serviceId))

	expr, err := expression.NewBuilder().
		WithKeyCondition(filterExpr).
		Build()

	if err != nil {
		katlogger.Logger().Warnf("Couldn't build expression. Here's why: %v", err)
		return nil, err
	}

	tableName := ddb.settings.GetPerEnvTable(TagsTableName)
	response, err := ddb.dynamoDbClient.Query(context.Background(), &dynamodb.QueryInput{
		TableName:                 &tableName,
		IndexName:                 aws.String("serviceId-updatedAt-index"),
		KeyConditionExpression:    expr.KeyCondition(),
		ExpressionAttributeNames:  expr.Names(),
		ExpressionAttributeValues: expr.Values(),
		ScanIndexForward:          aws.Bool(false),
		Limit:                     aws.Int32(int32(limit)),
		ProjectionExpression:      expr.Projection(),
	})

	if err != nil {
		katlogger.Logger().Warnf("Couldn't query for tags. Here's why: %v", err)
	} else {
		err = attributevalue.UnmarshalListOfMaps(response.Items, &tags)
		if err != nil {
			katlogger.Logger().Warnf("Couldn't unmarshal query response. Here's why: %v", err)
		}
	}

	return tags, err
}
