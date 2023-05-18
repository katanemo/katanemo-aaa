. ../common.sh
. .ehr_admin_details

KATANEMO_SERVICE_ID=$(../../../cli/bin/katutil get-default-service | jq -r .serviceId)

../../../cli/bin/katutil login-with-password --service_id $KATANEMO_SERVICE_ID --email $EHR_ADMIN_EMAIL --password $EHR_ADMIN_PASSWORD | jq -r .token
