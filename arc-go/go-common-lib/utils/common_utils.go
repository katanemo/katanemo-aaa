package utils

import (
	"encoding/json"
	"fmt"
	"strings"

	api_openapi "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/api/openapi"
	core_openapi "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/core/openapi"
	"gopkg.in/yaml.v2"
)

type Policy struct {
	Allow []string `json:"allow" yaml:"allow"`
	Where string   `json:"where,omitempty" yaml:"where,omitempty"`
}

type PolicyContent struct {
	Version int      `json:"version" yaml:"version"`
	Type    string   `json:"type" yaml:"type"`
	Policy  []Policy `json:"policy" yaml:"policy"`
}

func ApiRoleToCoreRole(roleObj *api_openapi.Role) (*core_openapi.Role, error) {
	policyData, err := unmarshalPolicyContent(&roleObj.Policy.PolicyContent)
	if err != nil {
		return nil, fmt.Errorf("Invalid policy content %s", roleObj.Policy.PolicyContent)
	}

	if len(policyData.Policy) < 1 {
		return nil, fmt.Errorf("Invalid policy content %s", roleObj.Policy.PolicyContent)
	}

	coreRoleObj := &core_openapi.Role{
		AccountId:     roleObj.AccountId,
		CreatedAt:     roleObj.CreatedAt,
		Policies:      nil,
		PolicyContent: &roleObj.Policy.PolicyContent,
		PolicyType:    &policyData.Type,
		PolicyVersion: &policyData.Version,
		RoleId:        roleObj.RoleId,
		Rolename:      roleObj.Rolename,
		ServiceId:     roleObj.ServiceId,
		UpdatedAt:     roleObj.UpdatedAt,
		Version:       roleObj.Version,
	}
	corePolicies := make([]core_openapi.Policy, len(policyData.Policy))
	for i := range policyData.Policy {
		corePolicies[i].Allow = &policyData.Policy[i].Allow
		if len(strings.TrimSpace(policyData.Policy[i].Where)) > 0 {
			corePolicies[i].Where = &policyData.Policy[i].Where
		}
	}
	coreRoleObj.Policies = &corePolicies

	return coreRoleObj, nil
}

func CoreRoleToApiRole(roleObj *core_openapi.Role) (*api_openapi.Role, error) {
	apiRoleObj := &api_openapi.Role{
		AccountId: roleObj.AccountId,
		CreatedAt: roleObj.CreatedAt,
		Policy: &api_openapi.Policy{
			PolicyContent: *roleObj.PolicyContent,
		},
		RoleId:    roleObj.RoleId,
		Rolename:  roleObj.Rolename,
		ServiceId: roleObj.ServiceId,
		UpdatedAt: roleObj.UpdatedAt,
		Version:   roleObj.Version,
	}

	return apiRoleObj, nil
}

func unmarshalPolicyContent(policyStr *string) (*PolicyContent, error) {
	var policyContent PolicyContent

	// TODO: it may be good idea to check the first non-white space character for {
	// to determine more efficiently if this is a json object.
	// Try to unmarshal the input as JSON
	if err := json.Unmarshal([]byte(*policyStr), &policyContent); err == nil {
		return &policyContent, nil
	}

	// If unmarshaling as JSON fails, try unmarshaling as YAML
	if err := yaml.Unmarshal([]byte(*policyStr), &policyContent); err == nil {
		return &policyContent, nil
	}

	return nil, fmt.Errorf("failed to unmarshal input as either JSON or YAML")
}
