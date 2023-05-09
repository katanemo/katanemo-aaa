#!/bin/sh
set -e -o errexit -o pipefail

. ./common.sh
. .ehr_admin_details
. .ehr_service_details

log '=== signing up subscriber to katanemo ==='

if [[ -z "$1" ]] || [[ -z "$2" ]] || [[ -z "$3" ]]; then
  echo "usage: $0 <subscriber_admin_email> <subscriber_doctor_email> <receptionist_email>"
  exit 1
fi

SUBSCRIBER_EMAIL=$1
DOCTOR_EMAIL=$2
RECEPTIONIST_EMAIL=$3

log signing up subscriber $SUBSCRIBER_EMAIL to $EHR_SERVICE_ID
log katutil signup-service --email $SUBSCRIBER_EMAIL --service_id $EHR_SERVICE_ID
SUBSCRIBER_ACCOUNT_ID=$($KATUTIL signup-service --email $SUBSCRIBER_EMAIL --service_id $EHR_SERVICE_ID | jq -r .accountId)

log enter code sent to $SUBSCRIBER_EMAIL
read CODE

if [[ -z "$CODE" ]]; then
  CODE="-"
fi

log katutil confirm-and-set-password --code $CODE --email $SUBSCRIBER_EMAIL --service_id $EHR_SERVICE_ID --password xxxx --account_id $SUBSCRIBER_ACCOUNT_ID
$KATUTIL confirm-and-set-password --code $CODE --email $SUBSCRIBER_EMAIL --service_id $EHR_SERVICE_ID --password $SUBSCRIBER_PASSWORD --account_id $SUBSCRIBER_ACCOUNT_ID

log getting token for subscriber $SUBSCRIBER_EMAIL
log katutil login-with-password --service_id $EHR_SERVICE_ID --email $SUBSCRIBER_EMAIL --password xxxx
SUBSCRIBER_ACCESS_TOKEN=$($KATUTIL login-with-password --service_id $EHR_SERVICE_ID --email $SUBSCRIBER_EMAIL --password $SUBSCRIBER_PASSWORD | jq .token -r)

log '=== adding doctor account ==='

# create doctor account to manage patient record
log adding doctor account $DOCTOR_EMAIL
log katutil add-user --account_id $SUBSCRIBER_ACCOUNT_ID --email $DOCTOR_EMAIL --token xxxx --tags '{"function": ["doctor"]}'
$KATUTIL add-user --account_id $SUBSCRIBER_ACCOUNT_ID --email $DOCTOR_EMAIL --token $SUBSCRIBER_ACCESS_TOKEN --tags '{"function": ["doctor"]}' &> /dev/null

log enter code sent to $DOCTOR_EMAIL
read CODE

if [[ -z "$CODE" ]]; then
  CODE="-"
fi

log katutil confirm-and-set-password --account_id $SUBSCRIBER_ACCOUNT_ID --email $DOCTOR_EMAIL --code $CODE --service_id $EHR_SERVICE_ID --password xxxx
# activate doctor account
$KATUTIL confirm-and-set-password --account_id $SUBSCRIBER_ACCOUNT_ID --email $DOCTOR_EMAIL --code $CODE --service_id $EHR_SERVICE_ID --password $DOCTOR_PASSWORD

log creating role with access to patient record
log katutil create-role --policies '[{"allow": ["GET:/patient/{patientId}", "PUT:/patient/{patientId}"], "where": "$principalTags:function = doctor"}, {"allow": ["POST:/diagnostic", "GET:/diagnostic/{diagnosticId}"], "where": "$principalTags:function = doctor"}]' --account_id $SUBSCRIBER_ACCOUNT_ID --service_id $EHR_SERVICE_ID --role_name 'patient record doctor access' --token xxxx
# create role to manage patient record and assign it to doctor account
DOCTOR_ROLE_DETAILS=$($KATUTIL create-role --policies '[{"allow": ["GET:/patient/{patientId}", "PUT:/patient/{patientId}"], "where": "$principalTags:function = doctor"}, {"allow": ["POST:/diagnostic", "GET:/diagnostic/{diagnosticId}"], "where": "$principalTags:function = doctor"}]' --account_id $SUBSCRIBER_ACCOUNT_ID --service_id $EHR_SERVICE_ID --role_name 'patient record doctor access' --token $SUBSCRIBER_ACCESS_TOKEN)
DOCTOR_ROLE_ID=`echo $DOCTOR_ROLE_DETAILS | jq -r .roleId`

