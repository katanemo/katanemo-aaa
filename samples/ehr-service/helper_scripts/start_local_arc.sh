source .ehr_admin_details 
source .ehr_service_details

DEFAULT_API_ENDPOINT=https://api.us-west-2.katanemo.dev
DEFAULT_ARC_IMAGE=public.ecr.aws/c2g2h4e5/repo/aaa-staging-public:arc_latest

if [[ -z "$ARC_IMAGE" ]]; then
  ARC_IMAGE=$DEFAULT_ARC_IMAGE
fi"]]

if [[ -z "$API_ENDPOINT" ]]; then
  API_ENDPOINT=$DEFAULT_API_ENDPOINT
fi

docker run -it -e API_ENDPOINT="$API_ENDPOINT" \
               -e SERVICE_ID="$EHR_SERVICE_ID" \
               -e CLIENT_KEY="$EHR_CLIENT_ID" \
               -e CLIENT_SECRET="$EHR_CLIENT_SECRET" \
               --rm -p 8083:8083 $ARC_IMAGE
