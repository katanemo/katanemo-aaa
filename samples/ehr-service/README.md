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

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html): version aws-cli/2.11.15
- [AWS Cloud Development Kit (CDK)](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html): version 2.78.0 (build 8e95c37)
- [Docker](https://docs.docker.com/get-docker/): version 20.10.23
- [jq](https://stedolan.github.io/jq/download/): v1.6
- AWS Account

# Installation

Use following steps to install lambda authorizer that uses apigateay to authorize calls to EHR service,


1. Clone [katanemo/katanemo-aaa](https://github.com/katanemo/katanemo-aaa) repo and navigate to samples/ehr_service
    ```
    $ git clone git@github.com:katanemo/katanemo-aaa.git
    $ cd katanemo-aaa/samples/ehr-service
    ```
2. Add katutil to path
    ```
    $ export PATH=$PATH:`pwd`/../../cli/bin
    ```
    Ensure that katutil is working by typing in following
    > you may see `broken pipe` error which is due to docker, rerun should work fine
    ```
    $ katutil get-default-service | jq -r .serviceId
    ```
3. Deploy ARC and Katanemo using CD
   > Use account-email that you used when onboarding with katanemo. And complete service registration step to get service-id
    ```
    $ sh deploy.sh <katanemo-account-email> <service-id>
    ```

After deployment is complete you will see following new resources in your AWS account,

1. DynamoDb tables for patient and diagnostic records
2. Lambda authroizer
3. Lambda function to manage patient records
4. Lambda function to manage diagnostic records
5. Katanemo's ARC deployed as ECS service
6. API Gateway that uses lambda authorizer to protect patient and diagnostic REST API paths

To find out name of your API gateway issue following command,
```
$ aws cloudformation describe-stacks --stack-name ApiLambdaEhrService --query "Stacks[*].Outputs" --output json | jq '.[]' | jq '.[] | select(.OutputKey | test("patientRecordServiceEndpoint")) | .OutputValue' -r
```

To find out name of Katanemo's ARC Endpoint address use following command,

```
$ aws cloudformation describe-stacks --query "Stacks[*].Outputs" --output json | jq '.[]' | jq '.[] | select(.OutputKey | test("KatanemoArcServiceURL")) | .OutputValue' -r
```

# Cleanup

To remove all resources configured during this sample application issue following command,
```
$ sh cleanup.sh
```
