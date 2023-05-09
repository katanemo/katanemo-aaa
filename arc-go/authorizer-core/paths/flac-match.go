package paths

import (
	"encoding/json"
	"strings"
)

// FLAC matching algorithm
// 1. Expand all resource nested fields e.g. {"a": {"b": "c", "d": {"e":"f"}}} to ["a.b", "a.d.e"]
// 2. Every expanded resource field must match with a FLAC policy field. A resource fields matches with FLAC policy if any of two conditions are true
//       a. policy field exactly matches with resource field
//       b. if policy field has * star as suffix,then policy field (without *) should be prefix of resource expanded field e.g. cluster* matches with cluster.name, cluster.id, cluster.data.value

func expandResourceToFields(prefix string, resource map[string]interface{}) []string {
	res := []string{}
	for d, value := range resource {
		new_prefix := prefix
		if prefix != "" {
			new_prefix = prefix + "."
		}
		switch valType := value.(type) {
		case map[string]interface{}: // if type is a map
			res = append(res, expandResourceToFields(new_prefix+d, valType)...)
		case []interface{}: // if type is array
			for _, arrayElement := range value.([]interface{}) {
				switch y := arrayElement.(type) {
				case map[string]interface{}: // if element array is a map. Note: not handling nested array at the moment.
					res = append(res, expandResourceToFields(new_prefix+d, y)...)
				default:
					res = append(res, new_prefix+d)
				}
			}
		default:
			res = append(res, new_prefix+d)
		}
	}
	return res
}

func matchImpl(policyFields []string, expandedResourceFields []string) bool {
	for _, field := range expandedResourceFields {
		matched := false
		for _, policyField := range policyFields {
			if policyField == field {
				matched = true
				break
			}
			if strings.HasSuffix(policyField, "*") {
				temp := policyField[0 : len(policyField)-1] // remove *
				if strings.HasPrefix(field, temp) {
					matched = true
					break
				}
			}

		}
		if !matched {
			return false
		}
	}
	return true
}

func FLACMatch(rolePath string, resource *string) bool {
	if resource == nil || *resource == "" {
		return true // no resource object passed as input, it will be a match
	}

	// TODO: Currently we assume that if resource is passed then FLAC must be given
	// when we'll move to whole request object passed to authorizer then we have
	// to figure out how FLAC parameter is passed.
	rolePathParts := strings.Split(rolePath, ":")
	if len(rolePathParts) < 3 {
		return true // if no FLAC policy but resource is given, it will be not a match
	}

	resourceObj := map[string]interface{}{}

	err := json.Unmarshal([]byte(*resource), &resourceObj)
	if err != nil {
		return false
	}
	expandedResouceFields := expandResourceToFields("", resourceObj)

	flacFieldsStr := strings.ReplaceAll(rolePathParts[2], "[", "")
	flacFieldsStr = strings.ReplaceAll(flacFieldsStr, "]", "")
	flacFields := strings.Split(flacFieldsStr, ",")
	for i := range flacFields {
		flacFields[i] = strings.TrimSpace(flacFields[i])
	}

	return matchImpl(flacFields, expandedResouceFields)
}
