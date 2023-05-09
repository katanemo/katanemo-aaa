package paths

import (
	"encoding/json"
	"fmt"
	"net/http"
	"reflect"
	"strings"

	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib"

	"github.com/golang-jwt/jwt/v5"
	authzparser "github.com/katanemo/katanemo-aaa/arc-go/authorizer-core/pkg/antlr"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/auditlogger"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/db"
	katlogger "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/logger"

	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/auth/openapi"
	core_openapi "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/core/openapi"
	"github.com/labstack/echo/v4"
)

type NameValPair struct {
	Name  string `json:"name"`
	Value string `json:"value"`
}

type ValidateToken func(token string) (jwt.MapClaims, error)

type AuthorizerCore struct {
	authDataAccess            db.AuthDataAccess
	validateTokenAndGetClaims ValidateToken
}

func NewAuthCore(authDataAccess db.AuthDataAccess, validateToken ValidateToken) *AuthorizerCore {

	return &AuthorizerCore{
		authDataAccess:            authDataAccess,
		validateTokenAndGetClaims: validateToken,
	}
}

func (dev *AuthorizerCore) getRolesInClaim(claims jwt.MapClaims) ([]*core_openapi.Role, error) {
	var roles []*core_openapi.Role
	accountId, ok := claims[common.TokenClaimAccountId].(string)
	if !ok {
		return nil, fmt.Errorf("invalid accountId type received in claims: %v", reflect.TypeOf(claims[common.TokenClaimAccountId]).Kind())
	}
	if reflect.TypeOf(claims["scp"]).Kind() == reflect.Slice {
		roleIds := reflect.ValueOf(claims["scp"])
		for i := 0; i < roleIds.Len(); i++ {
			roleId := fmt.Sprintf("%v", roleIds.Index(i))
			role, err := dev.authDataAccess.GetRole(&accountId, &roleId)
			if err != nil {
				return roles, err
			}
			roles = append(roles, role)
		}
	}
	return roles, nil
}

func (dev *AuthorizerCore) evaluateWhereClause(nameVals *[]NameValPair,
	claims jwt.MapClaims, serviceId, path, whereClause string, reqObj map[string]interface{}) (bool, error) {

	tags, err := dev.GetTagsForResource(nameVals, claims, serviceId, path)
	if err != nil {
		return false, err
	}

	return authzparser.Evaluate(whereClause, tags, claims, reqObj)
}

func (dev *AuthorizerCore) roleMatches(claims jwt.MapClaims, serviceId string,
	role *core_openapi.Role, path string,
	httpOperation string, reqObj map[string]interface{},
	defaultServiceId string) (*[]NameValPair, string, bool) {
	// TODO: src should be done at roles level for efficiency reasons
	// shouldn't do this split for each role
	src := strings.Split(path, "/")
	var nameVals []NameValPair

	for _, policy := range *role.Policies {
		allowList := *policy.Allow
		if len(allowList) > 0 && allowList[0] == "*" {
			service, err := dev.authDataAccess.GetService(serviceId)
			if err != nil {
				continue
			}
			allowList = *service.Apis
			// if it is a subscriber operating, we need to pull paths for Katanemo service as well
			if defaultServiceId != "" {
				defServ, err := dev.authDataAccess.GetService(defaultServiceId)
				if err != nil {
					continue
				}
				allowList = append(allowList, *defServ.Apis...)
			}
		}
		for _, p := range allowList {
			nameVals = nil
			temp := strings.Split(p, ":")
			rolePath := temp[1]
			roleOperation := temp[0]
			// TODO: add a check here that temp has only two values
			// assumption is that : can't be in relative path
			dst := strings.Split(rolePath, "/")
			if len(src) != len(dst) {
				continue
			}

			pathMatched := true
			for i, srcPart := range src {
				dstPart := dst[i]

				if strings.HasPrefix(dstPart, "{") && strings.HasSuffix(dstPart, "}") {
					name := dstPart[1 : len(dstPart)-1]
					nameVals = append(nameVals, NameValPair{Name: name, Value: srcPart})
					continue
				}

				if srcPart != dstPart {
					pathMatched = false
					break
				}
			}
			if pathMatched && roleOperation == httpOperation {
				if policy.Where != nil {
					res, err := dev.evaluateWhereClause(&nameVals, claims, serviceId, path, *policy.Where, reqObj)
					if err != nil || !res {
						continue
					}
				}
				return &nameVals, p, true
			}
		}
	}
	return nil, "", false
}

