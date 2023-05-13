#!/bin/sh
set -e

KATUTIL=../../cli/bin/katutil
AUTH_ENDPOINT=https://auth.us-west-2.katanemo.dev
KATANEMO_ACCOUNT_EMAIL=$1

if [[ -z "$KATANEMO_ACCOUNT_EMAIL" ]]; then
  echo "usage $0 <katanemo-account-email>"
  exit 1
fi

echo Enter password for $KATANEMO_ACCOUNT_EMAIL
read EHR_ADMIN_PASSWORD

source common.sh

KATANEMO_SERVICE_ID=$($KATUTIL get-default-service | jq -r .serviceId)

# get ehr admin token to create client key
LOGIN_RESP=$($KATUTIL login-with-password --service_id $KATANEMO_SERVICE_ID --email $KATANEMO_ACCOUNT_EMAIL --password $EHR_ADMIN_PASSWORD)
EHR_ADMIN_TOKEN=$(echo $LOGIN_RESP | jq -r .token)

KATANEMO_ACCOUNT_ID=$(echo $EHR_ADMIN_TOKEN | jq -R 'split(".") | .[1] | @base64d | fromjson | .accountId' -r)

log successfully logged in as $KATANEMO_ACCOUNT_EMAIL with katanemo $KATANEMO_ACCOUNT_ID

# get admin role id to be used with client key
EHR_ADMIN_ROLE_ID=`$KATUTIL get-roles --account_id $KATANEMO_ACCOUNT_ID --token $EHR_ADMIN_TOKEN | jq -r '.[] | select(.rolename | test("admin") ) | .roleId'`

# create client key to interact with katanemo api to be used with lambda authorizer
EHR_CLIENT_KEY_DETAILS=`$KATUTIL create-client-key --account_id $KATANEMO_ACCOUNT_ID --client_name 'ehr client key' --role_id $EHR_ADMIN_ROLE_ID --token $EHR_ADMIN_TOKEN`

EHR_CLIENT_ID=$(echo $EHR_CLIENT_KEY_DETAILS | jq -r .clientId)
EHR_CLIENT_SECRET=$(echo $EHR_CLIENT_KEY_DETAILS | jq -r .clientSecret)

log created client key id $EHR_CLIENT_ID and client key secret xxxxx used for identifying API calls to Katanemo by EHR SaaS Service

log npm install
npm install

log npm run build
npm run build

log cdk bootstrap
cdk bootstrap

log cdk deploy --parameters clientKey=$EHR_CLIENT_ID --parameters clientSecret=xxxxx --parameters authEndpoint="$AUTH_ENDPOINT"
cdk deploy --parameters clientKey=$EHR_CLIENT_ID --parameters clientSecret=$EHR_CLIENT_SECRET --parameters authEndpoint="$AUTH_ENDPOINT"

API_GATEWAY=$(aws cloudformation describe-stacks --query "Stacks[*].Outputs" --output json | jq '.[]' | jq '.[] | select(.OutputKey | test("patientRecordServiceEndpoint")) | .OutputValue' -r)

log API Gateway configured with katanemo lambda authorizer $API_GATEWAY
