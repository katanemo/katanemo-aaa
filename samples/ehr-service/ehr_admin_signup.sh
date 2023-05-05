#!/bin/sh
set -e -o errexit -o pipefail

. ./common.sh

log '=== signing up ehr admin to katanemo ==='

if [[ -z "$1" ]]; then
  echo "usage: $0 <ehr_admin_email>"
  exit 1
fi

EHR_ADMIN_EMAIL=$1

# katutil signup-service --service_id $KATANEMO_SERVICE_ID --email $EHR_ADMIN_EMAIL | jq -r .accountId

# signup ehr admin
log katutil signup-service --service_id $KATANEMO_SERVICE_ID --email $EHR_ADMIN_EMAIL
EHR_ADMIN_ACCOUNT_ID=$(katutil signup-service --service_id $KATANEMO_SERVICE_ID --email $EHR_ADMIN_EMAIL | jq -r .accountId)

log enter code sent to $EHR_ADMIN_EMAIL
read CODE

# confirm and set its password
log katutil confirm-and-set-password --code $CODE --service_id $KATANEMO_SERVICE_ID --account_id $EHR_ADMIN_ACCOUNT_ID --email $EHR_ADMIN_EMAIL --password xxxx
katutil confirm-and-set-password --code $CODE --service_id $KATANEMO_SERVICE_ID --account_id $EHR_ADMIN_ACCOUNT_ID --email $EHR_ADMIN_EMAIL --password $EHR_ADMIN_PASSWORD

# create client keys to interact with katanemo api
EHR_ADMIN_TOKEN=$(katutil login-with-password --service_id $KATANEMO_SERVICE_ID --email $EHR_ADMIN_EMAIL --password $EHR_ADMIN_PASSWORD | jq -r .token)
EHR_ADMIN_ROLE_ID=`katutil get-roles --account_id $EHR_ADMIN_ACCOUNT_ID --token $EHR_ADMIN_TOKEN | jq -r '.[] | select(.rolename | test("admin") ) | .roleId'`
EHR_CLIENT_KEY=`katutil create-client-key --account_id $EHR_ADMIN_ACCOUNT_ID --client_name 'ehr client key' --role_id $EHR_ADMIN_ROLE_ID --token $EHR_ADMIN_TOKEN`

EHR_CLIENT_ID=$(echo $EHR_CLIENT_KEY | jq -r .clientId)
EHR_CLIENT_SECRET=$(echo $EHR_CLIENT_KEY | jq -r .clientSecret)

echo EHR_ADMIN_ACCOUNT_ID=$EHR_ADMIN_ACCOUNT_ID > .ehr_admin_details
echo EHR_ADMIN_EMAIL=$EHR_ADMIN_EMAIL >> .ehr_admin_details
echo EHR_ADMIN_PASSWORD=$EHR_ADMIN_PASSWORD >> .ehr_admin_details
echo EHR_CLIENT_ID=$EHR_CLIENT_ID >> .ehr_admin_details
echo EHR_CLIENT_SECRET=$EHR_CLIENT_SECRET >> .ehr_admin_details

log "=== ehr admin $EHR_ADMIN_EMAIL signed up to katanemo with accountId $EHR_ADMIN_ACCOUNT_ID ==="
log "=== clinet id ($EHR_CLIENT_ID) and client secret (XXXX) created to interact with katanemo api ==="
