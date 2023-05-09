package dynamo

import (
	"context"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/db"
	ddb "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/db"
	katlogger "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/logger"
)

func (db *DynamodbDbLayer) AddUserConfirmation(confirmationObj *ddb.UserConfirmationInfo) error {

	item, err := attributevalue.MarshalMap(confirmationObj)

	if err != nil {
		panic(err)
	}
	tableName := db.settings.GetPerEnvTable(UsersConfirmationTableName)
	_, err = db.dynamoDbClient.PutItem(context.TODO(), &dynamodb.PutItemInput{
		TableName: aws.String(tableName), Item: item,
	})
	if err != nil {
		katlogger.Logger().Warnf("Couldn't add item to table. Here's why: %v", err)
	} else {
		katlogger.Logger().Infof("Successfully added User: %v", confirmationObj.UserId)
	}
	return err
}

func (db *DynamodbDbLayer) GetUserConfirmation(confirmationCode string) (*db.UserConfirmationInfo, error) {
	confirmUserInfo := &ddb.UserConfirmationInfo{}

	tableName := db.settings.GetPerEnvTable(UsersConfirmationTableName)
	response, err := db.dynamoDbClient.GetItem(context.TODO(), &dynamodb.GetItemInput{
		TableName: aws.String(tableName),
		Key: map[string]types.AttributeValue{
			"confirmationCode": &types.AttributeValueMemberS{Value: confirmationCode},
		},
	})

	if err != nil {
		katlogger.Logger().Warnf("Couldn't get item from table. Here's why: %v", err)
	} else {
		err = attributevalue.UnmarshalMap(response.Item, &confirmUserInfo)
	}
	return confirmUserInfo, err
}
