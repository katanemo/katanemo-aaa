# Overview
Sample EHR application that uses katanemo's aaa stack to provide seamless authentication, authorization and attestation service.

Following are main applications and their roles in this sample code,

`AcmeHealth.io`: An OpenAPI based services that manages patiend records. It exposes following endpoints,

- POST:/patient
- PUT:/patient/{patientId}
- GET:/patient/{patientId}
- POST:/diagnostics
- PUT:/diagnostics/{diagnosticsId}
- GET:/diagnostics/{diagnosticsId}

`HealWell Clinic`: A health provider that uses AcmeHealth.io to store patient records.

AcmeHealth.io uses Katanemo's AAA stack to allow its subscribers (e.g. HealthWell Clinic) to onboard seamlessly.

TODO: Add more details

## Architecture

This sample application uses lambda authorizer to authenticate calls to EHR service. Here is how different services are interacting with each other,

```
AcmeHealth.io --- HealthWell Clinic
    |
    |
Lambda Authorizer
    |
    |
Katanemo AAA
```

# Requirements

- Docker
- Terraform
- AWS Account

# Setup

- Add katanemo's katutil to path.
```
$ export PATH=$PATH:$PWD/../../cli/bin
```

- Signup AcmeHealth's admin to Katanemo
```
➜  ehr-service git:(main) ~ sh ehr_admin_signup.sh adil+acmehealthadmin@katanemo.com
2023-05-04T16:38:13-0700  -  === signing up ehr admin to katanemo ===
enter code sent to adil+acmehealthadmin@katanemo.com
xxxxxx
2023-05-04T16:38:32-0700  -  === ehr admin adil+acmehealthadmin@katanemo.com signed up to katanemo with accountId xxxx ===
2023-05-04T16:38:32-0700  -  === clinet id (xxx) and client secret (XXXX) created to interact with katanemo api ===
```

- Initialize AchmeHealth's service with Katanemo

```
➜  ehr-service git:(main) ~ sh ehr_service_init.sh ehr.yaml
2023-05-04T16:41:35-0700  -  === initializing service ===
2023-05-04T16:41:37-0700  -  === patients record service initialized with katanemo xxxx ===
➜  ehr-service git:(main) ~
```

- Onboard HealthWell Clinic with AcmeHealth's patient record service

```
➜  ehr-service git:(adil/ehr_sammple) ~ sh signup-subscriber.sh adil+healthwell_admin@katanemo.com adil+healthwell_doctor@katanemo.com
2023-05-04T16:43:22-0700  -  === signing up subscriber to katanemo ===
enter code sent to adil+healthwell_admin@katanemo.com
xxx
2023-05-04T16:43:37-0700  -  === adding doctor account ===
enter code sent to adil+healthwell_doctor@katanemo.com
xxx
2023-05-04T16:43:50-0700  -  === subscribed adil+healthwell_admin@katanemo.com to xxx with accountId xxx ===
2023-05-04T16:43:50-0700  -  === added doctor account adil+healthwell_doctor@katanemo.com with roleId xxx  ===
➜  ehr-service git:(adil/ehr_sammple) ~
```
