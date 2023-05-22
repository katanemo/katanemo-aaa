# Overview
The follwing project contains a sample Serverless EHR SaaS application that uses Katanemo's fully featured identity and fine-grained authorization service. With Katanemo developers can quickly add user and federated authentication to their applications, and build powerful privacy and collaboration features via Katanemo’s rich RBAC and ABAC capabilities

The high-level architecture below captures AWS infrastructure resources of our service, and Katanemo's authorization components deployed alongside our service.

<img src="https://github.com/katanemo/katanemo-aaa/blob/main/samples/ehr-service/saas_arch.png?raw=true" width="800">

# Key Components and Actors 

`EHR SaaS Service`: An OpenAPI based SaaS service that manages Patient and Diagnostic records via API-based microservices.

`AcmeHealth.io`: A provider facility (tenant) that uses the EHR SaaS service to store and manage Patient and Diagnostic records.

- The EHR SaaS service uses Katanemo to seamlessly onboard customers (e.g. AcmeHealth.io), and empowers its customers to define modern safety and privacy controls against its service, via self-service identity and access management tools offered by Katanemo.

# Pre-Requisites To Deploy EHR SaaS

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html): version aws-cli/2.11.15
- [AWS Cloud Development Kit (CDK)](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html): version 2.78.0 (build 8e95c37)
- [Docker](https://docs.docker.com/get-docker/): version 20.10.23
- [jq](https://stedolan.github.io/jq/download/): v1.5
- AWS Account

# Installation

Use following steps to install lambda authorizer that uses apigateway to authorize calls to EHR service

1. Clone [katanemo/katanemo-aaa](https://github.com/katanemo/katanemo-aaa) repo and navigate to samples/ehr-service
    ```bash
    git clone git@github.com:katanemo/katanemo-aaa.git
    cd katanemo-aaa/samples/ehr-service
    ```
2. Add katutil to path
    ```bash
    export PATH=$PATH:`pwd`/../../cli/bin
    ```
    Ensure that katutil is working by typing in following
    > on first run katutil will attempt to build docker container for katutil
    ```bash
    katutil get-default-service | jq -r .serviceId
    ```
3. Create a Katanemo [developer account](https://console.katanemo.com/sign-up), if you don't already have one. 

4. Create a Katanemo Service with the Katanemo CLI. 
   >First, retrive a token for your Katanemo developer account
   ```bash
   katanemo_aaa=$(katutil get-default-service | jq -r .serviceId)
   developer_token=$(katutil login-with-password --service_id $katanemo_aaa --email <katanemo-developer-account-email> --password <katanemo-developer-account-password> | jq -r .token)
   ```

   >Next, create a Katanemo Service via the init-service command. Note: the redirectURI is used to navigate users to a callback endpoint upon a successful login via Katanemo
   ```bash
    katutil init-service --service_name <service_name> --api_spec $(readlink -f ehr.yaml) --redirect_uri <callback_uri> --token $developer_token
   ```

5. Deploy Katanemo's Authentication Runtime Client (ARC), Lambda Authorizer, API Gateway and EHR SaaS Service using CDK
   > Use the email address with your Katanemo account. And complete service registration step to get service-id
    ```bash
    sh deploy.sh <katanemo-account-email> <service-id>
    ```

After deployment is complete you will see following new resources in your AWS account,

1. DynamoDb tables for patient and diagnostic records
2. Lambda authroizer
3. Lambda function to manage patient records
4. Lambda function to manage diagnostic records
5. Katanemo's ARC deployed as ECS service
6. API Gateway that uses lambda authorizer to protect patient and diagnostic REST API paths

To find out name of your API gateway issue following command,
```bash
aws cloudformation describe-stacks --stack-name ApiLambdaEhrService --query "Stacks[*].Outputs" --output json | jq '.[]' | jq '.[] | select(.OutputKey | test("patientRecordServiceEndpoint")) | .OutputValue' -r
```

To find out name of Katanemo's ARC Endpoint address use following command,

```bash
aws cloudformation describe-stacks --query "Stacks[*].Outputs" --output json | jq '.[]' | jq '.[] | select(.OutputKey | test("KatanemoArcServiceURL")) | .OutputValue' -r
```

# Cleanup

To remove all resources configured during this sample application issue following command,
```bash
sh cleanup.sh
```
