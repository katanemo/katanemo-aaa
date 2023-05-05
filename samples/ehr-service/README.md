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
- AWS Account
- jq

# Setup

- Add katanemo's katutil to path.
```
$ export PATH=$PATH:$PWD/../../cli/bin
```

- Signup EHR SaaS Service's admin to Katanemo
```
➜  ehr-service git:(main) ~ sh ehr_admin_signup.sh adil+ehr_admin@katanemo.com
2023-05-04T16:38:13-0700  -  === signing up ehr admin to katanemo ===
enter code sent to adil+ehr_admin@katanemo.com
xxxxxx
2023-05-04T16:38:32-0700  -  === ehr admin adil+ehr_admin@katanemo.com signed up to katanemo with accountId xxxx ===
2023-05-04T16:38:32-0700  -  === clinet id (xxx) and client secret (XXXX) created to interact with katanemo api ===
```

- Initialize EHR SaaS Service's OpenApi service with Katanemo

```
➜  ehr-service git:(main) ~ sh ehr_service_init.sh ehr.yaml
2023-05-04T16:41:35-0700  -  === initializing service ===
2023-05-04T16:41:37-0700  -  === patients record service initialized with katanemo xxxx ===
➜  ehr-service git:(main) ~
```

- Onboard AchmeHealth with EHR SaaS Service's patient record service

```
➜  ehr-service git:(main) ~ sh signup-subscriber.sh adil+achmehealth_admin@katanemo.com adil+achmehealth_doctor@katanemo.com
2023-05-04T16:43:22-0700  -  === signing up subscriber to katanemo ===
enter code sent to adil+achmehealth_admin@katanemo.com
xxx
2023-05-04T16:43:37-0700  -  === adding doctor account ===
enter code sent to adil+achmehealth_doctor@katanemo.com
xxx
2023-05-04T16:43:50-0700  -  === subscribed adil+achmehealth_admin@katanemo.com to xxx with accountId xxx ===
2023-05-04T16:43:50-0700  -  === added doctor account adil+achmehealth_doctor@katanemo.com with roleId xxx  ===
➜  ehr-service git:(main) ~
```
