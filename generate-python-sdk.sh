#!/bin/sh

if [[ -z "$1" ]]; then
  echo "usage: $0 <openapi-spec-file>"
  exit 1
fi

OPENAPI_SPEC_FILE=$1

cp $OPENAPI_SPEC_FILE openapi_spec.yaml

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:latest-release generate -i /local/openapi_spec.yaml -g python -o /local/python-sdk --skip-validate-spec --additional-properties=packageName=katanemo_sdk,projectName=katanemo-python-sdk

rm openapi_spec.yaml
