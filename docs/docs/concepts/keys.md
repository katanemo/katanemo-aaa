---
sidebar_position: 7
---

# Keys

Client Keys consist of an identifier, and a secret value used to identify client machines. APIs can be consumed in three primary ways: 

1. Users accessing APIs over a UI experience
2. 3rd party developers accessing User resources via OAuth2.0
3. Client machines performing API operations where a User is not present. 

For the latter two scenarios, Client Keys enable API developers to perform machine authentication, authorization and auditing (3xA). The key lifecycle is a bit different depending on the scenario in which it is used, therefore it's helpful to walk through these scenarios in detail.

_Scenario 1 - Using API Keys for machine-to-machine API operations_

When a client machine needs to programmatically access an API, it must establish identity before its’ allowed access to a developers APIs. In this scenario, an API customer would navigate to the Katanemo CIAM console for the SaaS application and create a Key. This process generates a key Id and secret which are used for authentication, authorization and auditing (3xA). Every Key generated in Katanemo must be associated with a Role, which limits operations to the ones supported in the Role. For information on Roles, please refer to docs [here](./roles).

When a client machine wants to make an API call it uses the Katanemo SDK to generate a JWT session token based on its key id and key secret, and uses that JWT session token in the HTTP Authorization Headers to perform API operations against the SaaS application. SaaS developers simply integrate the Katanemo SDK or use one of our managed gateway integrations for authentication, authorization and auditing (3xA). Once Katanemo completes authorization, the SaaS application returns the API call response to the customer.

_Scenario  2 - API Keys for user-delegated-access via OAuth2.0_

When a 3rd party developer wants to integrate with an API service to operate on protected resources it needs to establish an identity before its allowed access to the API service. To establish an identity, the 3rd party developer must navigate to the Katanemo API Service Console and create a Client Key. 

In this scenario, a 3rd party developer needs a JWT access token that contains appropriate OAuth2.0 claims to access a protected resource from a user pool belonging to an API subscriber. Once a Client Key is created, the 3rd party developer must navigate users to the Katanemo `/oauth/authorize` endpoint with relevant OAuth2.0 [Scopes](./scopes-oauth). Note, each [OpenAPI service](./service) gets managed `/login`, `/oauth/authorize`, and `/oauth/token` endpoints. 

The Katanemo `/oauth/authorize` endpoint first identifies the API subscriber domain that a user belongs to and then redirects to the appropriate Idp for an authorization grant. Once an OAuth2.0 JWT is issued, the 3rd party developer calls the API service endpoint with that token, which gets checked for authorization (e.g resource tags) by the Katanemo [evaluation engine](#). Once the API call is authorized, the token is passed to the API service for further processing. In this case, the Role associated with the Key is not used for authorization because the OAuth2.0 claims have the necessary permissions.

Once a key is created, you can download the key id/secret pair via the CIAM administrative experience hosted by Katanemo. You will need the Katanemo SDK to exchange the long-lived keys for short-term JWT session tokens for authorization purposes. When session tokens are generated they contain the appropriate role claims in the token for authorization. For more information on tokens, see [Session Tokens](./crypto-offload-and-sessions-tokens).

_Note: The primary reason to use a short-lived token is to defend against [session hijacking](https://en.wikipedia.org/wiki/Session_hijacking), when an adversary, through one method or another, steals session credentials (in this case, the token) and acts maliciously in the victim's session. The shorter-lived the token, the less time the attacker has to carry out whatever malicious activity they have planned._
