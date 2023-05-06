. common.sh
cd infra
API_GATEWAY=$(terraform output katanemo_apigw_id | sed -e 's/\"//g')
cd -

log 'trying to create patient record using receptionint token'
log curl -XPOST -d '{"name": "John Doe", "notes": "the perfect human being"}' $API_GATEWAY/patient -H "Authorization: Bearer `sh get_acmehealth_receptionist_token.sh`" 2> /dev/null | jq .
curl -XPOST -d '{"name": "John Doe", "notes": "the perfect human being"}' $API_GATEWAY/patient -H "Authorization: Bearer `sh get_acmehealth_receptionist_token.sh`" 2> /dev/null | jq .

log 'trying to create patient record using doctor token'
curl -XPOST -d '{"name": "John Doe", "notes": "the perfect human being"}' $API_GATEWAY/patient -H "Authorization: Bearer `sh get_acmehealth_doctor_token.sh`" 2> /dev/null | jq .

log 'trying to create patient record using acme health admin token'
PATIENT_DETAIL=$(curl -XPOST -d '{"name": "John Doe", "notes": "the perfect human being"}' $API_GATEWAY/patient -H "Authorization: Bearer `sh get_acmehealth_admin_token.sh`" 2> /dev/null | jq .)
echo $PATIENT_DETAIL | jq .

PATIENT_ID=$(echo $PATIENT_DETAIL | jq .Item.patientId -r)

log 'trying to get patient record using receptionint token'
log curl $API_GATEWAY/patient/$PATIENT_ID -H "Authorization: Bearer xxxx"
curl $API_GATEWAY/patient/$PATIENT_ID -H "Authorization: Bearer `sh get_acmehealth_receptionist_token.sh`" 2> /dev/null | jq .

log 'trying to get patient record using doctor token'
log curl $API_GATEWAY/patient/$PATIENT_ID -H "Authorization: Bearer xxxx"
curl $API_GATEWAY/patient/$PATIENT_ID -H "Authorization: Bearer `sh get_acmehealth_doctor_token.sh`" 2> /dev/null | jq .

log 'trying to get patient record using acme health admin token'
log curl $API_GATEWAY/patient/$PATIENT_ID -H "Authorization: Bearer xxxx"
curl $API_GATEWAY/patient/$PATIENT_ID -H "Authorization: Bearer `sh get_acmehealth_admin_token.sh`" 2> /dev/null | jq .
