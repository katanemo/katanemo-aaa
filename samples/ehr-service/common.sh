
log() {
  echo `date "+%Y-%m-%dT%H:%M:%S%z"` " - " "${@}"
}

KATANEMO_SERVICE_ID=$(katutil get-default-service | jq -r .serviceId)
EHR_ADMIN_PASSWORD=7TOfroc9aab3$
SUBSCRIBER_PASSWORD=7TOfroc9aab3$
DOCTOR_PASSWORD=7TOfroc9aab3$
