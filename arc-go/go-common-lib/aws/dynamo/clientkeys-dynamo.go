package dynamo

import (
	"context"
	"fmt"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/db"
	katlogger "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/logger"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/core/openapi"
)

func (db *DynamodbDbLayer) AddClientKeys(clientKeyObject *openapi.ClientKeyObject) error {
	item, err := attributevalue.MarshalMap(clientKeyObject)

	if err != nil {
		panic(err)
	}

	tableName := db.settings.GetPerEnvTable(ClientKeysTableName)
	_, err = db.dynamoDbClient.PutItem(context.TODO(), &dynamodb.PutItemInput{
		TableName: aws.String(tableName), Item: item,
	})
	if err != nil {
		katlogger.Logger().Warnf("Couldn't add item to table. Here's why: %v", err)
	} else {
		katlogger.Logger().Infof("Successfully added Service: %v for developer: %v", clientKeyObject.AccountId, clientKeyObject.ClientKeyId)
	}
	return err
}

func (ddb *DynamodbDbLayer) GetClientKey(accountId *string, clientKeyId *string) (*openapi.ClientKeyObject, error) {

	clientKeyObj := &openapi.ClientKeyObject{}

	tableName := ddb.settings.GetPerEnvTable(ClientKeysTableName)
	response, err := ddb.dynamoDbClient.GetItem(context.TODO(), &dynamodb.GetItemInput{
		TableName: aws.String(tableName),
		Key: map[string]types.AttributeValue{
			"accountId":   &types.AttributeValueMemberS{Value: *accountId},
			"clientKeyId": &types.AttributeValueMemberS{Value: *clientKeyId},
		},
	})

	if err != nil {
		katlogger.Logger().Warnf("Couldn't get item from table. Here's why: %v", err)
	} else {
		if response.Item == nil {
			return nil, db.ErrClientKeyNotFound
		}
		err = attributevalue.UnmarshalMap(response.Item, &clientKeyObj)
	}

	if err != nil && clientKeyObj.IsActive != nil && !*clientKeyObj.IsActive {
		return nil, db.ErrClientKeyNotFound
	}
	return clientKeyObj, err
}

func (db *DynamodbDbLayer) GetClientKeyList(accountId *string) ([]*openapi.ClientKeyObject, error) {

	tableName := db.settings.GetPerEnvTable(ClientKeysTableName)
	keyCond := expression.Key("accountId").Equal(expression.Value(*accountId))

	expr, err := expression.NewBuilder().
		WithKeyCondition(keyCond).
		Build()

	if err != nil {
		return nil, err
	}

	result, err := db.dynamoDbClient.Query(context.TODO(), &dynamodb.QueryInput{
		TableName:                 aws.String(tableName),
		KeyConditionExpression:    expr.KeyCondition(),
		ExpressionAttributeNames:  expr.Names(),
		ExpressionAttributeValues: expr.Values(),
	})

	if err != nil {
		return nil, fmt.Errorf("Couldn't get item from table. Here's why: %w", err)
	}

	clientKeyObjList := []*openapi.ClientKeyObject{}

	if len(result.Items) == 0 {
		return clientKeyObjList, nil
	}

	err = attributevalue.UnmarshalListOfMaps(result.Items, &clientKeyObjList)

	activeKeys := []*openapi.ClientKeyObject{}

	for _, key := range clientKeyObjList {
		if key.IsActive == nil || *key.IsActive {
			activeKeys = append(activeKeys, key)
		}
	}

	return activeKeys, err
}

func (db *DynamodbDbLayer) DeleteClientKey(accountId, clientKeyId *string) (*openapi.ClientKeyObject, error) {
	tableName := db.settings.GetPerEnvTable(ClientKeysTableName)

	clientKey, err := db.GetClientKey(accountId, clientKeyId)
	if err != nil {
		return nil, err
	}

	if err != nil {
		katlogger.Logger().Warnf("Couldn't get item from table. Here's why: %v", err)
	}

	update := expression.Set(expression.Name("isActive"), expression.Value(false))
	expr, err := expression.NewBuilder().WithUpdate(update).Build()
	if err != nil {
		log.Printf("Couldn't build expression for update. Here's why: %v\n", err)
	} else {
		_, err = db.dynamoDbClient.UpdateItem(context.TODO(), &dynamodb.UpdateItemInput{
			TableName: aws.String(tableName),
			Key: map[string]types.AttributeValue{
				"accountId":   &types.AttributeValueMemberS{Value: *accountId},
				"clientKeyId": &types.AttributeValueMemberS{Value: *clientKeyId},
			},
			ExpressionAttributeNames:  expr.Names(),
			ExpressionAttributeValues: expr.Values(),
			UpdateExpression:          expr.Update(),
		})
	}

	return clientKey, err
}
