package paths

import (
	"fmt"
	"strings"

	"github.com/golang-jwt/jwt/v5"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib"
)

func (dev *AuthorizerCore) TagMatches(nameVals *[]NameValPair, claims jwt.MapClaims, serviceId string, path string,
	httpOperation string, isTagCheckEnforced bool, defaultServiceId string) bool {

	if len(*nameVals) == 0 {
		return true
	}
	developerId := fmt.Sprintf("%v", claims[common.TokenClaimAccountId])
	userId := fmt.Sprintf("%v", claims["sub"])
	tags, err := dev.GetTagsForResource(nameVals, claims, serviceId, path)
	if err != nil {
		return true
	}

	if len(tags) == 0 && serviceId != defaultServiceId {
		tags, err = dev.GetTagsForResource(nameVals, claims, defaultServiceId, path)
		if err != nil {
			return true
		}
	}

	// if there are no tags, then for root level APIs return true
	if len(tags) == 0 {
		src := strings.Split(path, "/")
		if len(src) == 1 {
			return true
		}
		return !isTagCheckEnforced
	}

	if owner, ok := tags[common.CreateByTag]; ok {
		if len(owner) != 1 {
			return false
		}
		if owner[0] == developerId {
			return true
		}
	}

	if assumeRole, ok := tags[common.AssumeRoleGetTag]; ok {
		principal := developerId + ":" + userId

		for _, a := range assumeRole {
			if a == principal {
				return true
			}
		}
	}
	resourceId := (*nameVals)[len(*nameVals)-1].Value
	resourceName := (*nameVals)[len(*nameVals)-1].Name

	return checkAccessTags(tags, developerId, httpOperation, resourceId, resourceName)
}

/*
constructing all possible combinations of access tags here
to lookup in the tags map. Refer here:
https://docs.google.com/document/d/1fWNJ8sk3xAZBWR8EoOL1E-zDcl5Qbic1RBYiKH9AcqA/edit#heading=h.xk969otw5egw
for details on access tags and their possible combinations.
*/
func checkAccessTags(tags map[string][]string, developerId, httpOperation, resourceId, resourceName string) bool {
	// user defined access tag format: access-tag:<http Operation>:<resourceName>:<resourceId>:principals
	// system defined access tag katanemo:access-tag:<http Operation>:<resourceName>:<resourceId>:principals
	tagAll := fmt.Sprintf("access-tag:*:*:%v:principals", resourceId)
	tagOp := fmt.Sprintf("access-tag:%v:*:%v:principals", httpOperation, resourceId)
	tagPath := fmt.Sprintf("access-tag:*:%v:%v:principals", resourceName, resourceId)
	tagOpPath := fmt.Sprintf("access-tag:%v:%v:%v:principals", httpOperation, resourceName, resourceId)

	allTags := []string{tagAll, tagOp, tagPath, tagOpPath}
	for _, tag := range allTags {
		// check user defined access tag
		allowed := checkAccessTag(tags, &tag, &developerId)
		if allowed {
			return allowed
		}
		// check system tag
		sysTag := "katanemo:" + tag
		allowed = checkAccessTag(tags, &sysTag, &developerId)
		if allowed {
			return allowed
		}
	}
	return false
}

func checkAccessTag(tags map[string][]string, tag, developerId *string) bool {
	val, ok := tags[*tag]
	if ok {
		for _, principal := range val {
			if principal == "*" || principal == *developerId {
				return true
			}
		}
	}
	return false
}

func (dev *AuthorizerCore) GetTagsForResource(nameVals *[]NameValPair, claims jwt.MapClaims, serviceId, path string) (map[string][]string, error) {
	developerId := fmt.Sprintf("%v", claims[common.TokenClaimAccountId])

	src := strings.Split(path, "/")
	if len(src) == 1 || len(*nameVals) == 0 {
		return nil, nil
	}

	tags, err := dev.authDataAccess.GetTags(serviceId, developerId, (*nameVals)[len(*nameVals)-1].Name, (*nameVals)[len(*nameVals)-1].Value)

	if err != nil || tags == nil {
		return nil, err
	}

	return tags.Tags, nil
}
