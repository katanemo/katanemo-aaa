---
sidebar_position: 9
---

# Crypto Offload

Katanemo is an OIDC compliant 3xA service, which means that it generates an `id_token`, an `access_token` for users and API keys, and optionally a `refresh_token` as per the ODIC spec. These tokens are encrypted with an RSA256 (RS-256) signature key. You can retrieve the RSA public key via Katanemo’s JSON Web Key Set (JWKS).

If you are using Katanemo as an IDP, it creates a token that contains information about the user and additional meta-data like Tags and Role detail, and signs the JWT token using its private key. Katanemo secures the private key, which is unique per tenant (developer or subscriber). To verify that the token is valid and originated from Katanemo, your application can validate the token’s signature using the public key.  For example, you'll provide the client with the JWKS endpoint which exposes Katanemo’ signing keys. Using the getSigningKey you can then get the signing key that matches a specific kid.

```js
const jwksClient = require('jwks-rsa');
const client = jwksClient({
  jwksUri: 'https://api.katanemo.com/service/{serviceId}/.well-known/jwks.json',
  requestHeaders: {}, // Optional
  timeout: 30000 // Defaults to 30s
});

const kid = 'RkI5MjI5OUY5ODc1N0Q4QzM0OUYzNkVGMTJDOUEzQkFCOTU3NjE2Rg'; 
const key = await client.getSigningKey(kid);
const signingKey = key.getPublicKey();
```
