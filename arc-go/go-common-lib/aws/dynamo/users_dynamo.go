package dynamo

import (
	"context"
	"fmt"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
	katlogger "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/logger"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/core/openapi"
)

func (db *DynamodbDbLayer) AddUser(userObj openapi.User) error {

	item, err := attributevalue.MarshalMap(userObj)

	if err != nil {
		panic(err)
	}
	tableName := db.settings.GetPerEnvTable(UsersTableName)
	_, err = db.dynamoDbClient.PutItem(context.TODO(), &dynamodb.PutItemInput{
		TableName: aws.String(tableName), Item: item,
	})
	if err != nil {
		katlogger.Logger().Warnf("Couldn't add item to table. Here's why: %v", err)
	} else {
		katlogger.Logger().Infof("Successfully added User: %v", *userObj.UserId)
	}
	return err
}

func (db *DynamodbDbLayer) GetUser(accountId string, userId string) (*openapi.User, error) {
	userObj := &openapi.User{}

	tableName := db.settings.GetPerEnvTable(UsersTableName)
	response, err := db.dynamoDbClient.GetItem(context.TODO(), &dynamodb.GetItemInput{
		TableName: aws.String(tableName),
		Key: map[string]types.AttributeValue{
			"accountId": &types.AttributeValueMemberS{Value: accountId},
			"userId":    &types.AttributeValueMemberS{Value: userId},
		},
	})

	if err != nil {
		katlogger.Logger().Warnf("Couldn't get item from table. Here's why: %v", err)
	} else {
		err = attributevalue.UnmarshalMap(response.Item, &userObj)
	}
	return userObj, err
}

func (db *DynamodbDbLayer) GetUsersByAccountId(accountId string) (*[]openapi.User, error) {

	keyCond := expression.Key("accountId").Equal(expression.Value(accountId))

	expr, err := expression.NewBuilder().
		WithKeyCondition(keyCond).
		Build()

	if err != nil {
		katlogger.Logger().Infof("Couldn't build expressions for query. Here's why: %v", err)
		return nil, err
	}
	tableName := db.settings.GetPerEnvTable(UsersTableName)

	response, err := db.dynamoDbClient.Query(context.TODO(), &dynamodb.QueryInput{
		TableName:                 aws.String(tableName),
		KeyConditionExpression:    expr.KeyCondition(),
		ExpressionAttributeNames:  expr.Names(),
		ExpressionAttributeValues: expr.Values(),
	})

	if err != nil {
		katlogger.Logger().Warnf("Couldn't scan for services. Here's why: %v", err)
		return nil, err
	}

	var users []openapi.User
	err = attributevalue.UnmarshalListOfMaps(response.Items, &users)
	if err != nil {
		katlogger.Logger().Warnf("Couldn't unmarshal query response. Here's why: %v", err)
		return nil, err
	}

	return &users, err
}

func (db *DynamodbDbLayer) GetUserByServiceIdAndUserId(serviceId, userId string) (*openapi.User, error) {

	var users []openapi.User

	serviceExp := expression.Key("serviceId").Equal(expression.Value(serviceId))
	userExp := expression.Key("userId").Equal(expression.Value(userId))
	exp := serviceExp.And(userExp)

	expr, err := expression.NewBuilder().
		WithKeyCondition(exp).
		Build()

	if err != nil {
		katlogger.Logger().Warnf("Couldn't build expression. Here's why: %v", err)
		return nil, err
	}

	tableName := db.settings.GetPerEnvTable(UsersTableName)
	response, err := db.dynamoDbClient.Query(context.Background(), &dynamodb.QueryInput{
		TableName:                 aws.String(tableName),
		IndexName:                 aws.String("serviceId-userId-index"),
		KeyConditionExpression:    expr.KeyCondition(),
		ExpressionAttributeNames:  expr.Names(),
		ExpressionAttributeValues: expr.Values(),
		// ScanIndexForward:          aws.Bool(false),
		// Limit:                     aws.Int32(int32(2)),
		// ProjectionExpression: expr.Projection(),
	})

	if err != nil {
		katlogger.Logger().Warnf("Couldn't query for roles. Here's why: %v", err)
	} else {
		err = attributevalue.UnmarshalListOfMaps(response.Items, &users)
		if err != nil {
			katlogger.Logger().Warnf("Couldn't unmarshal query response. Here's why: %v", err)
		}
	}

	if len(users) > 1 {
		return nil, fmt.Errorf("One user supposed to be returned, but %d users returned", len(users))
	}

	if len(users) == 0 {
		return nil, nil
	}

	return &users[0], err
}
