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
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/db"
	katlogger "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/logger"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/core/openapi"
)

func (ddb *DynamodbDbLayer) AddSubscription(entity db.Subscription) error {
	item, err := attributevalue.MarshalMap(entity)

	if err != nil {
		panic(err)
	}
	tableName := ddb.settings.GetPerEnvTable(SubscriptionsTableName)
	_, err = ddb.dynamoDbClient.PutItem(context.TODO(), &dynamodb.PutItemInput{
		TableName: aws.String(tableName), Item: item,
	})
	if err != nil {
		katlogger.Logger().Warnf("Couldn't add item to table. Here's why: %v", err)
	} else {
		katlogger.Logger().Infof("Successfully added subscriber: %v", entity.SubscriberId)
	}
	return err
}

func (db *DynamodbDbLayer) AddDeveloper(entity openapi.Developer) error {
	nowMilli := time.Now().UnixMilli()
	entity.UpdatedAt = &nowMilli
	entity.CreatedAt = &nowMilli
	entity.Version = aws.Int(1)
	item, err := attributevalue.MarshalMap(entity)

	if err != nil {
		panic(err)
	}
	tableName := db.settings.GetPerEnvTable(ConstTableNameAccount)
	_, err = db.dynamoDbClient.PutItem(context.TODO(), &dynamodb.PutItemInput{
		TableName:           aws.String(tableName),
		Item:                item,
		ConditionExpression: aws.String("attribute_not_exists(accountId)"),
	})
	if err != nil {
		katlogger.Logger().Warnf("Couldn't add item to table. Here's why: %v", err)
	} else {
		katlogger.Logger().Infof("Successfully added Entity: %v", *entity.Developer)
	}
	return err
}

func (db *DynamodbDbLayer) UpdateDeveloper(entity openapi.Developer) error {
	entity.UpdatedAt = aws.Int64(time.Now().UnixMilli())
	item, err := attributevalue.MarshalMap(entity)
	if err != nil {
		return err
	}

	tableName := db.settings.GetPerEnvTable(ConstTableNameAccount)

	_, err = db.dynamoDbClient.UpdateItem(context.TODO(), &dynamodb.UpdateItemInput{
		TableName: aws.String(tableName),
		Key: map[string]types.AttributeValue{
			"accountId": &types.AttributeValueMemberS{Value: *entity.AccountId},
		},
		ExpressionAttributeValues: map[string]types.AttributeValue{
			":developer":          item["developer"],
			":isactive":           item["isactive"],
			":launchedServices":   item["launchedServices"],
			":subscribedServices": item["subscribedServices"],
			":updatedAt":          item["updatedAt"],
			":version":            item["version"],
			":newVersion":         &types.AttributeValueMemberN{Value: fmt.Sprintf("%v", *entity.Version+1)},
		},
		ConditionExpression: aws.String("version = :version"),
		UpdateExpression:    aws.String("set developer = :developer, isactive = :isactive, launchedServices = :launchedServices, subscribedServices = :subscribedServices, updatedAt = :updatedAt, version = :newVersion"),
	})
	if err != nil {
		katlogger.Logger().Warnf("Couldn't add item to table. Here's why: %v", err)
	} else {
		katlogger.Logger().Infof("Successfully added Entity: %v", *entity.Developer)
	}
	return err
}

func (ddb *DynamodbDbLayer) GetDeveloper(accountId *string) (*openapi.Developer, error) {
	entity := &openapi.Developer{}
	tableName := ddb.settings.GetPerEnvTable(ConstTableNameAccount)
	response, err := ddb.dynamoDbClient.GetItem(context.TODO(), &dynamodb.GetItemInput{
		TableName: aws.String(tableName),
		Key: map[string]types.AttributeValue{
			ConstAttrAccountId: &types.AttributeValueMemberS{Value: *accountId},
		},
	})

	if err != nil {
		katlogger.Logger().Warnf("Couldn't get item from table. Here's why: %v", err)
	} else {
		if response.Item == nil {

			return nil, db.ErrDeveloperNotFound
		}
		err = attributevalue.UnmarshalMap(response.Item, &entity)
	}
	return entity, err
}

