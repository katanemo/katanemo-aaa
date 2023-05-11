set -e
. common.sh

if [[ "$1" == "terraform" ]]; then
  echo "using terraform"
  cd infra
  API_GATEWAY=$(terraform output katanemo_apigw_id | sed -e 's/\"//g')
  cd -
else
  API_GATEWAY=$(aws cloudformation describe-stacks --query "Stacks[*].Outputs" --output json | jq '.[]' | jq '.[] | select(.OutputKey | test("patientRecordServiceEndpoint")) | .OutputValue' -r)
fi

echo "API_GATEWAY: $API_GATEWAY"

log 'trying to create patient record using receptionint token'
log curl -XPOST -d '{"name": "John Doe", "notes": "the perfect human being"}' $API_GATEWAY/patient -H "Authorization: Bearer xxxx"
curl -XPOST -d '{"name": "John Doe", "notes": "the perfect human being"}' $API_GATEWAY/patient -H "Authorization: Bearer `sh get_acmehealth_receptionist_token.sh`" 2> /dev/null | jq .

log 'trying to create patient record using doctor token'
log curl -XPOST -d '{"name": "John Doe", "notes": "the perfect human being"}' $API_GATEWAY/patient -H "Authorization: Bearer xxxx"
curl -XPOST -d '{"name": "John Doe", "notes": "the perfect human being"}' $API_GATEWAY/patient -H "Authorization: Bearer `sh get_acmehealth_doctor_token.sh`" 2> /dev/null | jq .

log 'trying to create patient record using acme health admin token'
log curl -XPOST -d '{"name": "John Doe", "notes": "the perfect human being"}' $API_GATEWAY/patient -H "Authorization: Bearer xxxx"
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
ACMEHEALTH_ADMIN_TOKEN=$(sh get_acmehealth_admin_token.sh)
curl $API_GATEWAY/patient/$PATIENT_ID -H "Authorization: Bearer $ACMEHEALTH_ADMIN_TOKEN" 2> /dev/null | jq .

log 2nd try to get patient record using acme health admin token
curl $API_GATEWAY/patient/$PATIENT_ID -H "Authorization: Bearer $ACMEHEALTH_ADMIN_TOKEN" 2> /dev/null | jq .
