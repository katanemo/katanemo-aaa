resource "aws_api_gateway_rest_api" "patient_records_api" {
  name = "patient-records-apigw"
  body = jsonencode({
    openapi = "3.0.1"
    info = {
      title   = "patient-records-gateway"
      version = "1.0"
    }
    "x-amazon-apigateway-api-key-source" = "AUTHORIZER"
    paths = {
      "/patient" = {
        post = {
          security : [
            {
              katanemo-authorizer : []
            }
          ]
          x-amazon-apigateway-integration = {
            httpMethod           = "POST"
            payloadFormatVersion = "1.0"
            type                 = "AWS_PROXY"
            uri                  = "arn:aws:apigateway:${data.aws_region.current.name}:lambda:path/2015-03-31/functions/arn:aws:lambda:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:function:${local.patient_service}/invocations"
          }
        }
      },
      "/patient/{patientId}" = {
        get = {
          security : [
            {
              katanemo-authorizer : []
            }
          ]
          x-amazon-apigateway-integration = {
            httpMethod           = "POST"
            payloadFormatVersion = "1.0"
            type                 = "AWS_PROXY"
            uri                  = "arn:aws:apigateway:${data.aws_region.current.name}:lambda:path/2015-03-31/functions/arn:aws:lambda:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:function:${local.patient_service}/invocations"
          }
        }
      },
      "/diagnosticreport" = {
        post = {
          security : [
            {
              katanemo-authorizer : []
            }
          ]
          x-amazon-apigateway-integration = {
            httpMethod           = "POST"
            payloadFormatVersion = "1.0"
            type                 = "AWS_PROXY"
            uri                  = "arn:aws:apigateway:${data.aws_region.current.name}:lambda:path/2015-03-31/functions/arn:aws:lambda:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:function:${local.patient_service}/invocations"
          }
        }
      },
      "/diagnosticreport/patientId/{patientId}/reportId/{reportId}" = {
        get = {
          security : [
            {
              katanemo-authorizer : []
            }
          ]
          x-amazon-apigateway-integration = {
            httpMethod           = "POST"
            payloadFormatVersion = "1.0"
            type                 = "AWS_PROXY"
            uri                  = "arn:aws:apigateway:${data.aws_region.current.name}:lambda:path/2015-03-31/functions/arn:aws:lambda:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:function:${local.patient_service}/invocations"
          }
        }
      }    }
    components = {
      securitySchemes = {
        katanemo-authorizer = {
          type                         = "apiKey",        // Required and the value must be "apiKey" for an API Gateway API.
          name                         = "Authorization", // The name of the header containing the authorization token.
          in                           = "header",        // Required and the value must be "header" for an API Gateway API.
          x-amazon-apigateway-authtype = "custom",        // Specifies the authorization mechanism for the client.
          x-amazon-apigateway-authorizer = {              // An API Gateway Lambda authorizer definition
            authorizerUri = "arn:aws:apigateway:${data.aws_region.current.name}:lambda:path/2015-03-31/functions/arn:aws:lambda:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:function:${local.authorizer_name}/invocations",
            # authorizerCredentials : "arn:aws:iam::account-id:role",
            # identityValidationExpression : "^x-[a-z]+",
            # TODO: put caching back
            authorizerResultTtlInSeconds : 1
            type : "token",                               // Required property and the value must "token"
          }
        }
      }
    }
  })

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

resource "aws_api_gateway_deployment" "patient_records_deployment" {
  rest_api_id = aws_api_gateway_rest_api.patient_records_api.id

  triggers = {
    redeployment = sha1(jsonencode(aws_api_gateway_rest_api.patient_records_api.body))
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_api_gateway_stage" "patient_records_stage" {
  deployment_id = aws_api_gateway_deployment.patient_records_deployment.id
  rest_api_id   = aws_api_gateway_rest_api.patient_records_api.id
  stage_name    = "staging"
}

resource "aws_api_gateway_method_settings" "patient_records_stage_settings" {
  rest_api_id = "${aws_api_gateway_rest_api.patient_records_api.id}"
  stage_name  = "${aws_api_gateway_stage.patient_records_stage.stage_name}"
  method_path = "*/*"
  settings {
    logging_level = "INFO"
    data_trace_enabled = true
    metrics_enabled = true
  }
}
