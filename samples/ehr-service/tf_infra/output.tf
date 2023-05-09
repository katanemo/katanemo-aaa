output "katanemo_apigw_id" {
  value = "https://${aws_api_gateway_rest_api.patient_records_api.id}.execute-api.us-west-1.amazonaws.com/staging"
  description = "value of the api gateway id"
}
