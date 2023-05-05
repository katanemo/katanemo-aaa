#!/bin/sh
set -e -o errexit -o pipefail

. ./common.sh
. .ehr_admin_details
. .ehr_service_details

log '=== signing up subscriber to katanemo ==='

if [[ -z "$1" ]] || [[ -z "$2" ]]; then
  echo "usage: $0 <subscriber_admin_email> <subscriber_doctor_email>"
  exit 1
fi

SUBSCRIBER_EMAIL=$1
DOCTOR_EMAIL=$2

log signing up subscriber $SUBSCRIBER_EMAIL to $EHR_SERVICE_ID
log katutil signup-service --email $SUBSCRIBER_EMAIL --service_id $EHR_SERVICE_ID
SUBSCRIBER_ACCOUNT_ID=$(katutil signup-service --email $SUBSCRIBER_EMAIL --service_id $EHR_SERVICE_ID | jq -r .accountId)

log enter code sent to $SUBSCRIBER_EMAIL
read CODE

log katutil confirm-and-set-password --code $CODE --email $SUBSCRIBER_EMAIL --service_id $EHR_SERVICE_ID --password xxxx --account_id $SUBSCRIBER_ACCOUNT_ID
katutil confirm-and-set-password --code $CODE --email $SUBSCRIBER_EMAIL --service_id $EHR_SERVICE_ID --password $SUBSCRIBER_PASSWORD --account_id $SUBSCRIBER_ACCOUNT_ID

log getting token for subscriber $SUBSCRIBER_EMAIL
log katutil login-with-password --service_id $EHR_SERVICE_ID --email $SUBSCRIBER_EMAIL --password xxxx
SUBSCRIBER_ACCESS_TOKEN=`katutil login-with-password --service_id $EHR_SERVICE_ID --email $SUBSCRIBER_EMAIL --password $SUBSCRIBER_PASSWORD | jq .token -r`

log '=== adding doctor account ==='

# create doctor account to manage patient record
log adding doctor account $DOCTOR_EMAIL
log katutil add-user --account_id $SUBSCRIBER_ACCOUNT_ID --email $DOCTOR_EMAIL --token xxxx --tags '{"function": ["doctor"]}'
DOCTOR_ACCOUNT_ID=`katutil add-user --account_id $SUBSCRIBER_ACCOUNT_ID --email $DOCTOR_EMAIL --token $SUBSCRIBER_ACCESS_TOKEN --tags '{"function": ["doctor"]}' | jq -r .accountId`

log enter code sent to $DOCTOR_EMAIL
read CODE

log katutil confirm-and-set-password --account_id $DOCTOR_ACCOUNT_ID --email $DOCTOR_EMAIL --code $CODE --service_id $EHR_SERVICE_ID --password xxxx --account_id $DOCTOR_ACCOUNT_ID
# activate doctor account
katutil confirm-and-set-password --account_id $DOCTOR_ACCOUNT_ID --email $DOCTOR_EMAIL --code $CODE --service_id $EHR_SERVICE_ID --password $DOCTOR_PASSWORD --account_id $DOCTOR_ACCOUNT_ID

log creating role with access to patient record
log katutil create-role --policies '[{"allow": ["GET:/patient/{patientId}", "PUT:/patient/{patientId}"], "where": "$principalTags:function = doctor"}, {"allow": ["POST:/diagnostics/", "GET:/diagnostics/{diagnosticsId}"], "where": "$principalTags:function = doctor"}]' --account_id $SUBSCRIBER_ACCOUNT_ID --service_id $EHR_SERVICE_ID --role_name 'patient record doctor access' --token xxxx
# create role to manage patient record and assign it to doctor account
DOCTOR_ROLE_DETAILS=`katutil create-role --policies '[{"allow": ["GET:/patient/{patientId}", "PUT:/patient/{patientId}"], "where": "$principalTags:function = doctor"}, {"allow": ["POST:/diagnostics/", "GET:/diagnostics/{diagnosticsId}"], "where": "$principalTags:function = doctor"}]' --account_id $SUBSCRIBER_ACCOUNT_ID --service_id $EHR_SERVICE_ID --role_name 'patient record doctor access' --token $SUBSCRIBER_ACCESS_TOKEN`
DOCTOR_ROLE_ID=`echo $DOCTOR_ROLE_DETAILS | jq -r .roleId`

log assigning doctor role to doctor account
log katutil assign-role --principal_id $DOCTOR_EMAIL --role_id $DOCTOR_ROLE_ID --token xxxx
katutil assign-role --principal_id $DOCTOR_EMAIL --role_id $DOCTOR_ROLE_ID --token $SUBSCRIBER_ACCESS_TOKEN &> /dev/null

echo SUBSCRIBER_EMAIL=$SUBSCRIBER_EMAIL > .subscriber_details
echo DOCTOR_EMAIL=$DOCTOR_EMAIL >> .subscriber_details
echo DOCTOR_ACCOUNT_ID=$DOCTOR_ACCOUNT_ID >> .subscriber_details
echo DOCTOR_ROLE_ID=$DOCTOR_ROLE_ID >> .subscriber_details

log "=== subscribed $SUBSCRIBER_EMAIL to $EHR_SERVICE_ID with accountId $SUBSCRIBER_ACCOUNT_ID ==="
log "=== added doctor account $DOCTOR_EMAIL with roleId $DOCTOR_ROLE_ID  ==="
