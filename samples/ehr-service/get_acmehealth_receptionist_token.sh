. .subscriber_details
. .ehr_service_details
katutil login-with-password --service_id $EHR_SERVICE_ID --email $RECEPTIONIST_EMAIL --password $RECEPTIONIST_PASSWORD | jq -r .token
