# Overview
Sample EHR application that uses katanemo's aaa stack to provide seamless authentication, authorization and attestation service.

Following are main applications and their roles in this sample code,

`EHR SaaS Service`: An OpenAPI based services that manages patiend records. It exposes following endpoints,

- POST:/patient
- PUT:/patient/{patientId}
- GET:/patient/{patientId}
- POST:/diagnostic
- PUT:/diagnostic/{diagnosticId}
- GET:/diagnostic/{diagnosticId}

`AcmeHealth.io`: A health provider that uses EHR SaaS Service to store patient records.

EHR SaaS Service uses Katanemo's AAA stack to allow its subscribers (e.g. AcmeHealth.io) to onboard seamlessly.

TODO: Add more details

## Architecture

This sample application uses lambda authorizer to authenticate calls to EHR service. Here is how different services are interacting with each other,

<img src="https://github.com/katanemo/katanemo-aaa/blob/main/samples/ehr-service/saas_arch.png?raw=true" width="800">

# Requirements

- AWS CLI: version aws-cli/2.11.15
- AWS Cloud Development Kit (CDK): version 2.78.0 (build 8e95c37)
- Docker: version 20.10.23
- jq: v1.6
- AWS Account

# Installation

Using following commands to install lambda authorizer that uses apigateay to install in your account,

1. bootstrap CDK

```
$ cdk bootstrap
```

2. build and deploy lambda authorizer along with requried resources to default account

```
$ cdk deploy
```

Note after deployment is complete you will see following new resources in AWS account,

1. ddb tables for patient and diagnost records
2. lambda authroizer
3. lambda function to manage patient records
4. lambda function to manage diagnostic records
5. api gateway that uses lambda authorizer to protect patient and diagnostic REST API paths

To find out name of your API gateway issue following command,

```
$ aws cloudformation describe-stacks --stack-name ApiLambdaEhrService --query "Stacks[*].Outputs" --output json | jq '.[]' | jq '.[] | select(.OutputKey | test("patientRecordServiceEndpoint")) | .OutputValue' -r
```

# Installation (Terraform)

Please refer to [tf_infra/README.md](tf_infra/README.md) file

# Testing

- Signup EHR SaaS Service's admin to Katanemo
```
$ sh ehr_admin_signup.sh <ehr_admin_email>
```

Note: you would need to enter correct email address so you can receive confirmation codes.

- Initialize EHR SaaS Service's OpenApi service with Katanemo
```
$ sh ehr_service_init.sh ehr.yaml
```

- Onboard AchmeHealth with EHR SaaS Service's patient record service
```
$ sh signup-subscriber.sh <ache_health_admin_email> <acme_health_doctor_email> <acme_health_receptionist_email>
```

# Validation

Run validate.sh script to ensure that,

