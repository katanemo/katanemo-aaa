#!/bin/sh

if [[ -z "$1" ]]; then
  echo "usage: $0 <openapi-spec-file>"
  exit 1
fi

OPENAPI_SPEC_FILE=$1

cp $OPENAPI_SPEC_FILE openapi_spec.yaml

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:latest generate -i /local/openapi_spec.yaml -g python-nextgen -o /local/python-sdk --skip-validate-spec --additional-properties=packageName=katanemo_sdk,projectName=katanemo-python-sdk --global-property skipFormModel=false

rm openapi_spec.yaml