log assigning doctor role to doctor account
log katutil assign-role --principal_id $DOCTOR_EMAIL --role_id $DOCTOR_ROLE_ID --token xxxx
$KATUTIL assign-role --principal_id $DOCTOR_EMAIL --role_id $DOCTOR_ROLE_ID --token $SUBSCRIBER_ACCESS_TOKEN &> /dev/null

# create receptionist account to manage appointments
log adding receptionist account $RECEPTIONIST_EMAIL
log katutil add-user --account_id $SUBSCRIBER_ACCOUNT_ID --email $RECEPTIONIST_EMAIL --token xxxx --tags '{"function": ["doctor"]}'
$KATUTIL add-user --account_id $SUBSCRIBER_ACCOUNT_ID --email $RECEPTIONIST_EMAIL --token $SUBSCRIBER_ACCESS_TOKEN --tags '{"function": ["receptionist"]}' &> /dev/null

log enter code sent to $RECEPTIONIST_EMAIL
read CODE

if [[ -z "$CODE" ]]; then
  CODE="-"
fi

log katutil confirm-and-set-password --account_id $SUBSCRIBER_ACCOUNT_ID --email $RECEPTIONIST_EMAIL --code $CODE --service_id $EHR_SERVICE_ID --password xxxx
# activate doctor account
$KATUTIL confirm-and-set-password --account_id $SUBSCRIBER_ACCOUNT_ID --email $RECEPTIONIST_EMAIL --code $CODE --service_id $EHR_SERVICE_ID --password $DOCTOR_PASSWORD

SUBSCRIBER_USER_ROLE_ID=$($KATUTIL get-roles --account_id $SUBSCRIBER_ACCOUNT_ID --token $SUBSCRIBER_ACCESS_TOKEN | jq -r '.[] | select(.rolename | test("user") ) | .roleId')
log assigning user role to receptionist account
log katutil assign-role --principal_id $RECEPTIONIST_EMAIL --role_id $SUBSCRIBER_USER_ROLE_ID --token xxxx
$KATUTIL assign-role --principal_id $RECEPTIONIST_EMAIL --role_id $SUBSCRIBER_USER_ROLE_ID --token $SUBSCRIBER_ACCESS_TOKEN &> /dev/null

echo SUBSCRIBER_ACCOUNT_ID=$SUBSCRIBER_ACCOUNT_ID > .subscriber_details
echo SUBSCRIBER_EMAIL=$SUBSCRIBER_EMAIL >> .subscriber_details
echo SUBSCRIBER_PASSWORD=$SUBSCRIBER_PASSWORD >> .subscriber_details

echo DOCTOR_EMAIL=$DOCTOR_EMAIL >> .subscriber_details
echo DOCTOR_PASSWORD=$DOCTOR_PASSWORD >> .subscriber_details
echo DOCTOR_ROLE_ID=$DOCTOR_ROLE_ID >> .subscriber_details

echo RECEPTIONIST_EMAIL=$RECEPTIONIST_EMAIL >> .subscriber_details
echo RECEPTIONIST_PASSWORD=$DOCTOR_PASSWORD >> .subscriber_details

log "=== subscribed $SUBSCRIBER_EMAIL to $EHR_SERVICE_ID with accountId $SUBSCRIBER_ACCOUNT_ID ==="
log "=== added doctor account $DOCTOR_EMAIL with roleId $DOCTOR_ROLE_ID  ==="
