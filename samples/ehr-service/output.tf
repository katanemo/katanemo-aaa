output "katanemo_lambda_auth" {
  value = module.aws_lambda_auth.lambda_function_name
  description = "value of the lambda function arn"
}

output "katanemo_apigw_id" {
  value = aws_api_gateway_rest_api.patient_records_api.id
  description = "value of the api gateway id"
}
