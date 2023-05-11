source common.sh
source .ehr_admin_details
set -e

AUTH_ENDPOINT=https://auth.us-west-2.katanemo.dev

if [[ -z "terraform" ]]; then
  cd tf_infra
  log terraform apply -var="client_key=$EHR_CLIENT_ID" -var="client_secret=$EHR_CLIENT_SECRET"
  terraform apply -var="client_key=$EHR_CLIENT_ID" -var="client_secret=$EHR_CLIENT_SECRET"
else
  log npm run build
  npm run build

  log cdk bootstrap
  cdk bootstrap

  log cdk deploy --parameters clientKey=$EHR_CLIENT_ID --parameters clientSecret=$EHR_CLIENT_SECRET --parameters authEndpoint="$AUTH_ENDPOINT"
  cdk deploy --parameters clientKey=$EHR_CLIENT_ID --parameters clientSecret=$EHR_CLIENT_SECRET --parameters authEndpoint="$AUTH_ENDPOINT"
fi
