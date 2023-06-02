---
sidebar_position: 1
---

# HL7 FHIR (Health Records Exchange via an EHR system)

The [Fast Healthcare Interoperability Resources (FIHR)](http://hl7.org/fhir/) is a standard describing data formats, elements and an application programming interface for exchanging electronic health records. The standard was created by the Health Level Seven (HL7) International health-care standards organization.

Katanemo gives EHR providers and Healthcare App developers super powers to quickly serve providers, payers and patients to operate on FHIR resources in _safe, compliant and self-service ways_. Katanemo offers a Policy Administration Point (PAP) and Policy Decision Point (PDP) for FHIR resources, and _eliminates_ the complexity in building and operating the security infrastructure for FHIR resources. 

#### How do I get started with Katanemo as an EHR (electronic health records) provider?
As an EHR developer, simply create an [account](../accounts) with Katanemo, package your FHIR APIs via the OpenAPI standard, and submit it to Katanemo to create a [Service](../concepts/service) instance. With a Service instance you can invite providers and 3rd party developers to seamlessly establish identities (via SSO [Connections](../concepts/connections)), define rich least-privilege permissions via [RESTful semantics](../concepts/roles), assign users and [machines](../concepts/keys) these permissions via self-service workflows, and analyze neatly structured audit logs to meet exacting and strict compliance requirements.

![sequence-diagram.png](..%2F..%2Fstatic%2Fimg%2Fsequence-diagram.png)

The sequence diagram above captures how an EHR provider signs-up with Katanemo, and how _partners_ of an EHR provider (e.g. providers, 3rd party developers) sign up to use the EHR FHIR Restful API via Katanemo.

When the setup is complete, providers can store, access and modify FHIR resources in safe and compliant ways, and 3rd party developers can operate on those resources via a strictly-accurate permissions model using short-lived tokens or via OAuth2.0

For more information on access patterns, and how Katanemo can enable you (EHR provider) to be a rich platform on which providers, payers and 3rd party developers can build meaningful interactions without any friction, please read our blog [here](#).

#### What level of support does Katanemo offer for FHIR resources?

Katanemo offers a first-class developer and operator experience for FHIR resources. Simply add the `x-Katanemo-open-api-service-type:fhirv4` extension to your OpenAPI spec, and Katanemo will validate the schema of resources (like Patient, Observation,  etc.), create FHIR-related [Roles](../concepts/roles) (by transforming _SMART OAuth 2.0 Scopes to Role definitions_), and authorize/audit API calls on FHIR resources - even ones captured via the [FHIR Extensibility framework](https://hl7.org/fhir/extensibility.html). 

#### How does Katanemo perform authorization and auditing for FHIR resources? 

As an EHR provider, simply embed the Katanemo Auth Runtime Client (ARC) at your gateway. ARC validates the JWT Bearer token, retrieves supported API operations via role_id(s) claims present in JWT and matches [Tags](../concepts/resource-access-via-tags) appropriately against the resource. ARC returns an authorization response, and neatly creates an audit log entry for resource access in the [OpenAPI Service](../concepts/service) instance bucket for forensics and analytics. For more details on how to add ARC in your code or to a supported gateway integration, please refer to the [“How to configure ARC”](../how-to-guides/katanemo-sdk-integration) guide. 


![sequence-diagram-2.png](..%2F..%2Fstatic%2Fimg%2Fsequence-diagram-2.png)

The sequence diagram above captures how a Care Provider uses an EHR’s API to create FHIR resources, and how 3rd party partners can use [assumeRole](../concepts/roles#assumerole) functionality in Katanemo to access resources when a user is not present. Katanemo offers full support for OAuth2.0 as well. For more information, please refer to the ["How to OAuth”](../how-to-guides/katanemo-sdk-integration) guide. Resources created by Care Providers can be tagged as needed so only select users can access resources on behalf of a patient. These [Tags](../concepts/resource-access-via-tags) are validated in ARC.

#### Does Katanemo support SMART OAuth Scopes? 
Yes. Katanemo supports _SMART OAuth 2.0 Scopes._ This enables 3rd party developers to initiate an OAuth2.0 flow via the Katanemo `/oauth/authorize` endpoint and request _SMART OAuth2.0 Scopes_ from the user. Katanemo models [Scopes (OAuth2.0)](../concepts/scopes-oauth) via Roles. For example, the _“patient/Patient.rs”_ SMART OAuth2.0 scope is the name given to a system generated Role created for a partner when they sign-up for the OpenAPI Service instance. The _“patient/Patient.rs”_ Role name maps all the HTTP “Get” operations on the FHIR RESTful path where the Patient resource is defined. 



#### How does Katanemo support authorization and auditing for chained search resources via a FHIR RESTful call? 
Katanemo performs authorization and auditing for chained search resources in multiple phases:

1. The first phase validates the RESTful path, which includes the FHIR resource identifier, the HTTP method and qualified scopes (patient/Patient.rs, etc)
2. The second phase tokenizes any search/chained resources via query parameters (explicitly _search_, _subject_, etc)
3. ARC returns three things
    1. The authentication token received in the request
    2. An authorization result (400, 403, etc) and authorization-check token that captures phases of authorization and fields used for authorization (_like subject)_.
    3. The fields ignored in authorization will be captured in the authorization-check token
1. Authorization will happen locally where our light-weight utility is embedded to achieve microsecond level latencies for authorization in 95th percentile.


#### How does Katanemo support related resources via _include and _revinclude search parameters?

In the same way that Katanemo offers support for chained resources, related resources retrieved via the _include and _revinclude parameters follow the same multi-phase authorization approach as outlined above. ARC will evaluate the permissions available in the JWT token (via Role id claims, Tag key/value pairs, etc) and return an authorize/deny response for each related resource. _Note_, Katanemo only performs authorization and auditing  on FHIR resources captured in the OpenAPI spec. This includes resources defined in the OpenAPI spec that follow the FHIR Extensibility Framework.



#### Does Katanemo support security labels?

Katanemo does not offer any immediate capability to store security labels for resources. Security labels capture the level of sensitivity of the resource type and what to do with it, when shared with trading partners who have agreed to abide by them in a Mutual Trust Framework.

