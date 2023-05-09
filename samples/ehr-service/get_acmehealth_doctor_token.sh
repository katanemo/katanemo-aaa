. common.sh
. .subscriber_details
. .ehr_service_details

$KATUTIL login-with-password --service_id $EHR_SERVICE_ID --email $DOCTOR_EMAIL --password $DOCTOR_PASSWORD | jq -r .token
