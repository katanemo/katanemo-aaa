set -e
# set -x

export API_ENDPOINT=https://api.us-west-2.katanemo.dev
export AUTH_ENDPOINT=https://auth.us-west-2.katanemo.dev

export DEFAULT_PASSWORD=7TOfroc9
EMAIL_PREFIX=adil+`uuidgen | md5sum | head -c 8; echo;`

EHR_ADMIN_EMAIL=$EMAIL_PREFIX+ehr-admin@katanemo.com
EVERGREEN_ADMIN_EMAIL=$EMAIL_PREFIX+evergreenadmin@katanemo.com
EVERGREEN_DOCTOR_EMAIL=$EMAIL_PREFIX+evergreendoctor@katanemo.com

log() {
  echo `date "+%Y-%m-%dT%H:%M:%S%z"` " - " "${@}"
}

echo
log '=== initializing service ==='

# get default service id
DEFAULT_SERVICE_ID=`katutil get-default-service | jq -r .serviceId`

# subscribe default service for ehr admin
EHR_ADMIN_ACCOUNT_ID=`katutil signup-service --email $EHR_ADMIN_EMAIL --service_id $DEFAULT_SERVICE_ID | jq -r .accountId`

# activate ehr admin account
katutil confirm-and-set-password --email $EHR_ADMIN_EMAIL --service_id $DEFAULT_SERVICE_ID --password $DEFAULT_PASSWORD --account_id $EHR_ADMIN_ACCOUNT_ID

EHR_ADMIN_ACCESS_TOKEN=`katutil login-with-password --service_id $DEFAULT_SERVICE_ID --email $EHR_ADMIN_EMAIL --password $DEFAULT_PASSWORD | jq .token -r`

# create client keys to interact with katanemo api
EHR_ADMIN_ROLE_ID=`katutil get-roles --account_id $EHR_ADMIN_ACCOUNT_ID --token $EHR_ADMIN_ACCESS_TOKEN | jq -r '.[] | select(.rolename | test("admin") ) | .roleId'`
EHR_CLIENT_KEY=`katutil create-client-key --account_id $EHR_ADMIN_ACCOUNT_ID --client_name 'ehr client key' --role_id $EHR_ADMIN_ROLE_ID --token $EHR_ADMIN_ACCESS_TOKEN`

# create and upload ehr service with openapi spec
EHR_SERVICE_ID=`katutil create-service --service_id $DEFAULT_SERVICE_ID --email $EHR_ADMIN_EMAIL --password $DEFAULT_PASSWORD --name 'ehr patient record' --openapi_spec $PWD/ehr.yaml --redirect_url https://localhost:8083/welcome | jq -r .serviceId`

# create subscriber for ehr service (evergreen) and activate account
EVERGREEN_ACCOUNT_ID=`katutil signup-service --email $EVERGREEN_ADMIN_EMAIL --service_id $EHR_SERVICE_ID | jq -r .accountId`
katutil confirm-and-set-password --code "" --email $EVERGREEN_ADMIN_EMAIL --service_id $EHR_SERVICE_ID --password $DEFAULT_PASSWORD --account_id $EVERGREEN_ACCOUNT_ID

EVERGREEN_ADMIN_ACCESS_TOKEN=`katutil login-with-password --service_id $EHR_SERVICE_ID --email $EVERGREEN_ADMIN_EMAIL --password $DEFAULT_PASSWORD | jq .token -r`

# create doctor account to manage patient record
DOCTOR_ACCOUNT_ID=`katutil add-user --account_id $EVERGREEN_ACCOUNT_ID --email $EVERGREEN_DOCTOR_EMAIL --token $EVERGREEN_ADMIN_ACCESS_TOKEN --tags '{"function": ["doctor"]}' | jq -r .accountId`
# activate doctor account
katutil confirm-and-set-password --account_id $DOCTOR_ACCOUNT_ID --email $EVERGREEN_DOCTOR_EMAIL --code "" --service_id $EHR_SERVICE_ID --password $DEFAULT_PASSWORD

# create role to manage patient record and assign it to doctor account
DOCTOR_ROLE_DETAILS=`katutil create-role --policies '[{"allow": ["GET:/patient/{patientId}", "PUT:/patient/{patientId}"], "where": "$principalTags:function = doctor"}, {"allow": ["POST:/diagnostics/", "GET:/diagnostics/{diagnosticsId}"], "where": "$principalTags:function = doctor"}]' --account_id $EVERGREEN_ACCOUNT_ID --service_id $EHR_SERVICE_ID --role_name 'patient record doctor access' --token $EHR_ADMIN_ACCESS_TOKEN`
ROLE_ID=`echo $DOCTOR_ROLE_DETAILS | jq -r .roleId`
katutil assign-role --principal_id $EVERGREEN_DOCTOR_EMAIL --role_id $ROLE_ID --token $EVERGREEN_ADMIN_ACCESS_TOKEN &> /dev/null