1. receptionist cannot create patient account
2. doctor cannot create patient account
3. acmehealth admin can create patient account
4. receptionist cannot read patient account
5. doctor can read patient account
6. acmehealth admin can read patient account
## Detailed run of these three commands
```
➜  ehr-service git:(main) ✗ sh ehr_admin_signup.sh adil+ehr_admin3a@katanemo.com
2023-05-06T16:18:32-0700  -  === signing up ehr admin to katanemo ===
2023-05-06T16:18:32-0700  -  katutil signup-service --service_id gq9rmqgtf --email adil+ehr_admin3a@katanemo.com
2023-05-06T16:18:35-0700  -  enter code sent to adil+ehr_admin3a@katanemo.com
8hwomTMLOkxH
2023-05-06T16:18:41-0700  -  katutil confirm-and-set-password --code 8hwomTMLOkxH --service_id gq9rmqgtf --account_id snt99bnb4 --email adil+ehr_admin3a@katanemo.com --password xxxx
2023-05-06T16:18:45-0700  -  === ehr admin adil+ehr_admin3a@katanemo.com signed up to katanemo with accountId snt99bnb4 ===
2023-05-06T16:18:45-0700  -  === clinet id (4gnccl17s4ia1pvlpt2nq7t9jl) and client secret (XXXX) created to interact with katanemo api ===


➜  ehr-service git:(main) ✗ sh ehr_service_init.sh ehr.yaml
2023-05-06T16:18:49-0700  -  === initializing service ===
2023-05-06T16:18:49-0700  -  getting token for ehr admin
2023-05-06T16:18:49-0700  -  katutil login-with-password --service_id gq9rmqgtf --email adil+ehr_admin3a@katanemo.com --password 7TOfroc9aab3$
2023-05-06T16:18:50-0700  -  registering service with api spec ehr.yaml to katanemo
2023-05-06T16:18:50-0700  -  katutil init-service --service_name patient records service --api_spec /Users/adilhafeez/src/katanemo-aaa/samples/ehr-service/ehr.yaml --redirect_uri www.google.com --print_output True --token XXXXX
2023-05-06 23:18:51,380 INFO -
2023-05-06 23:18:51,381 INFO - Successfully Created Service ✅
2023-05-06 23:18:51,381 INFO - Your Service ID is: zn3kxjf9d
2023-05-06 23:18:51,381 INFO - Katanemo's hosted Sign-up/Login URL for your service: https://console.us-west-2.katanemo.dev/CreateAccount?serviceId=zn3kxjf9d
2023-05-06 23:18:51,381 INFO - Katanemo's Console to manage your customers https://console.us-west-2.katanemo.dev/sign-up/3xA
2023-05-06 23:18:51,381 INFO -
2023-05-06T16:18:51-0700  -  === patients record service initialized with katanemo zn3kxjf9d ===


➜  ehr-service git:(main) ✗ sh signup-subscriber.sh adil+acmehealth_admin@katanemo.com adil+acmehealth_doctor@katanemo.com adil+acmehealth_receptionist@katanemo.com
2023-05-06T16:18:55-0700  -  === signing up subscriber to katanemo ===
2023-05-06T16:18:55-0700  -  signing up subscriber adil+acmehealth_admin@katanemo.com to zn3kxjf9d
2023-05-06T16:18:55-0700  -  katutil signup-service --email adil+acmehealth_admin@katanemo.com --service_id zn3kxjf9d
2023-05-06T16:18:58-0700  -  enter code sent to adil+acmehealth_admin@katanemo.com
KP65pwZCcqUM
2023-05-06T16:19:05-0700  -  katutil confirm-and-set-password --code KP65pwZCcqUM --email adil+acmehealth_admin@katanemo.com --service_id zn3kxjf9d --password xxxx --account_id kgjh8d7fr
2023-05-06T16:19:07-0700  -  getting token for subscriber adil+acmehealth_admin@katanemo.com
2023-05-06T16:19:07-0700  -  katutil login-with-password --service_id zn3kxjf9d --email adil+acmehealth_admin@katanemo.com --password xxxx
2023-05-06T16:19:08-0700  -  === adding doctor account ===
2023-05-06T16:19:08-0700  -  adding doctor account adil+acmehealth_doctor@katanemo.com
2023-05-06T16:19:08-0700  -  katutil add-user --account_id kgjh8d7fr --email adil+acmehealth_doctor@katanemo.com --token xxxx --tags {"function": ["doctor"]}
2023-05-06T16:19:09-0700  -  enter code sent to adil+acmehealth_doctor@katanemo.com
3SxxO4ueKwAi
2023-05-06T16:19:18-0700  -  katutil confirm-and-set-password --account_id kgjh8d7fr --email adil+acmehealth_doctor@katanemo.com --code 3SxxO4ueKwAi --service_id zn3kxjf9d --password xxxx
2023-05-06T16:19:20-0700  -  creating role with access to patient record
2023-05-06T16:19:20-0700  -  katutil create-role --policies [{"allow": ["GET:/patient/{patientId}", "PUT:/patient/{patientId}"], "where": "$principalTags:function = doctor"}, {"allow": ["POST:/diagnostic", "GET:/diagnostic/{diagnosticId}"], "where": "$principalTags:function = doctor"}] --account_id kgjh8d7fr --service_id zn3kxjf9d --role_name patient record doctor access --token xxxx
2023-05-06T16:19:21-0700  -  assigning doctor role to doctor account
2023-05-06T16:19:21-0700  -  katutil assign-role --principal_id adil+acmehealth_doctor@katanemo.com --role_id fen8zseww --token xxxx
2023-05-06T16:19:21-0700  -  adding receptionist account adil+acmehealth_receptionist@katanemo.com
2023-05-06T16:19:21-0700  -  katutil add-user --account_id kgjh8d7fr --email adil+acmehealth_receptionist@katanemo.com --token xxxx --tags {"function": ["doctor"]}
2023-05-06T16:19:22-0700  -  enter code sent to adil+acmehealth_receptionist@katanemo.com
A8tjcTV0RrDS
2023-05-06T16:19:30-0700  -  katutil confirm-and-set-password --account_id kgjh8d7fr --email adil+acmehealth_receptionist@katanemo.com --code A8tjcTV0RrDS --service_id zn3kxjf9d --password xxxx
2023-05-06T16:19:32-0700  -  assigning user role to receptionist account
2023-05-06T16:19:32-0700  -  katutil assign-role --principal_id adil+acmehealth_receptionist@katanemo.com --role_id ct25jna3r --token xxxx
2023-05-06T16:19:33-0700  -  === subscribed adil+acmehealth_admin@katanemo.com to zn3kxjf9d with accountId kgjh8d7fr ===
2023-05-06T16:19:33-0700  -  === added doctor account adil+acmehealth_doctor@katanemo.com with roleId fen8zseww  ===```
```
