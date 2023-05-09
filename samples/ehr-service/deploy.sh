source common.sh
source .ehr_admin_details
set -e

if [[ -z "terraform" ]]; then
  cd tf_infra
  log terraform apply -var="client_key=$EHR_CLIENT_ID" -var="client_secret=$EHR_CLIENT_SECRET"
  terraform apply -var="client_key=$EHR_CLIENT_ID" -var="client_secret=$EHR_CLIENT_SECRET"
else
  log cdk bootstrap
  cdk bootstrap

  log cdk deploy --parameters clientKey=$EHR_CLIENT_ID --parameters clientSecret=$EHR_CLIENT_SECRET
  cdk deploy --parameters clientKey=$EHR_CLIENT_ID --parameters clientSecret=$EHR_CLIENT_SECRET
fi
