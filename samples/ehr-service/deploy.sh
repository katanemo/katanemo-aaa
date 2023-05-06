source common.sh
source .ehr_admin_details
set -e

cd infra
if [[ -z "$1" ]]; then
  log terraform apply -var="client_key=$EHR_CLIENT_ID" -var="client_secret=$EHR_CLIENT_SECRET"
  terraform apply -var="client_key=$EHR_CLIENT_ID" -var="client_secret=$EHR_CLIENT_SECRET"
else
  log terraform apply -var="client_key=$EHR_CLIENT_ID" -var="client_secret=$EHR_CLIENT_SECRET" --var="auth_endpoint=$1"
  terraform apply -var="client_key=$EHR_CLIENT_ID" -var="client_secret=$EHR_CLIENT_SECRET" --var="auth_endpoint=$1"
fi
