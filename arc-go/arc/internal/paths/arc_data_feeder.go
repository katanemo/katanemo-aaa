package paths

import (
	"github.com/MicahParks/keyfunc/v2"
	"github.com/katanemo/katanemo-aaa/arc-go/arc/config"
	utils "github.com/katanemo/katanemo-aaa/arc-go/arc/internal/utils"

	katlogger "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/logger"
	core "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/core/openapi"
	common_utils "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/utils"
)

type ArcDataFeeder struct {
	cacheManager *utils.CacheManager
}

func NewArcDataFeeder(settings *config.Settings) *ArcDataFeeder {
	cacheManager, err := utils.NewCacheManager(settings)
	if err != nil {
		katlogger.Logger().Fatalf("failed to create cache manager. Error: %v", err)
		return nil
	}
	return &ArcDataFeeder{
		cacheManager: cacheManager,
	}
}

func (arcFeeder *ArcDataFeeder) GetPublicKey() *keyfunc.JWKS {
	return arcFeeder.cacheManager.GetPublicKey()
}

func (arcFeeder *ArcDataFeeder) GetRole(accountId, roleId *string) (*core.Role, error) {
	role, err := arcFeeder.cacheManager.GetRole(*accountId, *roleId)

	if err != nil {
		return nil, err
	}

	coreRoleObj, err := common_utils.ApiRoleToCoreRole(role)
	if err != nil {
		return nil, err
	}

	return coreRoleObj, nil
}

func (arcFeeder *ArcDataFeeder) GetService(serviceId string) (*core.Service, error) {
	service, err := arcFeeder.cacheManager.GetService(serviceId)
	if err != nil {
		return nil, err
	}
	return &core.Service{
		AccountId:   service.AccountId,
		Apis:        &service.Apis,
		ServiceId:   &service.ServiceId,
		Servicename: &service.ServiceName,
	}, nil

}

func (arcFeeder *ArcDataFeeder) GetTags(serviceId, accountId, name, resourceId string) (*core.Tags, error) {
	tags, err := arcFeeder.cacheManager.GetTags(serviceId, accountId, name, resourceId)

	if err != nil || tags == nil {
		return nil, err
	}
	return &core.Tags{
		AccountId:     tags.AccountId,
		Name:          tags.Name,
		ResourceId:    tags.ResourceId,
		ServiceId:     tags.ServiceId,
		Tags:          tags.Tags,
		ServiceIdPath: tags.ServiceIdPath,
	}, nil
}
