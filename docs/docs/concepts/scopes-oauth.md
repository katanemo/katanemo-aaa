---
sidebar_position: 8
---

# Scopes (OAuth 2.0)

Katanemo makes working with OAuth2.0 scopes simple. As an developer you simply define “service-defined” Roles in your OpenAPI spec via Katanemo extensions. A “service-defined” Role is a unique name mapped to a set of OpenAPI operations (resource paths and HTTP methods). Your customers use "service-defined” role names when assigning permissions to users or machine principals, or when initiating an OAuth2.0 flow via the Katanemo `/oauth/authorize` endpoint. Katanemo’s [evaluation engine](#) maps OAuth2.0 claims received in the JWT to “service-defined” Roles via the claim name, and performs  appropriate authorization checks when a user or 3rd party applications tries to access a resource or perform an API operation. Note, service-defined Roles can’t be modified by customers.
