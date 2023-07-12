#!/bin/sh

if [[ -z "$1" ]]; then
  echo "usage: $0 <openapi-spec-file>"
  exit 1
fi

OPENAPI_SPEC_FILE=$1

cp $OPENAPI_SPEC_FILE katanemo-authorizer.yml

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:latest generate -i /local/katanemo-authorizer.yml -g python-nextgen -o /local/python-auth-sdk --skip-validate-spec --additional-properties=packageName=katanemo_auth,projectName=katanemo-python-auth-sdk --global-property skipFormModel=false

rm katanemo-authorizer.yml
