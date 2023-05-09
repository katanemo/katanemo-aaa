package utils

import (
	"bytes"
	"context"
	"encoding/json"
	"time"

	"github.com/MicahParks/keyfunc/v2"
	"github.com/allegro/bigcache/v3"

	"github.com/katanemo/katanemo-aaa/arc-go/arc/config"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/api/openapi"
)

type CacheManager struct {
	rolesCache    *bigcache.BigCache
	tagsCache     *bigcache.BigCache
	serviceId     string
	updateManager *UpdateManager
	jwks          *keyfunc.JWKS
}

func NewCacheManager(settings *config.Settings) (*CacheManager, error) {

	rolesCache, err := bigcache.New(context.Background(), bigcache.DefaultConfig(10*time.Minute))
	if err != nil {
		return nil, err
	}
	tagsCache, err := bigcache.New(context.Background(), bigcache.DefaultConfig(10*time.Minute))
	if err != nil {
		return nil, err
	}
	cacheManager := &CacheManager{
		rolesCache: rolesCache,
		tagsCache:  tagsCache,
		serviceId:  settings.ServiceId,
		jwks:       nil,
	}
	updateManager := NewUpdateManager(cacheManager, settings)
	err = updateManager.BootstrapCache()
	if err != nil {
		return nil, err
	}
	cacheManager.updateManager = updateManager
	return cacheManager, nil
}

func (cm *CacheManager) GetPublicKey() *keyfunc.JWKS {
	if cm.jwks == nil {
		cm.updateManager.SetJwks()
	}
	return cm.jwks
}

func (cm *CacheManager) SetPublicKey(publicKey *keyfunc.JWKS) {
	cm.jwks = publicKey
}

func (cm *CacheManager) PutRole(role openapi.Role) error {
	reqBodyBytes := new(bytes.Buffer)
	err := json.NewEncoder(reqBodyBytes).Encode(role)
	if err != nil {
		return err
	}
	err = cm.rolesCache.Set(*role.RoleId, reqBodyBytes.Bytes())
	return err
}

func (cm *CacheManager) GetRole(accountId, roleId string) (*openapi.Role, error) {
	if entry, err := cm.rolesCache.Get(roleId); err == nil {
		var role openapi.Role
		err := json.Unmarshal(entry, &role)
		if err != nil {
			return nil, err
		}
		return &role, nil
	}

	role, err := cm.updateManager.GetRole(accountId, roleId)
	if err != nil {
		return nil, err
	}

	if role != nil {
		err := cm.PutRole(*role)
		if err != nil {
			return nil, err
		}
		return role, nil
	}
	return nil, nil

}

func (cm *CacheManager) PutTags(tags openapi.Tags) error {
	if tags.ServiceIdPath == nil {
		return nil
	}
	reqBodyBytes := new(bytes.Buffer)
	err := json.NewEncoder(reqBodyBytes).Encode(tags)
	if err != nil {
		return err
	}
	key := *tags.ServiceIdPath + "_" + tags.ResourceId
	err = cm.rolesCache.Set(key, reqBodyBytes.Bytes())
	return err
}

func (cm *CacheManager) GetTags(serviceId, accountId, name, resourceId string) (*openapi.Tags, error) {
	serviceIdPath := serviceId + "_" + name
	if entry, err := cm.rolesCache.Get(serviceIdPath + "_" + resourceId); err == nil {
		var tags openapi.Tags
		err := json.Unmarshal(entry, &tags)
		if err != nil {
			return nil, err
		}
		return &tags, nil
	}

	tags, err := cm.updateManager.GetTags(serviceId, accountId, name, resourceId)
	if err != nil {
		return nil, err
	}
	if tags != nil {
		err := cm.PutTags(*tags)
		if err != nil {
			return nil, err
		}
		return tags, nil
	}

	return nil, nil
}

func (cm *CacheManager) GetService(serviceId string) (*openapi.ServiceResponseObj, error) {
	return cm.updateManager.GetService(serviceId)
}
