package dynamo

import (
	"context"
	"errors"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
	katlogger "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/logger"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/core/openapi"
)

var ErrSAMLConnectionNotFound = errors.New("connection object not found")

func (db *DynamodbDbLayer) AddSAMLConnection(samlObj openapi.SAMLObj) error {
	item, err := attributevalue.MarshalMap(samlObj)

	if err != nil {
		panic(err)
	}

	tableName := db.settings.GetPerEnvTable(SamlConnectionTableName)
	_, err = db.dynamoDbClient.PutItem(context.TODO(), &dynamodb.PutItemInput{
		TableName: aws.String(tableName), Item: item,
	})
	if err != nil {
		katlogger.Logger().Warnf("Couldn't add item to table. Here's why: %v", err)
	} else {
		katlogger.Logger().Infof("Successfully added Service: %v for developer: %v", samlObj.ServiceId, samlObj.AccountId)
	}
	return err
}

func (db *DynamodbDbLayer) GetSAMLConnection(connectionId string) (*openapi.SAMLObj, error) {
	devObj := &openapi.SAMLObj{}

	tableName := db.settings.GetPerEnvTable(SamlConnectionTableName)
	response, err := db.dynamoDbClient.GetItem(context.TODO(), &dynamodb.GetItemInput{
		TableName: aws.String(tableName),
		Key: map[string]types.AttributeValue{
			"connectionId": &types.AttributeValueMemberS{Value: connectionId},
		},
	})

	if err != nil {
		katlogger.Logger().Warnf("Couldn't get item from table. Here's why: %v", err)
	} else {
		if response.Item == nil {
			return nil, ErrSAMLConnectionNotFound
		}
		err = attributevalue.UnmarshalMap(response.Item, &devObj)
	}
	return devObj, err
}

func (db *DynamodbDbLayer) GetSAMLConnectionByDevService(accountId, serviceId *string) ([]openapi.SAMLObj, error) {
	var err error
	var response *dynamodb.ScanOutput
	exprObj := expression.Name("accountId").Equal(expression.Value(accountId))
	var filterExpr expression.ConditionBuilder
	if serviceId != nil {
		servObj := expression.Name("serviceId").Equal(expression.Value(*serviceId))
		filterExpr = exprObj.And(servObj)
	} else {
		filterExpr = exprObj
	}
	var saml []openapi.SAMLObj

	expr, err := expression.NewBuilder().WithFilter(filterExpr).Build()

	if err != nil {
		katlogger.Logger().Warnf("Couldn't build expressions for scan. Here's why: %v", err)
		return nil, err
	}
	tableName := db.settings.GetPerEnvTable(SamlConnectionTableName)
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

	err = attributevalue.UnmarshalListOfMaps(response.Items, &saml)
	if err != nil {
		katlogger.Logger().Warnf("Couldn't unmarshal query response. Here's why: %v", err)
		return nil, err
	}
	if len(saml) == 0 {
		return saml, nil
	}
	return saml, err
}
