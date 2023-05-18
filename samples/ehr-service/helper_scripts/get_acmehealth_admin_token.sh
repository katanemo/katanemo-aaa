. ../common.sh
. .subscriber_details
. .ehr_service_details

../../../.cli/bin/katutil login-with-password --service_id $EHR_SERVICE_ID --email $SUBSCRIBER_EMAIL --password $SUBSCRIBER_PASSWORD | jq -r .token
