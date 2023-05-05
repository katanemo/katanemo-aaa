terraform {
	required_version = "~> 1.0"

	required_providers {
		aws = {
			source = "hashicorp/aws"
			version = "~> 3.0"
		}
	}
}

provider "aws" {
	region = "us-west-1"
}

data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

locals {
  authorizer_name = "katanemo-lambda-auth"
  patient_service = "patient-service"
  diagnostics_service = "diagnostics-service"
  region = data.aws_region.current.name
  account_id = data.aws_caller_identity.current.account_id
}
