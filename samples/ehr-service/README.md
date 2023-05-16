# Overview
The follwing is a sample Serverless EHR SaaS service that uses Katanemo's rich identity and fine-grained authorization service to build privacy and safe collobration features.  The high-level architecture below captures the different inrastructure pieces of the sample EHR SaaS application and Katanemo's authorization components that deployed alongside our application resources in our AWS VPC.

<img src="https://github.com/katanemo/katanemo-aaa/blob/main/samples/ehr-service/saas_arch.png?raw=true" width="800">

# Key Components and Actors 

`EHR SaaS Service`: An OpenAPI based SaaS services that manages Patient and Diagnostic records via separate API-based microservices.
`AcmeHealth.io`: A provider facility that uses the EHR SaaS Service to store and manage patient records.

- The EHR SaaS service uses Katanemo to seamlessly onboard customers (e.g. AcmeHealth.io), and empowers its customers to define modern safety and privacy controls via self-service identity and access management tools offered by Katanemo.

# Pre-Requisites To Deploy EHR SaaS

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html): version aws-cli/2.11.15
- [AWS Cloud Development Kit (CDK)](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html): version 2.78.0 (build 8e95c37)
- [Docker](https://docs.docker.com/get-docker/): version 20.10.23
- [jq](https://stedolan.github.io/jq/download/): v1.6
- AWS Account

# Installation

Use following steps to install lambda authorizer that uses apigateway to authorize calls to EHR service,


1. Clone [katanemo/katanemo-aaa](https://github.com/katanemo/katanemo-aaa) repo and navigate to samples/ehr-service
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
3. Deploy Katanemo's Authentication Runtime Client (ARC), Lambda Authorizer, API Gateway and EHR SaaS Service using CDK
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
