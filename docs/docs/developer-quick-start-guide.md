---
sidebar_position: 3
---

# Developer Quick Start Guide 

Katanemo supports an OpenAPI-based development workflow. You simply define RESTful APIs just like you would today via the [OpenAPI spec](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md), publish that spec to Katanemo and instantly add user/federated authentication to your application and build powerful privacy and collaboration features via Katanemo’s Role-based Access Control ([RBAC](https://en.wikipedia.org/wiki/Role-based_access_control)), Attribute-based Access Control ([ABAC](https://en.wikipedia.org/wiki/Attribute-based_access_control)) and [Resource-based Access Control](https://en.wikipedia.org/wiki/Access-control_list). Katanemo offers a holistic approach to identity, privacy, and safe collaboration that empowers developers to focus on what matters most: moving fast in building features and capabilities unique to their business.

## **Step 1: Create a Service in Katanemo via your OpenAPI service specification**


To get started, you must have a Katanemo account. If you don’t already have one, visit the [Katanemo signup page](https://console.katanemo.com/sign-up) to register with Katanemo. You are now ready to publish your [OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md) spec to Katanemo, and in minutes create self-service on-boarding workflows, powerful authorization and auditing capabilities for your SaaS application.

![service-dashboard.png](..%2Fstatic%2Fimg%2Fservice-dashboard.png)

1. Give your service a name, a description and configure a _redirect_uri_ where Katanemo redirects users upon a successful sign-up/log-in attempt.
2. Click **Publish** to create a Katanemo Service.
3. Copy the **Sign-Up/Login** **URL**s generated by Katanemo. You will need to add these links to your website so that your customers can easily sign-up and login to your SaaS application.

## **Step 2: Integrate the Katanemo SDK for authentication and authorization.**

Once you have registered your service with Katanemo, you can use the Katanemo SDK to perform authorization and authentication. To get started:




1. Sign in to the [Katanemo SaaS developer console](https://console.katanemo.com/service), and choose **Create New [Keys](./concepts/keys)**. _Note_: a client key is bound (by default) to a default role that can perform all Katanemo API actions. For more information on roles, see [Roles](./concepts/roles).


2. Use the Katanemo SDK to enforce authentication and authorization for your SaaS application. The sample python code below shows how you can add authentication and fine-grained authorization via a few line of code.
```python
# Katanemo Authentication

import http
import os
from katanemo_sdk import arc

def init():
    api_key = os.getenv("KATANEMO_CLIENT_KEY")
    api_key_secret = os.getenv("KATANEMO_CLIENT_SECRET")
    service_id = os.getenv("KATANEMO_SERVICE_ID")
    arc.configure(api_key, api_key_secret, service_id)

def authorize(request: http.Request, next_handler: http.Handler):
    response, error = arc.authorize(request)
    if error is not None:
        # Handle authentication and authorization error
        return response
    return next_handler

```