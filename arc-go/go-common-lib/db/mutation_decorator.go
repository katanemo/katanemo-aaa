package db

import (
	"fmt"

	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/core/openapi"
)

type mutationDecorator struct {
	db                  CoreDataAccess
	publishNotification func(topic string, message *common.Notification) error
}

func NewMutationNotificationDecorator(db CoreDataAccess, publishNotification func(topic string, message *common.Notification) error) CoreDataAccess {
	decorator := &mutationDecorator{
		db:                  db,
		publishNotification: publishNotification,
	}
	return decorator
}

// AddRole implements CoreDataAccess
func (d *mutationDecorator) AddRole(role *openapi.Role) (*openapi.Role, error) {
	addedRole, err := d.db.AddRole(role)
	if err != nil {
		return nil, err
	}

	notification := &common.Notification{
		HashKey:   *addedRole.AccountId,
		RangeKey:  *addedRole.RoleId,
		Version:   *addedRole.Version,
		UpdatedAt: *addedRole.UpdatedAt,
		Type:      common.RoleType,
	}

	err = d.publishNotification(*addedRole.ServiceId, notification)
	return addedRole, err
}

// AddTags implements CoreDataAccess
func (d *mutationDecorator) AddTags(tags *openapi.Tags) (*openapi.Tags, error) {
	newTag, err := d.db.AddTags(tags)
	if err != nil {
		return nil, err
	}

	notification := &common.Notification{
		HashKey:   fmt.Sprintf("%v_%v", newTag.ServiceId, newTag.Name),
		RangeKey:  newTag.ResourceId,
		Version:   *newTag.Version,
		UpdatedAt: *newTag.UpdatedAt,
		Type:      common.TagsType,
	}

	err = d.publishNotification(newTag.ServiceId, notification)

	return newTag, err
}

// UpdateTags implements CoreDataAccess
func (d *mutationDecorator) UpdateTags(tags *openapi.Tags) (*openapi.Tags, error) {
	updatedTags, err := d.db.UpdateTags(tags)
	if err != nil {
		return nil, err
	}

	notification := &common.Notification{
		HashKey:   fmt.Sprintf("%v_%v", updatedTags.ServiceId, updatedTags.Name),
		RangeKey:  updatedTags.ResourceId,
		Version:   *updatedTags.Version,
		UpdatedAt: *updatedTags.UpdatedAt,
		Type:      common.TagsType,
	}

	err = d.publishNotification(updatedTags.ServiceId, notification)

	return updatedTags, err
}

// UpdateRole implements CoreDataAccess
func (d *mutationDecorator) UpdateRole(accountId string, roleId string, roleObj *openapi.Role) (*openapi.Role, error) {
	updatedRole, err := d.db.UpdateRole(accountId, roleId, roleObj)
	if err != nil {
		return nil, err
	}

	notification := &common.Notification{
		HashKey:   *updatedRole.AccountId,
		RangeKey:  *updatedRole.RoleId,
		Version:   *updatedRole.Version,
		UpdatedAt: *updatedRole.UpdatedAt,
		Type:      common.RoleType,
	}

	err = d.publishNotification(*updatedRole.ServiceId, notification)
	return updatedRole, err
}

// UpdateService implements CoreDataAccess
func (d *mutationDecorator) UpdateService(apiservice *openapi.Service) (*openapi.Service, error) {
	updatedService, err := d.db.UpdateService(apiservice)
	if err != nil {
		return nil, err
	}

	notification := &common.Notification{
		HashKey:   *updatedService.AccountId,
		Version:   *updatedService.Version,
		UpdatedAt: *updatedService.UpdatedAt,
		Type:      common.ServiceType,
	}

	err = d.publishNotification(*updatedService.ServiceId, notification)
	return updatedService, err
}

// GetTagsForService implements CoreDataAccess
func (m *mutationDecorator) GetTagsForService(serviceId string, limit int) ([]openapi.Tags, error) {
	return m.db.GetTagsForService(serviceId, limit)
}

// GetRolesForService implements CoreDataAccess
func (d *mutationDecorator) GetRolesForService(serviceId string, limit int) ([]openapi.Role, error) {
	return d.db.GetRolesForService(serviceId, limit)
}

// GetRole implements CoreDataAccess
func (d *mutationDecorator) GetRole(accountId *string, roleId *string) (*openapi.Role, error) {
	return d.db.GetRole(accountId, roleId)
}

// GetService implements CoreDataAccess
func (d *mutationDecorator) GetService(serviceId string) (*openapi.Service, error) {
	return d.db.GetService(serviceId)
}

// GetTags implements CoreDataAccess
func (d *mutationDecorator) GetTags(serviceId string, accountId string, name string, resourceId string) (*openapi.Tags, error) {
	return d.db.GetTags(serviceId, accountId, name, resourceId)
}

// AddClientKeys implements CoreDataAccess
func (d *mutationDecorator) AddClientKeys(clientKeyObject *openapi.ClientKeyObject) error {
	return d.db.AddClientKeys(clientKeyObject)
}

// AddDeveloper implements CoreDataAccess
func (d *mutationDecorator) AddDeveloper(entity openapi.Developer) error {
	return d.db.AddDeveloper(entity)
}

// AddMetadata implements CoreDataAccess
func (d *mutationDecorator) AddMetadata(metadata *common.Metadata) error {
	return d.db.AddMetadata(metadata)
}

// AddOktaConnection implements CoreDataAccess
func (d *mutationDecorator) AddOktaConnection(oktaObj openapi.OktaObj) error {
	return d.db.AddOktaConnection(oktaObj)
}

