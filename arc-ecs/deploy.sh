
DEFAULT_API_ENDPOINT="https://api.katanemo.com"
DEFAULT_ARCOS_ENDPOINT="https://auth.katanemo.com"
DEFAULT_ARC_SHA="9059ddf"

if [[ -z "$API_ENDPOINT" ]]; then
  API_ENDPOINT=$DEFAULT_API_ENDPOINT
fi

if [[ -z "$ARCOS_ENDPOINT" ]]; then
  ARCOS_ENDPOINT=$DEFAULT_ARCOS_ENDPOINT
fi

if [[ -z "$ARC_SHA" ]]; then
  ARC_SHA=$DEFAULT_ARC_SHA
fi

if [[ -z "$SERVICE_ID" ]] || \
   [[ -z "$CLIENT_ID" ]] || \
   [[ -z "$CLIENT_SECRET" ]]; then
  echo "Please set the following environment variables:"
  echo "SERVICE_ID"
  echo "CLIENT_ID"
  echo "CLIENT_SECRET"
  exit 1
fi

npm install
npm run build

cdk deploy --parameters serviceId=$SERVICE_ID \
           --parameters clientKey=$CLIENT_ID \
           --parameters clientSecret=$CLIENT_SECRET \
           --parameters apiEndpoint="$API_ENDPOINT" \
           --parameters arcSha="$ARC_SHA"
