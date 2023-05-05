variable "patient_records_table_name" {
  description = "The name of the DynamoDB table for patient records"
  type        = string
  default     = "patient-records"
}
variable "diagnostic_table_name" {
  description = "The name of the DynamoDB table for diagnostic"
  type        = string
  default     = "diagnostic"
}
variable "client_key" {
  description = "client key to access katanemo api"
  type        = string
}
variable "client_secret" {
  description = "client secret to access katanemo api"
  type        = string
}
variable "lambda_auth_name" {
  description = "katanemo lamba authorizer name"
  type        = string
  default = "lambda-auth"
}

variable "patient_service" {
  description = "patient service lamnbda function name"
  type        = string
  default = "patient-service"
}
variable "diagnostic_service" {
  description = "diagnostic service lamnbda function name"
  type        = string
  default = "diagnostic-service"
}

variable "aws_region" {
  description = "aws region"
  type        = string
  default = "us-west-1"
}
variable "auth_endpoint" {
  description = "katanemo auth endpoint"
  type        = string
  default = "https://auth.us-west-2.katanemo.dev"
}
