package utils

import (
	"context"
	"fmt"
	"log"
	"net/http"

	"github.com/MicahParks/keyfunc/v2"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/katanemo/katanemo-aaa/arc-go/arc/config"
	openapi_api "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/api/openapi"
	"github.com/labstack/echo"
)

type UpdateManager struct {
	cacheManager *CacheManager
	serviceId    string
	bearerToken  string
	core         *openapi_api.ClientWithResponses
	apiEndpoint  string
}

func NewUpdateManager(cacheMgr *CacheManager, settings *config.Settings) *UpdateManager {
	core, err := openapi_api.NewClientWithResponses(settings.ApiEndpoint)
	if err != nil {
		panic(err)
	}

	resp, err := core.GetOAuthTokenWithResponse(context.Background(), settings.AccountId, openapi_api.GetOAuthTokenJSONRequestBody{
		ClientId:     aws.String(settings.ClientKey),
		ClientSecret: aws.String(settings.ClientSecret),
	})
	if err != nil {
		panic(err)
	}
	token := resp.JSON200.AccessToken

	// todo: spin up background thread to refresh token
	// TODO: Machine key to token exchange happens here

	return &UpdateManager{
		cacheManager: cacheMgr,
		serviceId:    settings.ServiceId,
		bearerToken:  *token,
		core:         core,
		apiEndpoint:  settings.ApiEndpoint,
	}
}

func (um *UpdateManager) SetJwks() {
	jwksURL := fmt.Sprintf("%s/service/%s/.well-known/jwks.json", um.apiEndpoint, um.serviceId)

	// Create the keyfunc options. Use an error handler that logs. Refresh the JWKS when a JWT signed by an unknown KID
	// is found or at the specified interval. Rate limit these refreshes. Timeout the initial JWKS refresh request after
	// 10 seconds. This timeout is also used to create the initial context.Context for keyfunc.Get.
	options := keyfunc.Options{
		RefreshUnknownKID: true,
	}

	// Create the JWKS from the resource at the given URL.
	jwks, err := keyfunc.Get(jwksURL, options)

	if err != nil {
		log.Fatalf("Failed to create JWKS from resource at the given URL.\nError: %s", err.Error())
	}
	um.cacheManager.SetPublicKey(jwks)
}

func createAttachAuthHeader(token string) openapi_api.RequestEditorFn {
	return func(ctx context.Context, req *http.Request) error {
		req.Header.Add(echo.HeaderAuthorization, fmt.Sprintf("Bearer %v", token))
		return nil
	}
}

func (um *UpdateManager) GetTags(serviceId, accountId, name, resourceId string) (*openapi_api.Tags, error) {
	resp, err := um.core.GetTagsForResourceWithResponse(context.Background(), accountId, serviceId, name,
		resourceId, createAttachAuthHeader(um.bearerToken))

	if err != nil {
		panic(err)
	}

	tags := resp.JSON200
	return tags, nil

}

func (um *UpdateManager) GetRole(accountId, roleId string) (*openapi_api.Role, error) {
	resp, err := um.core.GetRoleWithResponse(context.Background(), accountId, roleId, createAttachAuthHeader(um.bearerToken))
	if err != nil {
		panic(err)
	}
	return resp.JSON200, nil

}

func (um *UpdateManager) GetService(serviceId string) (*openapi_api.ServiceResponseObj, error) {
	resp, err := um.core.GetServiceWithResponse(context.Background(), serviceId, createAttachAuthHeader(um.bearerToken))
	if err != nil {
		panic(err)
	}
	return resp.JSON200, nil
}

func (um *UpdateManager) BootstrapCache() error {
	params := openapi_api.GetRolesForServiceParams{
		Limit: aws.Int(500),
	}
	resp, err := um.core.GetRolesForServiceWithResponse(context.Background(), um.serviceId, &params, createAttachAuthHeader(um.bearerToken))
	if err != nil {
		panic(err)
	}
	for _, role := range *resp.JSON200 {
		e := um.cacheManager.PutRole(role)
		if e != nil {
			panic(e)
		}
	}
	tagParams := openapi_api.GetTagsForServiceParams{
		Limit: aws.Int(500),
	}
	tagsResp, err := um.core.GetTagsForServiceWithResponse(context.Background(), um.serviceId, &tagParams, createAttachAuthHeader(um.bearerToken))
	if err != nil {
		panic(err)
	}

	for _, tag := range *tagsResp.JSON200 {
		err := um.cacheManager.PutTags(tag)
		if err != nil {
			panic(err)
		}
	}
	return nil
}
