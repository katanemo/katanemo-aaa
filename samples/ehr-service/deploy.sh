#!/bin/sh
set -e

KATUTIL=../../cli/bin/katutil
AUTH_ENDPOINT=https://auth.us-west-2.katanemo.dev
EHR_ADMIN_EMAIL=$1
EHR_ADMIN_ACCOUNT_ID=$2

if [[ -z "$EHR_ADMIN_EMAIL" ]]  || \
   [[ -z "$EHR_ADMIN_ACCOUNT_ID" ]]; then
  echo "usage $0 <ehr_admin_email> <ehr_admin_account_id>"
  exit 1
fi

echo 'Enter password for ehr admin'
read EHR_ADMIN_PASSWORD

source common.sh

KATANEMO_SERVICE_ID=$($KATUTIL get-default-service | jq -r .serviceId)

# get ehr admin token to create client key
EHR_ADMIN_TOKEN=$($KATUTIL login-with-password --service_id $KATANEMO_SERVICE_ID --email $EHR_ADMIN_EMAIL --password $EHR_ADMIN_PASSWORD | jq -r .token)

log successfully logged in as ehr admin

# get admin role id to be used with client key
EHR_ADMIN_ROLE_ID=`$KATUTIL get-roles --account_id $EHR_ADMIN_ACCOUNT_ID --token $EHR_ADMIN_TOKEN | jq -r '.[] | select(.rolename | test("admin") ) | .roleId'`

log got role for ehr admin $EHR_ADMIN_ROLE_ID

# create client key to interact with katanemo api to be used with lambda authorizer
EHR_CLIENT_KEY_DETAILS=`$KATUTIL create-client-key --account_id $EHR_ADMIN_ACCOUNT_ID --client_name 'ehr client key' --role_id $EHR_ADMIN_ROLE_ID --token $EHR_ADMIN_TOKEN`

EHR_CLIENT_ID=$(echo $EHR_CLIENT_KEY_DETAILS | jq -r .clientId)
EHR_CLIENT_SECRET=$(echo $EHR_CLIENT_KEY_DETAILS | jq -r .clientSecret)

log created client key id $EHR_CLIENT_ID and client key secret xxxxx

log npm install
npm install

log npm run build
npm run build

log cdk bootstrap
cdk bootstrap

log cdk deploy --parameters clientKey=$EHR_CLIENT_ID --parameters clientSecret=xxxxx --parameters authEndpoint="$AUTH_ENDPOINT"
cdk deploy --parameters clientKey=$EHR_CLIENT_ID --parameters clientSecret=$EHR_CLIENT_SECRET --parameters authEndpoint="$AUTH_ENDPOINT"

API_GATEWAY=$(aws cloudformation describe-stacks --query "Stacks[*].Outputs" --output json | jq '.[]' | jq '.[] | select(.OutputKey | test("patientRecordServiceEndpoint")) | .OutputValue' -r)

log API Gateway setup with with lambda authorizer $API_GATEWAY
