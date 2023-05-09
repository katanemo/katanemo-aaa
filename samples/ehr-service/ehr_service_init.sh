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

log getting token for ehr admin
log katutil login-with-password --service_id $KATANEMO_SERVICE_ID --email $EHR_ADMIN_EMAIL --password $EHR_ADMIN_PASSWORD
EHR_ADMIN_TOKEN=$($KATUTIL login-with-password --service_id $KATANEMO_SERVICE_ID --email $EHR_ADMIN_EMAIL --password $EHR_ADMIN_PASSWORD | jq -r .token)

log registering service with api spec $1 to katanemo
log katutil init-service --service_name 'patient records service' --api_spec $API_SPEC --redirect_uri www.google.com --print_output True --token XXXXX
EHR_SERVICE_ID=$($KATUTIL init-service --service_name 'patient records service' --api_spec $API_SPEC --redirect_uri www.google.com --print_output True --token $EHR_ADMIN_TOKEN | jq -r .serviceId)

echo EHR_SERVICE_ID=$EHR_SERVICE_ID > .ehr_service_details

log "=== patients record service initialized with katanemo $EHR_SERVICE_ID ==="
