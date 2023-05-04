#!/bin/sh
set -e
set -o errexit -o pipefail

. ./common.sh
. .ehr_admin_details

log '=== initializing service ==='

if [[ -z "$1" ]]; then
  echo "usage: $0 <path/to/api_spec>"
  exit 1
fi

# ensure that api spec file has full path
API_SPEC=`pwd`/$1

EHR_ADMIN_TOKEN=$(katutil login-with-password --service_id $KATANEMO_SERVICE_ID --email $EHR_ADMIN_EMAIL --password $EHR_ADMIN_PASSWORD | jq -r .token)
EHR_SERVICE_ID=$(katutil init-service --service_name 'patient records service' --api_spec $API_SPEC --redirect_uri www.google.com --token $EHR_ADMIN_TOKEN | jq -r .serviceId)
echo EHR_SERVICE_ID=$EHR_SERVICE_ID > .ehr_service_details

log "=== patients record service initialized with katanemo $EHR_SERVICE_ID ==="
