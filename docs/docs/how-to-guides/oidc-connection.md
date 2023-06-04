---
sidebar_position: 3
---

# How to Configure a New OIDC connection?

Each SSO Identity Provider requires specific information to create and configure a new [Connection](../concepts/connections). Often, the information required to create a Connection will differ by Identity Provider. To create an OpenID Connect (OIDC) Connection, you’ll need five pieces of information: a Redirect URI, a Client ID, a Client Secret, a Discovery Endpoint, and a Role.

Katanemo provides the Redirect URI. It’s readily available in your Connection Settings in the Katanemo Dashboard. The Redirect URI is the location an Identity Provider redirects its authentication response to. In order to integrate you’ll need the Client ID, Client Secret, the Discovery Endpoint, and the Role that is associated with the Connection.

1. **Create an Application with your IdP** - For SSO to properly function with your Identity Provider, you’ll need to create and configure your OpenID Connect application to support the authorization code grant type and have the redirect URI from Katanemo listed as your login or signup redirect URI.
2. **Add claims to the ID token** - Add the sub, email, given_name (or name), and family_name claims to the user ID token in your OIDC provider settings. These claims map to the idp_id, email, first_name, and last_name attributes in the user profile returned by Katanemo. For many providers, these claims are included by default, but for other providers you will need to add these claims.
3. **Provide your Client Credentials** - After creating an OpenID Connection application, a Client ID and Client Secret will be provisioned for you by your Identity Provider. Enter these details in your Connection settings in the Service Console Dashboard.
4. **Add Discovery Endpoint** - Discovery Endpoint contains important configuration information. Enter this endpoint in your Connection settings in the Katanemo Dashboard. It will always end with `/.well-known/openid-configuration` as described in the OpenID Provider Configuration Request documentation. You can confirm that the endpoint is correct by entering it in a browser window. If there is a JSON object with metadata about the connection returned, the endpoint is correct. 
5. **Configure Role for Connection** - Before a connection can be made active, you must associate a Role that was previously created. Users that SSO will be assigned this Role against which API operations will be authorized.

Role Mappings to Connections Object:
1. Katanemo supports creating multiple Connections in a single [Organization](../concepts/organizations) which allows you to assign different upstream user groups the appropriate SSO link for their specific access to service capabilities. For example you can create a Connections SSO link shared with ‘interns’, and another Connections SSO link shared with the ‘senior developers’ group.
2. You can also map OIDC scopes to Roles. For example, if you want to map the user’s group to a Role in Katanemo, you can configure the following mapping "groups:admins=$role-id” in the Connections object. The Connections default role is not used if Katanemo can find a valid scope to role mapping in the SSO request. Note, attribute names and values are case sensitive.
