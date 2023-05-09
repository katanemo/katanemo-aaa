package db

import (
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/core/openapi"
)

// test
type AuthDataAccess interface {
	GetRole(accountId *string, roleId *string) (*openapi.Role, error)
	GetService(serviceId string) (*openapi.Service, error)
	GetTags(serviceId, accountId, name, resourceId string) (*openapi.Tags, error)
}
