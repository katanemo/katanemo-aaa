---
sidebar_position: 4
---

# Customer Quick Start Guide 


This guide is intended for developers to share with their customers so that they use Katanemo’ Customer Identity and Access Management (CIAM) capabilities to manage authorization policies, view audit logs and define a multi-modal identity experience for their SaaS application. As a developer you must replace _{ placeholder }_ values before sharing this guide with your customers.


To get started, simply navigate to the sign-up {SaaS Application Sign-up _URL_} and complete the sign-up process.

## **Step 1:  Sign-up to use {SaaS Application Name}**



1. Navigate to the Sign-up URL to get started with our _{SaaS application name}_.
2. **Enter** your email address and **click** Sign Up, and wait for a system generated email
3. Navigate to the link you got in email, and set a password for your username (email).

Once you complete the steps above, you will be redirected to _{SaaS application name}_ CIAM experience where you can manage authorization policies, view audit logs and manage a rich identity experience for _{SaaS application name}_

## **Step 2: Create Roles **

Once you successfully sign-up to use _{SaaS application name}_ via the CIAM console, you should create roles that form the basis of authorization. By default, Katanemo creates an administrator role that has access to all API paths and methods. and a user role that only has the ability to get data about API resources of the _{SaaS application name}_. In [RESTful](https://en.wikipedia.org/wiki/Representational_state_transfer) terms, the admin role has the ability to perform GET, PUT, PATCH, DELETE, OPTIONS, and POST operations on any API, while the user role has GET access on all APIs.

Roles help you create least-privilege permissions that can be assigned to users, or assigned to clients (via API [Keys](./concepts/keys)) for OAuth or automation scenarios. To create roles:




1. Navigate to the **Roles **section of the _{SaaS application name}_ CIAM console hosted by Katanemo
2. Enter the **Name **and **Description **of the Role you are creating
3. Select **APIs** (_paths and HTTP methods_) from the dropdown list that you want to associate with the role. _Note_: you can add multiple API path/method combinations to a single role from the dropdown.
4. Click **Save. **


## **Step 3: Invite Users**

For light-weight team and user management simply invite users to use the { SaaS application name }, and assign them appropriate Roles upon invite. To invite users to use { SaaS application name }, simply: 




1. Navigate to the **Users **section of the _{SaaS application name}_ CIAM console hosted by Katanemo
2. Click on **+Add New User **and enter the email address of the user you want to invite.
3. Assign the user a **Role**, and associate any Tags/attributes that define the type of user
4. Click **Invite User**. _Note_: This will trigger an email verification workflow
