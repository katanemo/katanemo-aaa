
log() {
  echo `date "+%Y-%m-%dT%H:%M:%S%z"` " - " "${@}"
}

KATUTIL=../../cli/bin/katutil

KATANEMO_SERVICE_ID=$($KATUTIL get-default-service | jq -r .serviceId)
EHR_ADMIN_PASSWORD=7TOfroc9aab3$
SUBSCRIBER_PASSWORD=7TOfroc9aab3$
DOCTOR_PASSWORD=7TOfroc9aab3$
