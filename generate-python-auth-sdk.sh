#!/bin/sh

if [[ -z "$1" ]]; then
  echo "usage: $0 <openapi-spec-file>"
  exit 1
fi

OPENAPI_SPEC_FILE=$1

cp $OPENAPI_SPEC_FILE katanemo-authorizer.yml

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:latest generate -i /local/openapi_spec.yaml -g python-nextgen -o /local/python-sdk --skip-validate-spec --additional-properties=packageName=katanemo_sdk,projectName=katanemo-python-sdk --global-property skipFormModel=false

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:latest generate -i /local/katanemo-authorizer.yml -g python-nextgen -o /local/python-auth-sdk --skip-validate-spec --additional-properties=packageName=katanemo_auth_sdk,projectName=katanemo-python-auth-sdk --global-property skipFormModel=false

rm katanemo-authorizer.yml
