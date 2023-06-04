---
sidebar_position: 4
---

# How to Configure a New Okta SAML connection?

Each SSO Identity Provider requires specific information to create and configure a new SAML-based Connection. Often, the information required to create a new Connection will slightly differ by Identity Provider. To create an Okta SAML Connection, you’ll need three pieces of information: the Assertion Consumer Service (ACS) URL, a SP Entity ID, and an IdP Metadata URL.

The ACS URL is the location an Identity Provider redirects its authentication response to. In Okta’s case, it needs to be set by the Enterprise when configuring your application in their Okta instance. The SP Entity ID is a URI used to identify the issuer of a SAML request, response, or assertion. In this case, the entity ID is used to communicate that Katanemo will be the party performing SAML requests to the Enterprise’s Okta instance.

Specifically, the ACS URL will need to be set as the “Single sign on URL” and the SP Entity ID will need to be set as the “Audience URI (SP Entity ID)” in the “Configure SAML” step of the Okta “Edit SAML Integration” wizard.

1. **Create a SAML Application with Okta** - For SSO to properly function with Okta you’ll need to create and configure a SAML application. Log in to [Okta](https://login.okta.com/), go to the admin dashboard, and select “Applications” in the navigation bar. Once in the Applications page, click “Create App Integration -> Create New App”, and select “SAML 2.0” as a Sign on method. Click “Next”.
2. **Configure the SAML Application** - Input the ACS URL from your Katanemo Dashboard as the “Single sign on URL” and input the SP Entity ID from your Katanemo Dashboard as the “Audience URI (SP Entity ID)”.
3. **Assign Users to the SAML Application** - To give users permission to authenticate via this SAML app, you will need to assign individual users and/or groups of users to the Okta SAML app. Click on the “Assignments” tab, and select either “Assign to People” or “Assign to Groups”. Find the individual user(s) and/or group(s) that you would like to assign to the app, and click “Assign” next to them. Click “Done” when you are finished.
4. **Upload Metadata URL** - Click on the “Sign On” tab of the SAML app you just created. Click the “Actions” dropdown for the correct certificate and select “View IdP Metadata." A separate tab will open. Copy the link in the browser and add that to the SAML Connection in Katanemo.
5. **Configure Role for Connection** - Before a connection can be made active, you must associate a Role that was previously created. Users that SSO will be assigned this Role against which API operations will be authorized. 

Role Mappings to Connections Object:
1. Katanemo supports creating multiple Connections in a single [Identity Pool](#) which allows you to assign different upstream user groups the appropriate SSO link for their specific access to service capabilities. For example you can create a Connections SSO link shared with ‘interns’, and another Connections SSO link shared with the ‘senior developers’ group.
2. You can also map SAML attributes to Roles. For example, if you want to map user groups to Roles in Katanemo, you can map"attribute-name:group=attribute-value:admins" to a Katanemo role. The Connections default role is not used if Katanemo can find a valid SAML attribute to role mapping in the SSO request. Note, attribute names and values are case sensitive.
