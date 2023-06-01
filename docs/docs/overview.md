---
sidebar_position: 1
---

# Overview

Katanemo helps developers build critical privacy and collaboration features for SaaS applications that unlocks growth. Katanemo is a purpose-built identity and fine-grained authorization system designed for modern SaaS applications - it unifies customer onboarding and identity (_authentication_), protects who can do what on which resource (_authorization_), and leaves a structured audit trail that helps developers meet exacting compliance requirements on behalf of their customers. With Katanemo, developers can add [PLG](https://openviewpartners.com/product-led-growth/) motions via a frictionless on-boarding experience, and expand into new enterprise scenarios in minutes via powerful governance and sharing features for SaaS resources.



Today, developers building modern SaaS applications are faced with an increasingly complex trade-off between usability and security. On the one hand, they want users to simply and seamlessly access their applications. On the other, they must prevent access to data and functionality that should not be seen by other users.

Access patterns and safety controls, particularly in multi-tenant Software as a service (SaaS) apps, are far more complex than traditional consumer applications. Can your SaaS application go from supporting a single user in a team to effortlessly serving thousands of enterprise users via Single sign on (SSO)? Can it offer automation via Application Programming Interfaces (API) keys? Can it support modern fine-grained access controls needed for privacy, security and collaboration before businesses can trust you with their data and workloads?

With an [OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md) (and GraphQL) based development workflow, developers can add the same on-boarding, collaboration and privacy sophistication packed into planet-scale SaaS (API) companies like Plaid, Github and Stripe - without the effort, expertise or infrastructure complexity.

## **Who should use Katanemo? **

If you want to effortlessly go from supporting small teams to thousands of users in an enterprise, then Katanemo is for you. If you want to ensure that enterprises can quickly trust your application via rich privacy and collaboration features, then Katanemo is for you. If you want to enable a _platform_ experience where 3rd party developers innovate with your customers through APIs, then Katanemo is for you. Katanemo is designed for API-first SaaS application developers to get precious time back in building differentiated capabilities. Our purpose built experience helps developers add critical IAM (Identity and Access Management) capabilities and experiences that are as sticky and delightful as ones offered by AWS, Stripe and Twilio.

## **Why are APIs important?**

APIs are the future of software. Traditionally, software has been delivered via a user interface, where users interact with software via UI workflows. As the world gets even more connected and we augment our lives with automation, the future becomes more API driven so that software can be consumed in interesting ways. APIs are a disruptive way to deliver software, proven by the likes of Stripe, Twilio and AWS. If you don’t have an API-first strategy, consider adopting one or risk getting disrupted.

## **Why is authentication, authorization and auditing important for API-first SaaS applications? **

Authentication, authorization and auditing (3xA) are critical features needed to effortlessly on-board customers, and enable a world-class privacy and safe collaboration experience. Modern SaaS companies that achieve breakthrough success build an exceptional collaboration experience and achieve the highest levels of privacy - Figma, Slack, Box and AWS are just a few examples.

API-first SaaS developers must identify subscribers, check if callers have permissions on specific API operations and leave a compliant trail of what actions were performed by whom and when. Without a 3xA strategy in place, _developers can’t sell into enterprises or unlock new market segments_. Enterprises demand these capabilities because of two simultaneous transitions in the SaaS industry: _protect from prolific attacks via least privilege access controls, and the need to create safe collaboration for sticky growth_. As the enterprise-readiness bar keeps on raising, it's leaving many developers to build out critical 3xA infrastructure themselves.

## **How does Katanemo work at a high-level?**

At a high-level, the following image captures key actors and interactions in Katanemo.

![Overview.png](..%2Fstatic%2Fimg%2FOverview.png)

1. Developers publish an [OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md) spec and get delightful sign-up and login workflows for their SaaS application.
2. SaaS customers can use self-service tools offered by Katanemo (on behalf of SaaS developers) to:
    1. Manage multi-modal identities (users, SSO, etc) in their organization
    2. Construct simple, yet strictly accurate authorization rules via familiar RESTful semantics
    3. Manage user and machine-to-machine access strategies  – _without hopping between multiple tools or being forced to learn new concepts to achieve an exceptional enterprise-readiness experience._
3. The Katanemo authorization runtime client (ARC) is a light-weight utility that does the intelligent heavy lifting of protecting who can do what on which resource (_authorization_) - at blazing fast speed. ARC neatly integrates with popular gateway solutions, or via an SDK where crypto-offload and authorization checks happen.
4. All authorization calls are neatly logged and retained for developers to meet compliance requirements or upsell to enterprises for additional revenue.


## **What if I already have an Identity Provider for my SaaS Application?**

No problem. If you already have an existing identity pool where you manage customers for your service, you can neatly bring that to Katanemo and use all of the remaining functionality that we offer. For more details on how to bring your identity pool, contact us [here](http://www.katanemo.com/talk-to-an-expert).