EVERGREEN_DOCTOR_ACCESS_TOKEN_TOKEN=`katutil login-with-password --service_id $EHR_SERVICE_ID --email $EVERGREEN_DOCTOR_EMAIL --password $DEFAULT_PASSWORD --account_id $EVERGREEN_ACCOUNT_ID | jq .token -r`

echo 'EHR_ADMIN_EMAIL='$EHR_ADMIN_EMAIL > ehr.env
echo 'EHR_ADMIN_ACCOUNT_ID='$EHR_ADMIN_ACCOUNT_ID >> ehr.env
echo 'EHR_SERVICE_ID='$EHR_SERVICE_ID >> ehr.env
echo 'EHR_CLIENT_KEY='`echo $EHR_CLIENT_KEY | jq -r .clientId` >> ehr.env
echo 'EHR_CLIENT_SECRET='`echo $EHR_CLIENT_KEY | jq -r .clientSecret` >> ehr.env
echo 'EVERGREEN_ADMIN_EMAIL='$EVERGREEN_ADMIN_EMAIL >> ehr.env
echo 'EVERGREEN_ACCOUNT_ID='$EVERGREEN_ACCOUNT_ID >> ehr.env
echo 'EHR_ADMIN_ACCESS_TOKEN='$EHR_ADMIN_ACCESS_TOKEN >> ehr.env
echo 'EVERGREEN_ADMIN_ACCESS_TOKEN='$EVERGREEN_ADMIN_ACCESS_TOKEN >> ehr.env
echo 'EVERGREEN_DOCTOR_ACCESS_TOKEN_TOKEN='$EVERGREEN_DOCTOR_ACCESS_TOKEN_TOKEN >> ehr.env
echo 'EVERGREEN_DOCTOR_EMAIL'=$EVERGREEN_DOCTOR_EMAIL >> ehr.env
echo
log '=== boostrap complete ==='
echo
log 'EHR Admin Email: '$EHR_ADMIN_EMAIL
log 'EHR Admin Account Id: '$EHR_ADMIN_ACCOUNT_ID
log 'EHR Admin Access Token: xxxxx (see ehr.env)'
log 'EHR Service Id: '$EHR_SERVICE_ID
log 'EHR Client Id: '`echo $EHR_CLIENT_KEY | jq -r .clientId`
log 'EHR Client Secret: '`echo $EHR_CLIENT_KEY | jq -r .clientSecret`
echo
log 'Evergreen Admin Email: '$EVERGREEN_ADMIN_EMAIL
log 'Evergreen Admin Account Id: '$EVERGREEN_ACCOUNT_ID
log 'Evergreen Admin Access Token: xxxxx (see ehr.env)'
log 'Evergreen Doctor Email Address: '$EVERGREEN_DOCTOR_EMAIL
log 'Evergreen Dcotor Access Token: xxxxx (see ehr.env)'
log 'Evergreen Doctor Access Policy: '
echo $DOCTOR_ROLE_DETAILS | jq -r .policies

# EVERGREEN_DOCTOR=$EVERGREEN_ADMIN_EMAIL

# API_GATEWAY_ENDPOINT=https://1oxr45usjc.execute-api.us-east-1.amazonaws.com/staging
# DOCTOR_ACCESS_TOKEN=`python -m katutil login-with-password --service_id $EHR_SERVICE_ID --email $EVERGREEN_DOCTOR --password $DEFAULT_PASSWORD | jq .token -r`

# DOCTOR_ACCESS_TOKEN=`python -m katutil login-with-password --service_id $EHR_SERVICE_ID --email $EVERGREEN_DOCTOR --password $DEFAULT_PASSWORD 2> /dev/null | jq .token -r`
# echo $API_GATEWAY_ENDPOINT
# curl -XPOST -v -H 'Authorization: Bearer '$DOCTOR_ACCESS_TOKEN'' -H 'Content-Type: application/json' -d '{"name": "Tom Brands"}' $API_GATEWAY_ENDPOINT/patient 2>&1 | grep "< HTTP/"
# curl -XPOST -v -H 'Authentication: Bearer '$DOCTOR_ACCESS_TOKEN'' -H 'Content-Type: application/json' -d '{"type": "observation", "value": "high blood pressure", "patientId": "1234"}' $API_GATEWAY_ENDPOINT/diagnostics 2>&1 | grep "< HTTP/"
