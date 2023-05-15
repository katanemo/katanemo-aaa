# Overview
Sample EHR application that uses katanemo's aaa stack to provide seamless authentication, authorization and attestation service. This sample application uses lambda authorizer to authenticate calls to EHR service. Here is how different services are interacting with each other,

<img src="https://github.com/katanemo/katanemo-aaa/blob/main/samples/ehr-service/saas_arch.png?raw=true" width="800">

Following are main components in this sample application,

`EHR SaaS Service`: An OpenAPI based services that manages patiend records. It exposes following endpoints,

- POST:/patient
- PUT:/patient/{patientId}
- GET:/patient/{patientId}
- POST:/diagnostic
- PUT:/diagnostic/{diagnosticId}
- GET:/diagnostic/{diagnosticId}

`AcmeHealth.io`: A health provider that uses EHR SaaS Service to store patient records.

- EHR SaaS Service uses Katanemo's AAA stack to allow its subscribers (e.g. AcmeHealth.io) to onboard seamlessly.

# Requirements

- AWS CLI: version aws-cli/2.11.15
- AWS Cloud Development Kit (CDK): version 2.78.0 (build 8e95c37)
- Docker: version 20.10.23
- jq: v1.6
- AWS Account

# Installation

Using following commands to install lambda authorizer that uses apigateay to install in your account,

1. Add katutil to path
```
$ export PATH=$PATH:`pwd`/../../cli/bin
```

Ensure that katutil is working by typing in following
```
$ katutil get-default-service | jq -r .serviceId
```

2. Deploy ARC and Katanemo using CDK

```
$ sh deploy.sh <katanemo-account-email> <service-id>
```

Note after deployment is complete you will see following new resources in AWS account,

1. ddb tables for patient and diagnost records
2. lambda authroizer
3. lambda function to manage patient records
4. lambda function to manage diagnostic records
5. api gateway that uses lambda authorizer to protect patient and diagnostic REST API paths
6. ARC deployed as ecs service

To find out name of your API gateway issue following command,

```
$ aws cloudformation describe-stacks --stack-name ApiLambdaEhrService --query "Stacks[*].Outputs" --output json | jq '.[]' | jq '.[] | select(.OutputKey | test("patientRecordServiceEndpoint")) | .OutputValue' -r
```

To find out name of Katanemo's ARC Endpoint address use following command,

```
$ aws cloudformation describe-stacks --query "Stacks[*].Outputs" --output json | jq '.[]' | jq '.[] | select(.OutputKey | test("KatanemoArcServiceURL")) | .OutputValue' -r
```
