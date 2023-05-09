package dynamo

import (
	"context"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
	katlogger "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/logger"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/core/openapi"
)

func (db *DynamodbDbLayer) AddOktaConnection(oktaObj openapi.OktaObj) error {
	item, err := attributevalue.MarshalMap(oktaObj)

	if err != nil {
		panic(err)
	}
	tableName := db.settings.GetPerEnvTable(OktaConnectionTableName)
	_, err = db.dynamoDbClient.PutItem(context.TODO(), &dynamodb.PutItemInput{
		TableName: aws.String(tableName), Item: item,
	})
	if err != nil {
		katlogger.Logger().Warnf("Couldn't add item to table. Here's why: %v", err)
	} else {
		katlogger.Logger().Infof("Successfully added Service: %v for developer: %v", oktaObj.ServiceId, oktaObj.AccountId)
	}
	return err
}

func (db *DynamodbDbLayer) GetOktaConnection(connectionId string) (*openapi.OktaObj, error) {
	devObj := &openapi.OktaObj{}

	tableName := db.settings.GetPerEnvTable(OktaConnectionTableName)
	response, err := db.dynamoDbClient.GetItem(context.TODO(), &dynamodb.GetItemInput{
		TableName: aws.String(tableName),
		Key: map[string]types.AttributeValue{
			"connectionId": &types.AttributeValueMemberS{Value: connectionId},
		},
	})

	if err != nil {
		katlogger.Logger().Warnf("Couldn't get item from table. Here's why: %v", err)
	} else {
		err = attributevalue.UnmarshalMap(response.Item, &devObj)
	}
	return devObj, err
}

func (db *DynamodbDbLayer) GetOktaConnectionByClient(clientId string) (*openapi.OktaObj, error) {
	var err error
	var response *dynamodb.ScanOutput
	exprObj := expression.Name("clientId").Equal(expression.Value(clientId))
	var okta []openapi.OktaObj

	expr, err := expression.NewBuilder().WithFilter(exprObj).Build()
	if err != nil {
		katlogger.Logger().Warnf("Couldn't build expressions for scan. Here's why: %v", err)
		return nil, err
	}
	tableName := db.settings.GetPerEnvTable(OktaConnectionTableName)
	response, err = db.dynamoDbClient.Scan(context.TODO(), &dynamodb.ScanInput{
		TableName:                 aws.String(tableName),
		ExpressionAttributeNames:  expr.Names(),
		ExpressionAttributeValues: expr.Values(),
		FilterExpression:          expr.Filter(),
		ProjectionExpression:      expr.Projection(),
	})
	if err != nil {
		katlogger.Logger().Warnf("Couldn't scan for services. Here's why: %v", err)
		return nil, err
	}

	err = attributevalue.UnmarshalListOfMaps(response.Items, &okta)
	if err != nil {
		katlogger.Logger().Warnf("Couldn't unmarshal query response. Here's why: %v", err)
		return nil, err
	}
	if len(okta) == 0 {
		return nil, nil
	}
	return &okta[0], err
}

func (db *DynamodbDbLayer) GetOktaConnectionByState(state string) (*openapi.OktaObj, error) {
	var err error
	var response *dynamodb.ScanOutput
	exprObj := expression.Name("state").Equal(expression.Value(state))
	var okta []openapi.OktaObj

	expr, err := expression.NewBuilder().WithFilter(exprObj).Build()
	if err != nil {
		katlogger.Logger().Warnf("Couldn't build expressions for scan. Here's why: %v", err)
		return nil, err
	}
	tableName := db.settings.GetPerEnvTable(OktaConnectionTableName)
	response, err = db.dynamoDbClient.Scan(context.TODO(), &dynamodb.ScanInput{
		TableName:                 aws.String(tableName),
		ExpressionAttributeNames:  expr.Names(),
		ExpressionAttributeValues: expr.Values(),
		FilterExpression:          expr.Filter(),
		ProjectionExpression:      expr.Projection(),
	})
	if err != nil {
		katlogger.Logger().Warnf("Couldn't scan for services. Here's why: %v", err)
		return nil, err
	}

	err = attributevalue.UnmarshalListOfMaps(response.Items, &okta)
	if err != nil {
		katlogger.Logger().Warnf("Couldn't unmarshal query response. Here's why: %v", err)
		return nil, err
	}
	if len(okta) == 0 {
		return nil, nil
	}
	return &okta[0], err
}

func (db *DynamodbDbLayer) GetOktaConnectionsByAccount(accountId string) ([]openapi.OktaObj, error) {
	var err error
	var response *dynamodb.ScanOutput
	exprObj := expression.Name("accountId").Equal(expression.Value(accountId))
	var okta []openapi.OktaObj

	expr, err := expression.NewBuilder().WithFilter(exprObj).Build()
	if err != nil {
		katlogger.Logger().Warnf("Couldn't build expressions for scan. Here's why: %v", err)
		return nil, err
	}
	tableName := db.settings.GetPerEnvTable(OktaConnectionTableName)
	response, err = db.dynamoDbClient.Scan(context.TODO(), &dynamodb.ScanInput{
		TableName:                 aws.String(tableName),
		ExpressionAttributeNames:  expr.Names(),
		ExpressionAttributeValues: expr.Values(),
		FilterExpression:          expr.Filter(),
		ProjectionExpression:      expr.Projection(),
	})
	if err != nil {
		katlogger.Logger().Warnf("Couldn't scan for services. Here's why: %v", err)
		return nil, err
	}

	err = attributevalue.UnmarshalListOfMaps(response.Items, &okta)
	if err != nil {
		katlogger.Logger().Warnf("Couldn't unmarshal query response. Here's why: %v", err)
		return nil, err
	}

	return okta, err
}
