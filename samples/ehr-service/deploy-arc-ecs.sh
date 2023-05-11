source common.sh
source .ehr_admin_details
source .ehr_service_details

set -e

pushd ../../arc-ecs
ADMIN_ACCOUNT_ID=$EHR_ADMIN_ACCOUNT_ID SERVICE_ID=$EHR_SERVICE_ID  CLIENT_ID=$EHR_CLIENT_ID CLIENT_SECRET=$EHR_CLIENT_SECRET sh deploy.sh
popd

log npm run build
npm run build

log getting the arc auth endpoint

ARC_AUTH_ENDPOINT=$(aws cloudformation describe-stacks --query "Stacks[*].Outputs" --output json | jq '.[]' | jq '.[] | select(.OutputKey | test("KatanemoArcServiceURL")) | .OutputValue' -r)

log arc endpoint address $ARC_AUTH_ENDPOINT

log cdk bootstrap
cdk bootstrap


log cdk deploy --parameters clientKey=$EHR_CLIENT_ID --parameters clientSecret=$EHR_CLIENT_SECRET --parameters apiEndpoint="https://api.us-west-2.katanemo.dev" --parameters authEndpoint="$ARC_AUTH_ENDPOINT"
cdk deploy --parameters clientKey=$EHR_CLIENT_ID --parameters clientSecret=$EHR_CLIENT_SECRET --parameters apiEndpoint="https://api.us-west-2.katanemo.dev" --parameters authEndpoint="$ARC_AUTH_ENDPOINT"
