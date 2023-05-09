package db

import (
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/core/openapi"
)

type Subscription struct {
	AccountId    string `dynamodbav:"accountId"`
	SubscriberId string `dynamodbav:"subscriberId"`
	ServiceId    string `dynamodbav:"serviceId"`
}

type UserConfirmationInfo struct {
	ConfirmationCode string `dynamodbav:"confirmationCode"`
	AccountId        string `dynamodbav:"accountId"`
	UserId           string `dynamodbav:"userId"`
}

type ArcDataAccess interface {
	GetRolesForService(serviceId string, limit int) ([]openapi.Role, error)
	GetTagsForService(serviceId string, limit int) ([]openapi.Tags, error)
}

type CoreDataAccess interface {
	AuthDataAccess
	ArcDataAccess
	AddClientKeys(clientKeyObject *openapi.ClientKeyObject) error
	AddDeveloper(entity openapi.Developer) error
	UpdateDeveloper(entity openapi.Developer) error
	AddOktaConnection(oktaObj openapi.OktaObj) error
	AddRole(role *openapi.Role) (*openapi.Role, error)
	AddSAMLConnection(samlObj openapi.SAMLObj) error
	AddService(apiservice *openapi.Service) (*openapi.Service, error)
	UpdateService(apiservice *openapi.Service) (*openapi.Service, error)
	AddSubscription(entity Subscription) error
	AddTags(tags *openapi.Tags) (*openapi.Tags, error)
	AddUser(userObj openapi.User) error
	DeleteClientKey(accountId, clientId *string) (*openapi.ClientKeyObject, error)
	GetClientKey(accountId *string, clientKeyId *string) (*openapi.ClientKeyObject, error)
	GetClientKeyList(accountId *string) ([]*openapi.ClientKeyObject, error)
	GetDeveloper(accountId *string) (*openapi.Developer, error)
	GetDeveloperByServiceAndEmail(serviceId, email string) (*openapi.Developer, error)
	GetDeveloperByServiceId(serviceId string) (*openapi.Developer, error)
	GetOktaConnection(connectionId string) (*openapi.OktaObj, error)
	GetOktaConnectionByClient(clientId string) (*openapi.OktaObj, error)
	GetOktaConnectionByState(state string) (*openapi.OktaObj, error)
	GetOktaConnectionsByAccount(accountId string) ([]openapi.OktaObj, error)
	GetRolesForAccount(accountId string) ([]openapi.Role, error)
	GetSAMLConnection(connectionId string) (*openapi.SAMLObj, error)
	GetSAMLConnectionByDevService(accountId, serviceId *string) ([]openapi.SAMLObj, error)
	GetSubscriptionsForDeveloper(accountId string) (*[]Subscription, error)
	GetUser(accountId string, userId string) (*openapi.User, error)
	GetUsersByAccountId(accountId string) (*[]openapi.User, error)
	AddUserConfirmation(confirmation *UserConfirmationInfo) error
	GetUserConfirmation(confirmationCode string) (*UserConfirmationInfo, error)
	AddMetadata(metadata *common.Metadata) error
	UpdateMetadata(metadata *common.Metadata) error
	GetMetadata(serviceName string) (*common.Metadata, error)
	UpdateRole(accountId, roleId string, roleObj *openapi.Role) (*openapi.Role, error)
	UpdateTags(tags *openapi.Tags) (*openapi.Tags, error)
	GetUserByServiceIdAndUserId(serviceId, userId string) (*openapi.User, error)
}
