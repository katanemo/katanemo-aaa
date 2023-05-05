variable "patient_records_table_name" {
  description = "The name of the DynamoDB table for patient records"
  type        = string
  default     = "patient-records"
}

variable "diagnostics_table_name" {
  description = "The name of the DynamoDB table for diagnostics"
  type        = string
  default     = "diagnostics"
}
