resource "aws_dynamodb_table" "patientrecords_table" {
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

resource "aws_dynamodb_table" "diagnostic_table" {
  name           = var.diagnostic_table_name
  billing_mode   = "PROVISIONED"
  read_capacity  = "30"
  write_capacity = "30"
  attribute {
    name = "diagnosticId"
    type = "S"
  }
  hash_key = "diagnosticId"
}
