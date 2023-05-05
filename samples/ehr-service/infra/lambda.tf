module "aws_lambda_auth" {
	source = "terraform-aws-modules/lambda/aws"
	version = "~> 2.5"

	function_name = local.authorizer_name
	handler = "index.handler"
	runtime = "nodejs18.x"
	source_path = [
		{
			commands = ["npm install", ":zip"]
			path = "${path.module}/../lambda/auth",
			patterns = [
				"!.*", // * Exclude everything
				"index.js",
				"node_modules/.+", // * Add all non-empty directories and files in /node_modules/
				"package-lock.json",
				"package.json",
			]
		},
	]
  environment_variables = {
    AUTH_ENDPOINT = "https://auth.us-west-2.katanemo.dev"
  }
}

resource "aws_lambda_permission" "apigw_lambda_auth" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = "${local.authorizer_name}"
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_rest_api.patient_records_api.execution_arn}/*/*"
}

module "aws_lambda_patient_service" {
	source = "terraform-aws-modules/lambda/aws"
	version = "~> 2.5"

	function_name = local.patient_service
	handler = "index.handler"
	runtime = "nodejs18.x"
	source_path = [
		{
			commands = ["npm install", ":zip"]
			path = "${path.module}/../lambda/patients",
			patterns = [
				"!.*", // * Exclude everything
				"index.js",
				"node_modules/.+", // * Add all non-empty directories and files in /node_modules/
				"package-lock.json",
				"package.json",
			]
		},
	]
  environment_variables = {
    PATIENTS_TABLE_NAME = var.patient_records_table_name
  }
  attach_policy_statements = true
  policy_statements = {
    dynamodb = {
      effect    = "Allow",
      actions   = ["dynamodb:*"],
      resources = ["arn:aws:dynamodb:${local.region}:${local.account_id}:table/${var.patient_records_table_name}"]
    },
  }
}

resource "aws_lambda_permission" "apigw_patient_service" {
  statement_id  = "AllowAPIGatewayInvoke1"
  action        = "lambda:InvokeFunction"
  function_name = "${module.aws_lambda_patient_service.lambda_function_name}"
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_rest_api.patient_records_api.execution_arn}/*/*"
}


module "aws_lambda_diagnostics_service" {
	source = "terraform-aws-modules/lambda/aws"
	version = "~> 2.5"

	function_name = local.diagnostics_service
	handler = "index.handler"
	runtime = "nodejs18.x"
	source_path = [
		{
			commands = ["npm install", ":zip"]
			path = "${path.module}/../lambda/diagnostics",
			patterns = [
				"!.*", // * Exclude everything
				"index.js",
				"node_modules/.+", // * Add all non-empty directories and files in /node_modules/
				"package-lock.json",
				"package.json",
			]
		},
	]
  environment_variables = {
    DIAGNOSTICS_TABLE_NAME = var.diagnostics_table_name
  }
  attach_policy_statements = true
  policy_statements = {
    dynamodb = {
      effect    = "Allow",
      actions   = ["dynamodb:*"],
      resources = ["arn:aws:dynamodb:${local.region}:${local.account_id}:table/${var.diagnostics_table_name}"]
    },
  }
}

resource "aws_lambda_permission" "apigw_diagnostics_service" {
  statement_id  = "AllowAPIGatewayInvoke1"
  action        = "lambda:InvokeFunction"
  function_name = "${module.aws_lambda_diagnostics_service.lambda_function_name}"
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_rest_api.patient_records_api.execution_arn}/*/*"
}
