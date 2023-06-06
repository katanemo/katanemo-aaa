#!/bin/sh
set -e

source ./common.sh


DEFAULT_API_ENDPOINT=https://api.katanemo.com

if [[ -z "$API_ENDPOINT" ]]; then
  API_ENDPOINT=$DEFAULT_API_ENDPOINT
fi

log using api endpoint $API_ENDPOINT, auth endpoint $AUTH_ENDPOINT

KATUTIL=../../cli/bin/katutil
KATANEMO_ACCOUNT_EMAIL=$1
EHR_SERVICE_ID=$2

if [[ -z "$KATANEMO_ACCOUNT_EMAIL" ]] || \
   [[ -z "$EHR_SERVICE_ID" ]]; then
  echo "usage $0 <katanemo-account-email> <service-id>"
  exit 1
fi

echo Enter password for $KATANEMO_ACCOUNT_EMAIL
read EHR_ADMIN_PASSWORD

KATANEMO_SERVICE_ID=$($KATUTIL get-default-service | jq -r .serviceId)

# get ehr admin token to create client key
LOGIN_RESP=$($KATUTIL login-with-password --service_id $KATANEMO_SERVICE_ID --email $KATANEMO_ACCOUNT_EMAIL --password $EHR_ADMIN_PASSWORD)
EHR_ADMIN_TOKEN=$(echo $LOGIN_RESP | jq -r .token)

KATANEMO_ACCOUNT_ID=`$KATUTIL get-account-id-from-token --token $EHR_ADMIN_TOKEN | jq -r '.accountId'`

log successfully logged in as $KATANEMO_ACCOUNT_EMAIL with katanemo $KATANEMO_ACCOUNT_ID

# get admin role id to be used with client key
EHR_ADMIN_ROLE_ID=`$KATUTIL get-roles --account_id $KATANEMO_ACCOUNT_ID --token $EHR_ADMIN_TOKEN | jq -r '.[] | select(.rolename | test("admin") ) | .roleId'`

# create client key to interact with katanemo api to be used with lambda authorizer
EHR_CLIENT_KEY_DETAILS=`$KATUTIL create-client-key --account_id $KATANEMO_ACCOUNT_ID --client_name 'ehr client key' --role_id $EHR_ADMIN_ROLE_ID --token $EHR_ADMIN_TOKEN`

EHR_CLIENT_ID=$(echo $EHR_CLIENT_KEY_DETAILS | jq -r .clientId)
EHR_CLIENT_SECRET=$(echo $EHR_CLIENT_KEY_DETAILS | jq -r .clientSecret)

log created client key id $EHR_CLIENT_ID and client key secret xxxxx used for identifying API calls to Katanemo by EHR SaaS Service


log setting up arc on ecs
pushd ../../arc-ecs
ADMIN_ACCOUNT_ID=$KATANEMO_ACCOUNT_ID SERVICE_ID=$EHR_SERVICE_ID  CLIENT_ID=$EHR_CLIENT_ID CLIENT_SECRET=$EHR_CLIENT_SECRET sh deploy.sh
popd

log npm install
npm install

log npm run build
npm run build

log getting the arc auth endpoint
ARC_AUTH_ENDPOINT=$(aws cloudformation describe-stacks --query "Stacks[*].Outputs" --output json | jq '.[]' | jq '.[] | select(.OutputKey | test("KatanemoArcServiceURL")) | .OutputValue' -r)

log arc endpoint address $ARC_AUTH_ENDPOINT

log cdk bootstrap
cdk bootstrap

log cdk deploy --parameters clientKey=$EHR_CLIENT_ID --parameters clientSecret=$EHR_CLIENT_SECRET --parameters apiEndpoint="$API_ENDPOINT" --parameters authEndpoint="$ARC_AUTH_ENDPOINT"
cdk deploy --parameters clientKey=$EHR_CLIENT_ID --parameters clientSecret=$EHR_CLIENT_SECRET --parameters apiEndpoint="$API_ENDPOINT" --parameters authEndpoint="$ARC_AUTH_ENDPOINT" --parameters serviceId=$EHR_SERVICE_ID

API_GATEWAY=$(aws cloudformation describe-stacks --query "Stacks[*].Outputs" --output json | jq '.[]' | jq '.[] | select(.OutputKey | test("patientRecordServiceEndpoint")) | .OutputValue' -r)

log Katanemo ARC Endpoint: $ARC_AUTH_ENDPOINT
log API Gateway configured with katanemo lambda authorizer $API_GATEWAY
