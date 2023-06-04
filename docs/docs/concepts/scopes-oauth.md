---
sidebar_position: 8
---

# Scopes (OAuth 2.0)

Katanemo makes working with OAuth2.0 scopes super simple. As an API developer you simply define “service-defined” Roles in your OpenAPI spec via Katanemo extensions. A “service-defined” Role is simply a unique name mapped to a set of OpenAPI operations (resource paths and HTTP methods). 3rd party developers simply use “service-defined” role names as scopes when initiating an OAuth2.0 flow via the `/oauth/authorize` endpoint for that specific OpenAPI Service instance. Katanemo’s [evaluation engine](#) maps OAuth2.0 claims received in the JWT to “service-defined” Roles via the claim name, and performs the appropriate authorization checks. Note, service-defined Roles can’t be modified by API subscribers.