func (ddb *DynamodbDbLayer) GetDeveloperByServiceAndEmail(serviceId, email string) (*openapi.Developer, error) {
	keyCond := expression.Key("email").Equal(expression.Value(email))
	expr, err := expression.NewBuilder().
		WithKeyCondition(keyCond).
		Build()

	if err != nil {
		katlogger.Logger().Warnf("Couldn't build expression. Here's why: %v", err)
		return nil, err
	}

	tableName := ddb.settings.GetPerEnvTable(ConstTableNameAccount)
	response, err := ddb.dynamoDbClient.Query(context.Background(), &dynamodb.QueryInput{
		TableName:                 &tableName,
		IndexName:                 aws.String("account-email-index"),
		KeyConditionExpression:    expr.KeyCondition(),
		ExpressionAttributeNames:  expr.Names(),
		ExpressionAttributeValues: expr.Values(),
	})

	if err != nil {
		katlogger.Logger().Warnf("Couldn't query for developer. Here's why: %v", err)
		return nil, err
	}

	var developer []openapi.Developer
	err = attributevalue.UnmarshalListOfMaps(response.Items, &developer)
	if err != nil {
		katlogger.Logger().Warnf("Couldn't unmarshal query response. Here's why: %v", err)
		return nil, err
	}
	for _, d := range developer {
		for _, s := range *d.SubscribedServices {
			if s == serviceId {
				return &d, nil
			}
		}
	}

	return nil, db.ErrDeveloperNotWithWithService
}

func (ddb *DynamodbDbLayer) GetDeveloperByServiceId(serviceId string) (*openapi.Developer, error) {
	serviceObj, err := ddb.GetService(serviceId)
	if err != nil {
		katlogger.Logger().Warnf("Could not find the service, with ID: %v", serviceId)
		return nil, err
	}

	var developerObj openapi.Developer
	response, err := DDBGetItemFromAccountTable(ConstAttrAccountId, *serviceObj.AccountId, ddb)
	if err != nil {
		katlogger.Logger().Warnf("Couldn't get item from table. Here's why: %v", err)
	} else {
		if response.Item == nil {
			return nil, db.ErrDeveloperNotFound
		}
		err = attributevalue.UnmarshalMap(response.Item, &developerObj)

		if err != nil {
			katlogger.Logger().Warnf("Couldn't unmarshal query response. Here's why: %v", err)
			return nil, err
		}
	}
	return &developerObj, nil
}

func (ddb *DynamodbDbLayer) GetSubscriptionsForDeveloper(accountId string) (*[]db.Subscription, error) {
	var subscriptions []db.Subscription

	keyCond := expression.Key(ConstAttrAccountId).Equal(expression.Value(accountId))
	expr, err := expression.NewBuilder().
		WithKeyCondition(keyCond).
		Build()

	if err != nil {
		katlogger.Logger().Infof("Couldn't build expressions for query. Here's why: %v", err)
		return nil, err
	}

	tableName := ddb.settings.GetPerEnvTable(SubscriptionsTableName)

	response, err := ddb.dynamoDbClient.Query(context.Background(), &dynamodb.QueryInput{
		TableName:                 &tableName,
		KeyConditionExpression:    expr.KeyCondition(),
		ExpressionAttributeNames:  expr.Names(),
		ExpressionAttributeValues: expr.Values(),
	})

	if err != nil {
		katlogger.Logger().Infof("Query failed. Here's why: %v", err)
		return nil, err
	}

	err = attributevalue.UnmarshalListOfMaps(response.Items, &subscriptions)
	if err != nil {
		katlogger.Logger().Warnf("Couldn't unmarshal query response. Here's why: %v", err)
		return nil, err
	}

	return &subscriptions, nil
}

// Helper method to get an item from the account table.
func DDBGetItemFromAccountTable(attributeName string, attributeValue string, ddb *DynamodbDbLayer) (*dynamodb.GetItemOutput, error) {
	tableName := ddb.settings.GetPerEnvTable(ConstTableNameAccount)
	return getDDBItem(tableName, attributeName, attributeValue, ddb)
}

// Helper method to get an item from the account table.
func DDBGetItemFromServiceTable(attributeName string, attributeValue string, ddb *DynamodbDbLayer) (*dynamodb.GetItemOutput, error) {
	tableName := ddb.settings.GetPerEnvTable(ConstTableNameAccount)
	return getDDBItem(tableName, attributeName, attributeValue, ddb)
}

// Helper method to get an item from DDB for any arbitrary table with attrbute key/value pair
func getDDBItem(tableName string, attributeName string, attributeValue string, ddb *DynamodbDbLayer) (*dynamodb.GetItemOutput, error) {
	return ddb.dynamoDbClient.GetItem(context.TODO(), &dynamodb.GetItemInput{
		TableName: aws.String(tableName),
		Key: map[string]types.AttributeValue{
			attributeName: &types.AttributeValueMemberS{Value: attributeValue},
		},
	})
}
