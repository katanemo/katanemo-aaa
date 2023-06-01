---
sidebar_position: 1
---

# How to Integrate the Katanemo SDK in your application (Authorization Runtime Client)?

Katanemo’s Authorization Runtime Client (ARC) is the leight-weight utility that does the intelligent heavy lifting of protecting who can do what on which resource (authorization). As a developer, you can configure ARC at the gateway layer of your SaaS (API) service in minutes. Katanemo offers two primary integration points with varying levels of support to suit your specific environment needs.

```python
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
#### 1. Using the Katanemo SDK
You can use the Katanemo SDK and embed that in your code (as shown below) to authorize calls that hit your front-end servers. In the code below, ARC will look for and validate the JWT Bearer Token, extract Role details for the authorization principal, and perform authorization. Katanemo’s SDK will make calls to the closest region by looking at the host headers of the HTTP request, and makes all authorization calls to its cloud service over a highly secure TLS 1.3 connection.


_Configure AWS Private Link (interface endpoint) with Katanemo_

Katanemo also supports [AWS Private Link](https://aws.amazon.com/privatelink/) for workloads hosted in AWS where authorization traffic should not go over the internet. There is no additional charge for using Private Link with Katanemo. Once configured correctly, authorization traffic between your VPC  and the Katanemo endpoint service traverses through the AWS backbone. Follow the steps below to configure AWS Private Link with Katanemo. _Note: Configuring an AWS Private Link interface endpoint must be done via VPC, Subnet, Security Group semantics (vs OpenAPI RESTful semantics) -🤮 we have made our friends at AWS aware of our feelings here._

To configure the use of AWS Private Link with Katanemo, first navigate to the Katanemo Service Console and select the **_Service_** that you are interested to enable Private Link support for. Next select **_Client Keys _**from the left hand menu, and then click on the **_“AWS Private Link”_** tab on the top of that page. Here you will be asked to provide your AWS account id ( used for permissions), select the region where you’d like Private Link turned on, and AZs from which traffic will originate from your side to Katanemo’s endpoint service. Click **save**, and in a few moments will get an _endpoint interface id_ and a _private DNS name_ that you will use to [create an interface endpoint ](https://docs.aws.amazon.com/vpc/latest/privatelink/interface-endpoints.html)in your AWS account.

Today, Katanemo supports Private Link in the us-east-1, us-east-2 and the us-west-1 regions, and is deployed in three AZs in each of those regions. When selecting an AZ make sure that the AZ id where Katanemo hosts its’ endpoint service matches the AZ id where traffic will originate from your VPC, else you’ll fail to [create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in AWS.

Now, log in to the AWS management console, and follow steps in their guide to create an [interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html). Make sure that you select “**Service Defined” **for the **DNS record IP type** and for “Service Name” use the endpoint interface id that you got from the previous step above. _Note_, Katanemo accepts all interface endpoint connections and manages permissions to its endpoint interface via the AWS account id that you configured in the Katanemo Service Console.

#### 2. Integrated as part of Amazon API Gateway or NGINX servers or Envoy Proxy 

MISSING SECTION?