// AddSAMLConnection implements CoreDataAccess
func (d *mutationDecorator) AddSAMLConnection(samlObj openapi.SAMLObj) error {
	return d.db.AddSAMLConnection(samlObj)
}

// AddService implements CoreDataAccess
func (d *mutationDecorator) AddService(apiservice *openapi.Service) (*openapi.Service, error) {
	addedService, err := d.db.AddService(apiservice)
	return addedService, err
}

// AddSubscription implements CoreDataAccess
func (d *mutationDecorator) AddSubscription(entity Subscription) error {
	return d.db.AddSubscription(entity)
}

// AddUser implements CoreDataAccess
func (d *mutationDecorator) AddUser(userObj openapi.User) error {
	return d.db.AddUser(userObj)
}

// AddUserConfirmation implements CoreDataAccess
func (d *mutationDecorator) AddUserConfirmation(confirmation *UserConfirmationInfo) error {
	return d.db.AddUserConfirmation(confirmation)
}

// DeleteClientKey implements CoreDataAccess
func (d *mutationDecorator) DeleteClientKey(accountId *string, clientId *string) (*openapi.ClientKeyObject, error) {
	return d.db.DeleteClientKey(accountId, clientId)
}

// GetClientKey implements CoreDataAccess
func (d *mutationDecorator) GetClientKey(accountId *string, clientKeyId *string) (*openapi.ClientKeyObject, error) {
	return d.db.GetClientKey(accountId, clientKeyId)
}

// GetClientKeyList implements CoreDataAccess
func (d *mutationDecorator) GetClientKeyList(accountId *string) ([]*openapi.ClientKeyObject, error) {
	return d.db.GetClientKeyList(accountId)
}

// GetDeveloper implements CoreDataAccess
func (d *mutationDecorator) GetDeveloper(accountId *string) (*openapi.Developer, error) {
	return d.db.GetDeveloper(accountId)
}

// GetDeveloperByServiceAndEmail implements CoreDataAccess
func (d *mutationDecorator) GetDeveloperByServiceAndEmail(serviceId string, email string) (*openapi.Developer, error) {
	return d.db.GetDeveloperByServiceAndEmail(serviceId, email)
}

// GetDeveloperByServiceId implements CoreDataAccess
func (d *mutationDecorator) GetDeveloperByServiceId(serviceId string) (*openapi.Developer, error) {
	return d.db.GetDeveloperByServiceId(serviceId)
}

// GetMetadata implements CoreDataAccess
func (d *mutationDecorator) GetMetadata(serviceName string) (*common.Metadata, error) {
	return d.db.GetMetadata(serviceName)
}

// GetOktaConnection implements CoreDataAccess
func (d *mutationDecorator) GetOktaConnection(connectionId string) (*openapi.OktaObj, error) {
	return d.db.GetOktaConnection(connectionId)
}

// GetOktaConnectionByClient implements CoreDataAccess
func (d *mutationDecorator) GetOktaConnectionByClient(clientId string) (*openapi.OktaObj, error) {
	return d.db.GetOktaConnectionByClient(clientId)
}

// GetOktaConnectionByState implements CoreDataAccess
func (d *mutationDecorator) GetOktaConnectionByState(state string) (*openapi.OktaObj, error) {
	return d.db.GetOktaConnectionByState(state)
}

// GetOktaConnectionsByAccount implements CoreDataAccess
func (d *mutationDecorator) GetOktaConnectionsByAccount(accountId string) ([]openapi.OktaObj, error) {
	return d.db.GetOktaConnectionsByAccount(accountId)
}

// GetRolesForAccount implements CoreDataAccess
func (d *mutationDecorator) GetRolesForAccount(accountId string) ([]openapi.Role, error) {
	return d.db.GetRolesForAccount(accountId)
}

// GetSAMLConnection implements CoreDataAccess
func (d *mutationDecorator) GetSAMLConnection(connectionId string) (*openapi.SAMLObj, error) {
	return d.db.GetSAMLConnection(connectionId)
}

// GetSAMLConnectionByDevService implements CoreDataAccess
func (d *mutationDecorator) GetSAMLConnectionByDevService(accountId *string, serviceId *string) ([]openapi.SAMLObj, error) {
	return d.db.GetSAMLConnectionByDevService(accountId, serviceId)
}

// GetSubscriptionsForDeveloper implements CoreDataAccess
func (d *mutationDecorator) GetSubscriptionsForDeveloper(accountId string) (*[]Subscription, error) {
	return d.db.GetSubscriptionsForDeveloper(accountId)
}

// GetUser implements CoreDataAccess
func (d *mutationDecorator) GetUser(accountId string, userId string) (*openapi.User, error) {
	return d.db.GetUser(accountId, userId)
}

// GetUserConfirmation implements CoreDataAccess
func (d *mutationDecorator) GetUserConfirmation(confirmationCode string) (*UserConfirmationInfo, error) {
	return d.db.GetUserConfirmation(confirmationCode)
}

// GetUsersByAccountId implements CoreDataAccess
func (d *mutationDecorator) GetUsersByAccountId(accountId string) (*[]openapi.User, error) {
	return d.db.GetUsersByAccountId(accountId)
}

// UpdateDeveloper implements CoreDataAccess
func (d *mutationDecorator) UpdateDeveloper(entity openapi.Developer) error {
	return d.db.UpdateDeveloper(entity)
}

// UpdateMetadata implements CoreDataAccess
func (d *mutationDecorator) UpdateMetadata(metadata *common.Metadata) error {
	return d.db.UpdateMetadata(metadata)
}

func (d *mutationDecorator) GetUserByServiceIdAndUserId(serviceId, userId string) (*openapi.User, error) {
	return d.db.GetUserByServiceIdAndUserId(serviceId, userId)
}
