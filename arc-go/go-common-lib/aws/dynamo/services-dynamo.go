package dynamo

import (
	"context"
	"fmt"
	"time"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/db"
	katlogger "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/logger"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/core/openapi"
)

func (db *DynamodbDbLayer) AddService(apiservice *openapi.Service) (*openapi.Service, error) {
	item, err := attributevalue.MarshalMap(apiservice)

	if err != nil {
		panic(err)
	}
	tableName := db.settings.GetPerEnvTable(ServicesTableName)
	_, err = db.dynamoDbClient.PutItem(context.TODO(), &dynamodb.PutItemInput{
		TableName: aws.String(tableName), Item: item,
		ConditionExpression: aws.String("attribute_not_exists(serviceId)"),
	})
	if err != nil {
		katlogger.Logger().Warnf("Couldn't add item to table. Here's why: %v", err)
	} else {
		katlogger.Logger().Infof("Successfully added Service: %v", *apiservice.Servicename)
	}
	return db.GetService(*apiservice.ServiceId)
}

func (db *DynamodbDbLayer) UpdateService(apiservice *openapi.Service) (*openapi.Service, error) {
	tableName := db.settings.GetPerEnvTable(ServicesTableName)

	serviceFromDb, err := db.GetService(*apiservice.ServiceId)
	if err != nil {
		return nil, err
	}

	description := ""
	if apiservice.Description != nil {
		description = *apiservice.Description
	}
	redirectURL := ""
	if apiservice.RedirectURL != nil {
		redirectURL = *apiservice.RedirectURL
	}
	vals := map[string]types.AttributeValue{
		":description": &types.AttributeValueMemberS{Value: description},
		":redirectUrl": &types.AttributeValueMemberS{Value: redirectURL},
		":serviceName": &types.AttributeValueMemberS{Value: *apiservice.Servicename},
		":updatedAt":   &types.AttributeValueMemberN{Value: fmt.Sprintf("%v", time.Now().UnixMilli())},
		":version":     &types.AttributeValueMemberN{Value: fmt.Sprintf("%v", *serviceFromDb.Version)},
		":newVersion":  &types.AttributeValueMemberN{Value: fmt.Sprintf("%v", *serviceFromDb.Version+1)},
	}

	if apiservice.Apis != nil {
		vals[":apiPaths"] = &types.AttributeValueMemberSS{Value: *apiservice.Apis}
	} else {
		vals[":apiPaths"] = &types.AttributeValueMemberSS{Value: []string{""}}
	}

	_, err = db.dynamoDbClient.UpdateItem(context.TODO(), &dynamodb.UpdateItemInput{
		TableName: aws.String(tableName),
		Key: map[string]types.AttributeValue{
			"serviceId": &types.AttributeValueMemberS{Value: *apiservice.ServiceId},
		},
		ExpressionAttributeValues: vals,
		ConditionExpression:       aws.String("version = :version"),
		UpdateExpression:          aws.String("set serviceName = :serviceName, description = :description, redirectUrl = :redirectUrl, updatedAt = :updatedAt, version = :newVersion, apiPaths = :apiPaths"),
	})

	if err != nil {
		katlogger.Logger().Warnf("Couldn't add item to table. Here's why: %v", err)
	} else {
		katlogger.Logger().Infof("Successfully added Service: %v", *apiservice.Servicename)
	}
	return db.GetService(*apiservice.ServiceId)
}

func (ddb *DynamodbDbLayer) GetService(serviceId string) (*openapi.Service, error) {
	devObj := &openapi.Service{}

	response, err := ddb.dynamoDbClient.GetItem(context.TODO(), &dynamodb.GetItemInput{
		TableName: aws.String(ddb.settings.GetPerEnvTable(ServicesTableName)),
		Key: map[string]types.AttributeValue{
			"serviceId": &types.AttributeValueMemberS{Value: serviceId},
		},
	})

	if err != nil {
		katlogger.Logger().Warnf("Couldn't get item from table. Here's why: %v", err)
	} else {
		if response.Item == nil {

			return nil, db.ErrServiceNotFound
		}

		err = attributevalue.UnmarshalMap(response.Item, &devObj)
	}
	return devObj, err
}
