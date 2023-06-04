---
sidebar_position: 2
---

# Service


A Katanemo Service is a representation of the API surface area that developers want to enrich with enterprise-readiness capabilities (_authentication, authorization, auditing - 3xA_). Services are created using the familiar [OpenAPI](https://www.openapis.org/) standard. OpenAPI neatly captures RESTful API definitions, resource schemas and establishes a great foundation for authorization and auditing. With familiar RESTful semantics developers (and customers) don’t need to learn a new policy language, and get to enrich their API experience with rich 3xA capabilities without having to build and scale complex authorization and auditing engines

Each Katanemo OpenAPI Service instance gets a canonical sign-up and login URL that can be shared with SaaS customers. In addition Katanemo hosts a Customer Identity and Access Management (CIAM) console for each Service instance, where SaaS customers can define identities, manage roles, review audit logs and manage authorization strategies in fully **self-service ways**.

Note, the OpenAPI Service instance you create in Katanemo is private by default. To share your Service with customers, you need to add [Tags](./resource-access-via-tags) so that anyone can sign-up for your SaaS service. Tags are a core part of Katanemo’s [authorization evaluation logic](../concepts/authorization-evaluation-logic). You can also use the Katanemo SaaS developer console to easily toggle the Service instance from private to public. For more information on Tags, see the documentation [here](./resource-access-via-tags).

### Updating Services (or Creating Multiple Services)

You can create multiple Katanemo Service instances to support test and production scenarios. You can also update your Katanemo Service resources by uploading new versions of your [OpenAPI](https://www.openapis.org/) spec. Changes made to your Katanemo Service instance reflect immediately in the CIAM console experience of your customers. 
