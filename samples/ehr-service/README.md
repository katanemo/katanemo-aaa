# Overview
Sample EHR application that uses katanemo's aaa stack to provide seamless authentication, authorization and attestation service.

Following are main applications and their roles in this sample code,

`EHR SaaS Service`: An OpenAPI based services that manages patiend records. It exposes following endpoints,

- POST:/patient
- PUT:/patient/{patientId}
- GET:/patient/{patientId}
- POST:/diagnostics
- PUT:/diagnostics/{diagnosticsId}
- GET:/diagnostics/{diagnosticsId}

`AcmeHealth.io`: A health provider that uses EHR SaaS Service to store patient records.

EHR SaaS Service uses Katanemo's AAA stack to allow its subscribers (e.g. AcmeHealth.io) to onboard seamlessly.

TODO: Add more details

## Architecture

This sample application uses lambda authorizer to authenticate calls to EHR service. Here is how different services are interacting with each other,



<img src="https://github.com/katanemo/katanemo-aaa/blob/main/samples/ehr-service/saas_arch.png?raw=true" width="800">


# Requirements

- Docker: version 20.10.23
- Terraform: version v1.4.6
- jq: v1.6
- AWS Account

# Setup

- Add katanemo's katutil to path.
```
$ export PATH=$PATH:$PWD/../../cli/bin
```

- Signup EHR SaaS Service's admin to Katanemo
```
➜  ehr-service git:(main) ✗ sh ehr_admin_signup.sh adil+ehr_admin1a@katanemo.com
2023-05-04T22:30:32-0700  -  === signing up ehr admin to katanemo ===
2023-05-04T22:30:32-0700  -  katutil signup-service --service_id gq9rmqgtf --email adil+ehr_admin1a@katanemo.com
2023-05-04T22:30:35-0700  -  enter code sent to adil+ehr_admin1a@katanemo.com
SNqD7ow0zChR
2023-05-04T22:30:43-0700  -  katutil confirm-and-set-password --code SNqD7ow0zChR --service_id gq9rmqgtf --account_id wfb5cprzc --email adil+ehr_admin1a@katanemo.com --password xxxx
2023-05-04T22:30:46-0700  -  === ehr admin adil+ehr_admin1a@katanemo.com signed up to katanemo with accountId wfb5cprzc ===
2023-05-04T22:30:46-0700  -  === clinet id (d7ui3507kousl2r93lt0n9rqo) and client secret (XXXX) created to interact with katanemo api ===
```

- Initialize EHR SaaS Service's OpenApi service with Katanemo

```
➜  ehr-service git:(main) ✗ sh ehr_service_init.sh ehr.yaml
2023-05-04T22:31:02-0700  -  === initializing service ===
2023-05-04T22:31:02-0700  -  getting token for ehr admin
2023-05-04T22:31:02-0700  -  katutil login-with-password --service_id gq9rmqgtf --email adil+ehr_admin1a@katanemo.com --password 7TOfroc9aab3$
2023-05-04T22:31:03-0700  -  registering service with api spec ehr.yaml to katanemo
2023-05-04T22:31:03-0700  -  katutil init-service --service_name patient records service --api_spec /Users/adilhafeez/src/katanemo-aaa/samples/ehr-service/ehr.yaml --redirect_uri www.google.com --token XXXXX
2023-05-04T22:31:04-0700  -  === patients record service initialized with katanemo kud6r8zd7 ===
```

- Onboard AchmeHealth with EHR SaaS Service's patient record service

```
➜  ehr-service git:(main) ✗ sh signup-subscriber.sh adil+acmeheathl_admin1@katanemo.com adil+acmehealth_doctor1@katanemo.com
2023-05-04T22:31:18-0700  -  === signing up subscriber to katanemo ===
2023-05-04T22:31:18-0700  -  signing up subscriber adil+acmeheathl_admin1@katanemo.com to kud6r8zd7
2023-05-04T22:31:18-0700  -  katutil signup-service --email adil+acmeheathl_admin1@katanemo.com --service_id kud6r8zd7
2023-05-04T22:31:21-0700  -  enter code sent to adil+acmeheathl_admin1@katanemo.com
CyL8xJgeja3B
2023-05-04T22:31:33-0700  -  katutil confirm-and-set-password --code CyL8xJgeja3B --email adil+acmeheathl_admin1@katanemo.com --service_id kud6r8zd7 --password xxxx --account_id e36xmc2fd
2023-05-04T22:31:34-0700  -  getting token for subscriber adil+acmeheathl_admin1@katanemo.com
2023-05-04T22:31:34-0700  -  katutil login-with-password --service_id kud6r8zd7 --email adil+acmeheathl_admin1@katanemo.com --password xxxx
2023-05-04T22:31:35-0700  -  === adding doctor account ===
2023-05-04T22:31:35-0700  -  adding doctor account adil+acmehealth_doctor1@katanemo.com
2023-05-04T22:31:35-0700  -  katutil add-user --account_id e36xmc2fd --email adil+acmehealth_doctor1@katanemo.com --token xxxx --tags {"function": ["doctor"]}
2023-05-04T22:31:36-0700  -  enter code sent to adil+acmehealth_doctor1@katanemo.com
6Patk2zgtnlP
2023-05-04T22:31:44-0700  -  katutil confirm-and-set-password --account_id e36xmc2fd --email adil+acmehealth_doctor1@katanemo.com --code 6Patk2zgtnlP --service_id kud6r8zd7 --password xxxx --account_id e36xmc2fd
2023-05-04T22:31:46-0700  -  creating role with access to patient record
2023-05-04T22:31:46-0700  -  katutil create-role --policies [{"allow": ["GET:/patient/{patientId}", "PUT:/patient/{patientId}"], "where": "$principalTags:function = doctor"}, {"allow": ["POST:/diagnostics/", "GET:/diagnostics/{diagnosticsId}"], "where": "$principalTags:function = doctor"}] --account_id e36xmc2fd --service_id kud6r8zd7 --role_name patient record doctor access --token xxxx
2023-05-04T22:31:46-0700  -  assigning doctor role to doctor account
2023-05-04T22:31:46-0700  -  katutil assign-role --principal_id adil+acmehealth_doctor1@katanemo.com --role_id a33f5fq87 --token xxxx
2023-05-04T22:31:47-0700  -  === subscribed adil+acmeheathl_admin1@katanemo.com to kud6r8zd7 with accountId e36xmc2fd ===
2023-05-04T22:31:47-0700  -  === added doctor account adil+acmehealth_doctor1@katanemo.com with roleId a33f5fq87  ===
```
