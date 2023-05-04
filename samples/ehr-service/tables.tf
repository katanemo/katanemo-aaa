resource "aws_dynamodb_table" "patientprofiles_table" {
  name           = var.patient_records_table_name
  billing_mode   = "PROVISIONED"
  read_capacity  = "30"
  write_capacity = "30"
  attribute {
    name = "patientId"
    type = "S"
  }
  hash_key = "patientId"
}

resource "aws_dynamodb_table" "diagnostics_table" {
  name           = var.diagnostics_table_name
  billing_mode   = "PROVISIONED"
  read_capacity  = "30"
  write_capacity = "30"
  attribute {
    name = "patientId"
    type = "S"
  }
  attribute {
    name = "reportId"
    type = "S"
  }
  hash_key = "patientId"
  range_key = "reportId"
}
