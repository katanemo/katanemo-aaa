package dynamo

import (
	"context"
	"errors"
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

var ErrRoleNotFound = errors.New("role not found")

func (db *DynamodbDbLayer) AddRole(role *openapi.Role) (*openapi.Role, error) {
	nowMilli := time.Now().UnixMilli()
	role.UpdatedAt = &nowMilli
	role.CreatedAt = &nowMilli
	role.Version = aws.Int(1)
	item, err := attributevalue.MarshalMap(role)

	if err != nil {
		panic(err)
	}

	tableName := db.settings.GetPerEnvTable(RolesTableName)
	_, err = db.dynamoDbClient.PutItem(context.TODO(), &dynamodb.PutItemInput{
		TableName:           aws.String(tableName),
		Item:                item,
		ConditionExpression: aws.String("attribute_not_exists(accountId) AND attribute_not_exists(roleId)"),
	})
	if err != nil {
		katlogger.Logger().Warnf("Couldn't add item to table. Here's why: %v", err)
	} else {
		katlogger.Logger().Infof("Successfully added Service: %v", *role.Rolename)
	}
	return db.GetRole(role.AccountId, role.RoleId)
}

func (ddb *DynamodbDbLayer) UpdateRole(accountId, roleId string, roleObj *openapi.Role) (*openapi.Role, error) {
	nowMilli := time.Now().UnixMilli()
	roleObj.UpdatedAt = &nowMilli

	roleFromDb, err := ddb.GetRole(&accountId, &roleId)
	if err != nil {
		return nil, err
	}

	if *roleObj.AccountId != accountId ||
		*roleObj.RoleId != roleId ||
		*roleObj.ServiceId != *roleFromDb.ServiceId {
		return nil, errors.New("role update not allowed")
	}

	item, err := attributevalue.MarshalMap(roleObj)
	if err != nil {
		return nil, err
	}

	tableName := ddb.settings.GetPerEnvTable(RolesTableName)
	_, err = ddb.dynamoDbClient.UpdateItem(context.TODO(), &dynamodb.UpdateItemInput{
		TableName: aws.String(tableName),
		Key: map[string]types.AttributeValue{
			"accountId": &types.AttributeValueMemberS{Value: accountId},
			"roleId":    &types.AttributeValueMemberS{Value: roleId},
		},
		ExpressionAttributeValues: map[string]types.AttributeValue{
			":rolename":   item["rolename"],
			":policies":   item["policies"],
			":updatedAt":  &types.AttributeValueMemberN{Value: fmt.Sprintf("%v", *roleObj.UpdatedAt)},
			":version":    &types.AttributeValueMemberN{Value: fmt.Sprintf("%v", *roleObj.Version)},
			":newVersion": &types.AttributeValueMemberN{Value: fmt.Sprintf("%v", *roleFromDb.Version+1)},
		},
		ConditionExpression: aws.String("version = :version"),
		UpdateExpression:    aws.String("set rolename = :rolename, policies = :policies, updatedAt = :updatedAt, version = :newVersion"),
	})
	if err != nil {
		katlogger.Logger().Warnf("Couldn't add item to table. Here's why: %v", err)
		return nil, err
	} else {
		katlogger.Logger().Infof("Successfully updated role: %v", *roleObj.Rolename)
	}
	return ddb.GetRole(&accountId, &roleId)
}

func (db *DynamodbDbLayer) GetRole(accountId *string, roleId *string) (*openapi.Role, error) {

	roleObj := &openapi.Role{}

	tableName := db.settings.GetPerEnvTable(RolesTableName)
	response, err := db.dynamoDbClient.GetItem(context.TODO(), &dynamodb.GetItemInput{
		TableName: aws.String(tableName),
		Key: map[string]types.AttributeValue{
			"accountId": &types.AttributeValueMemberS{Value: *accountId},
			"roleId":    &types.AttributeValueMemberS{Value: *roleId},
		},
	})

	if err != nil {
		katlogger.Logger().Warnf("Couldn't get item from table. Here's why: %v", err)
	} else {
		if response.Item == nil {
			return nil, ErrRoleNotFound
		}
		err = attributevalue.UnmarshalMap(response.Item, &roleObj)
	}
	return roleObj, err
}

func (db *DynamodbDbLayer) GetRolesForAccount(accountId string) ([]openapi.Role, error) {
	var roles []openapi.Role

	keyCond := expression.Key("accountId").Equal(expression.Value(accountId))

	expr, err := expression.NewBuilder().
		WithKeyCondition(keyCond).
		Build()

	if err != nil {
		katlogger.Logger().Infof("Couldn't build expressions for query. Here's why: %v", err)
		return nil, err
	}

	tableName := db.settings.GetPerEnvTable(RolesTableName)

	response, err := db.dynamoDbClient.Query(context.TODO(), &dynamodb.QueryInput{
		TableName:                 aws.String(tableName),
		KeyConditionExpression:    expr.KeyCondition(),
		ExpressionAttributeNames:  expr.Names(),
		ExpressionAttributeValues: expr.Values(),
	})

	if err != nil {
		katlogger.Logger().Warnf("Couldn't scan for roles. Here's why: %v", err)
	} else {
		err = attributevalue.UnmarshalListOfMaps(response.Items, &roles)
		if err != nil {
			katlogger.Logger().Warnf("Couldn't unmarshal query response. Here's why: %v", err)
		}
	}

	return roles, err
}

func (ddb *DynamodbDbLayer) GetRolesForService(serviceId string, limit int) ([]openapi.Role, error) {
	var roles []openapi.Role

	filterExpr := expression.Key("serviceId").Equal(expression.Value(serviceId))

	expr, err := expression.NewBuilder().
		WithKeyCondition(filterExpr).
		Build()

	if err != nil {
		katlogger.Logger().Warnf("Couldn't build expression. Here's why: %v", err)
		return nil, err
	}

	tableName := ddb.settings.GetPerEnvTable(RolesTableName)
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
		katlogger.Logger().Warnf("Couldn't query for roles. Here's why: %v", err)
	} else {
		err = attributevalue.UnmarshalListOfMaps(response.Items, &roles)
		if err != nil {
			katlogger.Logger().Warnf("Couldn't unmarshal query response. Here's why: %v", err)
		}
	}

	return roles, err
}
