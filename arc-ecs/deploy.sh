if [[ -z "$ADMIN_ACCOUNT_ID" ]] || \
   [[ -z "$SERVICE_ID" ]] || \
   [[ -z "$SERVICE_ID" ]] || \
   [[ -z "$CLIENT_ID" ]] || \
   [[ -z "$CLIENT_SECRET" ]]; then
  echo "Please set the following environment variables:"
  echo "ADMIN_ACCOUNT_ID"
  echo "SERVICE_ID"
  echo "CLIENT_ID"
  echo "CLIENT_SECRET"
  exit 1
fi

npm run build

cdk deploy --parameters accountId=$ADMIN_ACCOUNT_ID \
           --parameters serviceId=$SERVICE_ID \
           --parameters clientKey=$CLIENT_ID \
           --parameters clientSecret=$CLIENT_SECRET \
           --parameters apiEndpoint="https://api.us-west-2.katanemo.dev" \
