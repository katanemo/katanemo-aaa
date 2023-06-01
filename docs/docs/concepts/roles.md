---
sidebar_position: 4
---

# Roles


Roles establish a permission boundary that enables access to select API operations of a SaaS application. You don’t need to learn a new policy language to create Roles. Simply associate a list of OpenAPI-based operations (API paths and HTTP methods) with a Role, and assign Roles to Users or [API Keys](../concepts/keys) to enforce a strict authorization boundary. For example, the below UI shows how an API subscriber can define a Role for a set of API operations of an SaaS EHR application. Once the Role gets assigned to a User or an API Key, those [principals](../concepts/authorization-principles.md) are then limited to only those API operations associated with the Role. For instance the “Intern” Role below can only conduct the following API operations.

* GET:  /v2/catalog/doctors/images/{image-id}
* PUT:  /v2/catalog/doctors/images/{image-id}
* POST: /v2/catalog/doctors/images/{image-id

![rolename.png](..%2F..%2Fstatic%2Fimg%2Frolename.png)

Katanemo performs role-based authorization via scp claims in the JWT session token, or specific attributes in the case of an OIDC-compliant IDP integration to ensure that the entity (User or API Key) has permissions to perform the appropriate API operation. To learn more about Katanemo's authorization evaluation logic, read [here](../concepts/authorization-evaluation-logic).

### Policies (based on OpenAPI and GraphQL)

Policies capture permissions for a user or machine action on a particular set of APIs. Kataemo’s policy language is based on popular specification languages of APIs.

For RESTful APIs Katanemo supports an OpenAPI-based policy language. OpenAPI neatly captures RESTful API definitions, resource schemas and establishes a great foundation for authorization and auditing. With familiar RESTful semantics customers (and developers) don’t need to learn yet another policy language. Instead customers focus on defining accurate authorization strategies in logical and idiomatic ways. Katanemo reduces permissions complexity, improves readability and understanding of access controls, and enables customers to easily achieve the principle of least privilege.

The following is an OpenAPI-based permission policy for an SaaS application where users can get and update the cluster resource via the /cluster API. 

```yaml
allow:
  apis:
    - PUT: /cluster/{cluster-id}
    - GET: /cluster/{cluster-id}
```

Similarly, the following is a GraphQL-based permission policy where users can query the cluster resource of a SaaS application. 

```yaml
allow:
  query:
    - cluster
```

_Where clause_
In some cases a simple permissions policy like the ones shown above can’t satisfy strict security requirements.  For such scenarios Katanemo allows customers to define conditional policies using the “where” clause. Katanemo’s “where” clause is modeled after the popular SQL where clause to make construction of policies simple to understand and deploy. The following policies show you can construct simple yet strictly precise permissions policies and associate them with authorization principals like users, machines, etc. 

_Use Case #1: Interns will have READ/WRITE access to dev clusters, and READ access to stage & prod clusters._

```yaml
allow:
  api:
    - PUT: /cluster/{cluster-id}
    - GET: /cluster/{cluster-id}
  where: $resourceTags:cluster = ‘dev’
  api: 
    - GET: /cluster/{cluster-id}
  where: $resourceTags:cluster IN (‘stage’, ‘prod’)
```
_Note: $resourceTags, $request, and $principalTags_ are reserved Katanemo variables that can be used in the where clause to construct precise authorization policies. In the above example, Katanemo retrieves values for the "cluster" tag on the `{clusterId}` resource, and checks to see if the tag value is either `staging` or `production`. Learn more about resource access via Katanemo Tags.

_Use Case #2: Some users will have READ/WRITE access to dev clusters of type EKS_

```yaml
allow:
  api:
    - PUT: /cluster/{cluster-id}
    - GET: /cluster/{cluster-id}
  where: $resourceTags:cluster = ‘dev’ AND $resourceTags:clusterType = ‘EKS’
```

_Use Case #3: Some users will have the ability to create promotions only up to a maximum of 10% off._

```yaml
allow:
  api:
    - POST: /api-offers/promo/create
  where: $request:promo:discount:value < 10 AND $request:promo:targetProducts:value IN ('SKU-124')
```

_Use Case #3a: Some users will have the ability to UPDATE promotions where tag = “independence-day”_

```yaml
allow:
  api:
    - PUT: /api-offers/promo/update/{promoId}
  where: $resourceTag:note = "independence day promos"
```

### AssumeRole

APIs are disruptive because they enable software to be consumed in new and interesting ways. One of those ways is having API resources created by one customer be operated by another using the same APIs. For example, imagine an Electronic Healthcare Records (EHR) system that manages records on behalf of clinics and care providers. These care providers need AI/ML capabilities to dramatically enhance the patient experience. Before Katanemo, an EHR provider would select an AI/ML solution, spend time integrating it, and then package it as a value added service. With Katanemo the same EHR provider can enable hundreds of AI/ML solutions to be consumed by 1000s of care providers in a frictionless self-service way. The EHR provider can offer a true platform experience, and enjoy network growth effects without compromising on security or compliance.

![careproviderimage.png](..%2F..%2Fstatic%2Fimg%2Fcareproviderimage.png)

Katanemo’s `assumeRole` functionality enables a platform experience for any SaaS developer. With assumeRole one a developer (say an AI/ML application) can request temporary, limited-privilege access to resources created by another customer (say a clinic or care provider). If you want to give someone the right to request temporary tokens, simply create a Role in Katanemo, configure supported API operations for that Role, and [Tag](./resource-access-via-tags) the Role with authorization principal(s) that can assume it. For more information on [Tags](./resource-access-via-tags), and how they compliment Roles for authorization, please read further.  For more information about the assumeRole API, please see [Role APIs](#).

![overlake.png](..%2F..%2Fstatic%2Fimg%2Foverlake.png)
