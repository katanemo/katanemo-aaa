---
sidebar_position: 2
---

# How to Modify the Default “all tags must match” Behavior of Katanemo?

Katanemo’s default behavior is to match **all** tags associated with a resource against tags present in the session token (of the principal) making the call. However, you can alter this default behavior for your particular use case by adding the “where” clause to your Role definition (aka. Role policies).


_Where clause (via Role policies)_
In cases where the default behavior of **all** tags associated with a resource doesn’t satisfy your particular use case, you can define conditional policies using the “where” clause to match tags as per your use case. Note, the above UI experience hides the details of how to construct permission boundaries of a Role, however the following use cases showcase _policies_ using the OpenAPI-based semantics and the “where” clause to construct simple, yet highly powerful authorization rules.

_Use Case #1: Some users will have READ/WRITE access to dev clusters, and READ access to stage & prod clusters._


```yaml
 allow:
  api: 
    – PUT:/cluster/{clusterId}
    – GET:/cluster/{clusterId}
  where: $resourceTags:clustertag = 'dev'
  api:
   - GET:/cluster/{clusterId}
  where: $resourceTags:clustertag IN ('staging', 'production')
```


_Use Case #2: Some users will have READ/WRITE access to dev clusters of type EKS._


```yaml
 allow:
  api: 
   – PUT:/cluster/{clusterId}
   – GET:/cluster/{clusterId}
  where: $resourceTags:clustertag = 'EKS'
```


_Use Case #3: Some users will have the ability to create promotions only up to a maximum of 10% off._


```yaml
 allow:
  api: 
   – POST:/api-offers/promo/create
  where: $request:promo:discount:value < 10 AND $request:promo:targetProducts:value IN ('SKU-124')
```


_Use Case #3a: Some users will have the ability to UPDATE promotions where tag = “independence-day”_


```yaml
 allow:
  api: 
   – PUT:/api-offers/promo/update/{promoId}
  where: $resourceTag:note = "independence day promos"
```


`$resourceTags,` `$request`, and `$principalTags` are system variables that can be used in the _where_ clause to get tags for the resource or the principal, respectively. The `$resourceTags:tagkey` directive allows you to look for a particular tag key for a resource.


