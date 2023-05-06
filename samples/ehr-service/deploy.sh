source .ehr_admin_details
cd infra
terraform apply -var="client_key=$EHR_CLIENT_ID" -var="client_secret=$EHR_CLIENT_SECRET"