func (dev *AuthorizerCore) AuthorizeRequestImpl(authObj *openapi.AuthorizationRequest) (int, error) {
	katlogger.Logger().Infof("Authorizing request: method: %v, path: %v", authObj.HttpMethod, authObj.Path)

	claims, err := dev.validateTokenAndGetClaims(authObj.Token)

	if err != nil {
		return 0, fmt.Errorf("token validation failed for token. error: %w", err)
	}

	serviceId := fmt.Sprintf("%v", claims[common.TokenClaimServiceId])
	serviceObj, err := dev.authDataAccess.GetService(serviceId)
	if err != nil {
		return 0, fmt.Errorf("get service failed. error: %w", err)
	}

	roles, err := dev.getRolesInClaim(claims)
	if err != nil {
		return 0, fmt.Errorf("get roles failed. error: %w", err)
	}

	resourceObj := map[string]interface{}{}
	if authObj.RequestBody != nil {
		err := json.Unmarshal([]byte(*authObj.RequestBody), &resourceObj)
		if err != nil {
			return 0, fmt.Errorf("unable to parse json object: %w", err)
		}
	}
	defaultServiceId := ""
	// See if it is a subscriber token ... if so we need to get default service id as well
	val, ok := claims[common.KatanemoDefaultServiceId]
	if ok {
		defaultServiceId = fmt.Sprintf("%v", val)
	}

	accountId := ""
	if serviceObj == nil || serviceObj.AccountId == nil {
		katlogger.Logger().Warn("Service object is nil or account id is nil")
	} else {
		accountId = *serviceObj.AccountId
	}

	audit := auditlogger.AuditLogEntry{
		Version: common.AuditLogsEntryVersion,
		AuditLogEntry: openapi.AuditLogEntry{
			Operation: authObj.HttpMethod,
			Path:      authObj.Path,
			ServiceId: serviceId,
			Principal: fmt.Sprintf("%v", claims[common.TokenClaimSubject]),
			AccountId: accountId,
		},
	}
	// policy, authentication result will be populated to audi entry during matching process.
	defer auditlogger.AuditLog(&audit)

	for _, role := range roles {
		nameVals, rolePath, isMatch := dev.roleMatches(claims, serviceId, role, authObj.Path, authObj.HttpMethod, resourceObj, defaultServiceId)
		if isMatch {
			// skip tag check when creating resources
			katlogger.Logger().Infof("Path matched. RoleId: %s, RolePath: %s, path: %s:%s", *role.RoleId, rolePath, authObj.HttpMethod, authObj.Path)
			if authObj.HttpMethod == "POST" {
				audit.AuthorizationCode = http.StatusOK
				return http.StatusOK, nil
			}
			tagEnforced := isTagCheckEnforced(serviceObj)
			tagMatches := dev.TagMatches(nameVals, claims, serviceId, authObj.Path, authObj.HttpMethod, tagEnforced, defaultServiceId)

			if tagMatches {
				if FLACMatch(rolePath, authObj.RequestBody) {

					audit.AuthorizationCode = http.StatusOK
					return http.StatusOK, nil
				}
			}
		}
	}

	audit.AuthorizationCode = http.StatusForbidden
	return http.StatusForbidden, nil
}

func (dev *AuthorizerCore) AuthorizeRequest(ctx echo.Context) (int, error) {

	authObj := &openapi.AuthorizationRequest{}
	if err := ctx.Bind(&authObj); err != nil {
		return 0, fmt.Errorf("couldn't bind requst to auth object. error: %w", err)
	}

	return dev.AuthorizeRequestImpl(authObj)
}

// utility function to check if access tags are enforced or not
// for katanemo servie access tags are enforced.

// TODO: Add ability to enforce access tags to our customers.
func isTagCheckEnforced(serviceObject *core_openapi.Service) bool {
	return *serviceObject.Servicename == common.KatanemoServiceName
}
