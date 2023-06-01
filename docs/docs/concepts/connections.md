---
sidebar_position: 6
---

# Connections

Katanemo enables customers to invite and manage Users via the CIAM console. But enterprise customers will demand that they federate users via an existing Identity provider (Idp) . Katanemo supports Single sign-on (SSO) for OIDC and SAML compliant Identity providers like Okta, Ping, Auth0 via Connections. An enterprise IT administrator simply creates a Connection to their preferred Idp, and Katanemo uses the upstream Idp to initiate login and manages the token lifecycle before returning an authorization code to the application via its configured redirect_uri. For more details, read [How to Configure a New OIDC connection?](../how-to-guides/oidc-connection)
