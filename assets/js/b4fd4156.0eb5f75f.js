"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[333],{4137:(e,a,t)=>{t.d(a,{Zo:()=>p,kt:()=>m});var r=t(7294);function o(e,a,t){return a in e?Object.defineProperty(e,a,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[a]=t,e}function n(e,a){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);a&&(r=r.filter((function(a){return Object.getOwnPropertyDescriptor(e,a).enumerable}))),t.push.apply(t,r)}return t}function s(e){for(var a=1;a<arguments.length;a++){var t=null!=arguments[a]?arguments[a]:{};a%2?n(Object(t),!0).forEach((function(a){o(e,a,t[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):n(Object(t)).forEach((function(a){Object.defineProperty(e,a,Object.getOwnPropertyDescriptor(t,a))}))}return e}function i(e,a){if(null==e)return{};var t,r,o=function(e,a){if(null==e)return{};var t,r,o={},n=Object.keys(e);for(r=0;r<n.length;r++)t=n[r],a.indexOf(t)>=0||(o[t]=e[t]);return o}(e,a);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);for(r=0;r<n.length;r++)t=n[r],a.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(o[t]=e[t])}return o}var c=r.createContext({}),l=function(e){var a=r.useContext(c),t=a;return e&&(t="function"==typeof e?e(a):s(s({},a),e)),t},p=function(e){var a=l(e.components);return r.createElement(c.Provider,{value:a},e.children)},d="mdxType",u={inlineCode:"code",wrapper:function(e){var a=e.children;return r.createElement(r.Fragment,{},a)}},h=r.forwardRef((function(e,a){var t=e.components,o=e.mdxType,n=e.originalType,c=e.parentName,p=i(e,["components","mdxType","originalType","parentName"]),d=l(t),h=o,m=d["".concat(c,".").concat(h)]||d[h]||u[h]||n;return t?r.createElement(m,s(s({ref:a},p),{},{components:t})):r.createElement(m,s({ref:a},p))}));function m(e,a){var t=arguments,o=a&&a.mdxType;if("string"==typeof e||o){var n=t.length,s=new Array(n);s[0]=h;var i={};for(var c in a)hasOwnProperty.call(a,c)&&(i[c]=a[c]);i.originalType=e,i[d]="string"==typeof e?e:o,s[1]=i;for(var l=2;l<n;l++)s[l]=t[l];return r.createElement.apply(null,s)}return r.createElement.apply(null,t)}h.displayName="MDXCreateElement"},5196:(e,a,t)=>{t.r(a),t.d(a,{assets:()=>c,contentTitle:()=>s,default:()=>u,frontMatter:()=>n,metadata:()=>i,toc:()=>l});var r=t(7462),o=(t(7294),t(4137));const n={sidebar_position:1},s="HL7 FHIR (Health Records Exchange via an EHR system)",i={unversionedId:"use-cases/health-records-use-case",id:"use-cases/health-records-use-case",title:"HL7 FHIR (Health Records Exchange via an EHR system)",description:"The Fast Healthcare Interoperability Resources (FIHR) is a standard describing data formats, elements and an application programming interface for exchanging electronic health records. The standard was created by the Health Level Seven (HL7) International health-care standards organization.",source:"@site/docs/use-cases/health-records-use-case.md",sourceDirName:"use-cases",slug:"/use-cases/health-records-use-case",permalink:"/docs/use-cases/health-records-use-case",draft:!1,tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"defaultSidebar",previous:{title:"Use Cases",permalink:"/docs/category/use-cases"},next:{title:"Saas (API) Managed Cloud Service",permalink:"/docs/use-cases/oidc-connection"}},c={},l=[{value:"How do I get started with Katanemo as an EHR (electronic health records) provider?",id:"how-do-i-get-started-with-katanemo-as-an-ehr-electronic-health-records-provider",level:4},{value:"What level of support does Katanemo offer for FHIR resources?",id:"what-level-of-support-does-katanemo-offer-for-fhir-resources",level:4},{value:"How does Katanemo perform authorization and auditing for FHIR resources?",id:"how-does-katanemo-perform-authorization-and-auditing-for-fhir-resources",level:4},{value:"Does Katanemo support SMART OAuth Scopes?",id:"does-katanemo-support-smart-oauth-scopes",level:4},{value:"How does Katanemo support authorization and auditing for chained search resources via a FHIR RESTful call?",id:"how-does-katanemo-support-authorization-and-auditing-for-chained-search-resources-via-a-fhir-restful-call",level:4},{value:"How does Katanemo support related resources via _include and _revinclude search parameters?",id:"how-does-katanemo-support-related-resources-via-_include-and-_revinclude-search-parameters",level:4},{value:"Does Katanemo support security labels?",id:"does-katanemo-support-security-labels",level:4}],p={toc:l},d="wrapper";function u(e){let{components:a,...n}=e;return(0,o.kt)(d,(0,r.Z)({},p,n,{components:a,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"hl7-fhir-health-records-exchange-via-an-ehr-system"},"HL7 FHIR (Health Records Exchange via an EHR system)"),(0,o.kt)("p",null,"The ",(0,o.kt)("a",{parentName:"p",href:"http://hl7.org/fhir/"},"Fast Healthcare Interoperability Resources (FIHR)")," is a standard describing data formats, elements and an application programming interface for exchanging electronic health records. The standard was created by the Health Level Seven (HL7) International health-care standards organization."),(0,o.kt)("p",null,"Katanemo gives EHR providers and Healthcare App developers super powers to quickly serve providers, payers and patients to operate on FHIR resources in ",(0,o.kt)("em",{parentName:"p"},"safe, compliant and self-service ways"),". Katanemo offers a Policy Administration Point (PAP) and Policy Decision Point (PDP) for FHIR resources, and ",(0,o.kt)("em",{parentName:"p"},"eliminates")," the complexity in building and operating the security infrastructure for FHIR resources. "),(0,o.kt)("h4",{id:"how-do-i-get-started-with-katanemo-as-an-ehr-electronic-health-records-provider"},"How do I get started with Katanemo as an EHR (electronic health records) provider?"),(0,o.kt)("p",null,"As an EHR developer, simply create an ",(0,o.kt)("a",{parentName:"p",href:"../accounts"},"account")," with Katanemo, package your FHIR APIs via the OpenAPI standard, and submit it to Katanemo to create a ",(0,o.kt)("a",{parentName:"p",href:"../concepts/service"},"Service")," instance. With a Service instance you can invite providers and 3rd party developers to seamlessly establish identities (via SSO ",(0,o.kt)("a",{parentName:"p",href:"../concepts/connections"},"Connections"),"), define rich least-privilege permissions via ",(0,o.kt)("a",{parentName:"p",href:"../concepts/roles"},"RESTful semantics"),", assign users and ",(0,o.kt)("a",{parentName:"p",href:"../concepts/keys"},"machines")," these permissions via self-service workflows, and analyze neatly structured audit logs to meet exacting and strict compliance requirements."),(0,o.kt)("p",null,(0,o.kt)("img",{alt:"sequence-diagram.png",src:t(5282).Z,width:"1510",height:"1438"})),(0,o.kt)("p",null,"The sequence diagram above captures how an EHR provider signs-up with Katanemo, and how ",(0,o.kt)("em",{parentName:"p"},"partners")," of an EHR provider (e.g. providers, 3rd party developers) sign up to use the EHR FHIR Restful API via Katanemo."),(0,o.kt)("p",null,"When the setup is complete, providers can store, access and modify FHIR resources in safe and compliant ways, and 3rd party developers can operate on those resources via a strictly-accurate permissions model using short-lived tokens or via OAuth2.0"),(0,o.kt)("p",null,"For more information on access patterns, and how Katanemo can enable you (EHR provider) to be a rich platform on which providers, payers and 3rd party developers can build meaningful interactions without any friction, please read our blog ",(0,o.kt)("a",{parentName:"p",href:"#"},"here"),"."),(0,o.kt)("h4",{id:"what-level-of-support-does-katanemo-offer-for-fhir-resources"},"What level of support does Katanemo offer for FHIR resources?"),(0,o.kt)("p",null,"Katanemo offers a first-class developer and operator experience for FHIR resources. Simply add the ",(0,o.kt)("inlineCode",{parentName:"p"},"x-Katanemo-open-api-service-type:fhirv4")," extension to your OpenAPI spec, and Katanemo will validate the schema of resources (like Patient, Observation,  etc.), create FHIR-related ",(0,o.kt)("a",{parentName:"p",href:"../concepts/roles"},"Roles")," (by transforming ",(0,o.kt)("em",{parentName:"p"},"SMART OAuth 2.0 Scopes to Role definitions"),"), and authorize/audit API calls on FHIR resources - even ones captured via the ",(0,o.kt)("a",{parentName:"p",href:"https://hl7.org/fhir/extensibility.html"},"FHIR Extensibility framework"),". "),(0,o.kt)("h4",{id:"how-does-katanemo-perform-authorization-and-auditing-for-fhir-resources"},"How does Katanemo perform authorization and auditing for FHIR resources?"),(0,o.kt)("p",null,"As an EHR provider, simply embed the Katanemo Auth Runtime Client (ARC) at your gateway. ARC validates the JWT Bearer token, retrieves supported API operations via role_id(s) claims present in JWT and matches ",(0,o.kt)("a",{parentName:"p",href:"../concepts/resource-access-via-tags"},"Tags")," appropriately against the resource. ARC returns an authorization response, and neatly creates an audit log entry for resource access in the ",(0,o.kt)("a",{parentName:"p",href:"../concepts/service"},"OpenAPI Service")," instance bucket for forensics and analytics. For more details on how to add ARC in your code or to a supported gateway integration, please refer to the ",(0,o.kt)("a",{parentName:"p",href:"../how-to-guides/katanemo-sdk-integration"},"\u201cHow to configure ARC\u201d")," guide. "),(0,o.kt)("p",null,(0,o.kt)("img",{alt:"sequence-diagram-2.png",src:t(765).Z,width:"592",height:"406"})),(0,o.kt)("p",null,"The sequence diagram above captures how a Care Provider uses an EHR\u2019s API to create FHIR resources, and how 3rd party partners can use ",(0,o.kt)("a",{parentName:"p",href:"../concepts/roles#assumerole"},"assumeRole")," functionality in Katanemo to access resources when a user is not present. Katanemo offers full support for OAuth2.0 as well. For more information, please refer to the ",(0,o.kt)("a",{parentName:"p",href:"../how-to-guides/katanemo-sdk-integration"},'"How to OAuth\u201d')," guide. Resources created by Care Providers can be tagged as needed so only select users can access resources on behalf of a patient. These ",(0,o.kt)("a",{parentName:"p",href:"../concepts/resource-access-via-tags"},"Tags")," are validated in ARC."),(0,o.kt)("h4",{id:"does-katanemo-support-smart-oauth-scopes"},"Does Katanemo support SMART OAuth Scopes?"),(0,o.kt)("p",null,"Yes. Katanemo supports ",(0,o.kt)("em",{parentName:"p"},"SMART OAuth 2.0 Scopes.")," This enables 3rd party developers to initiate an OAuth2.0 flow via the Katanemo ",(0,o.kt)("inlineCode",{parentName:"p"},"/oauth/authorize")," endpoint and request ",(0,o.kt)("em",{parentName:"p"},"SMART OAuth2.0 Scopes")," from the user. Katanemo models ",(0,o.kt)("a",{parentName:"p",href:"../concepts/scopes-oauth"},"Scopes (OAuth2.0)")," via Roles. For example, the ",(0,o.kt)("em",{parentName:"p"},"\u201cpatient/Patient.rs\u201d")," SMART OAuth2.0 scope is the name given to a system generated Role created for a partner when they sign-up for the OpenAPI Service instance. The ",(0,o.kt)("em",{parentName:"p"},"\u201cpatient/Patient.rs\u201d")," Role name maps all the HTTP \u201cGet\u201d operations on the FHIR RESTful path where the Patient resource is defined. "),(0,o.kt)("h4",{id:"how-does-katanemo-support-authorization-and-auditing-for-chained-search-resources-via-a-fhir-restful-call"},"How does Katanemo support authorization and auditing for chained search resources via a FHIR RESTful call?"),(0,o.kt)("p",null,"Katanemo performs authorization and auditing for chained search resources in multiple phases:"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},"The first phase validates the RESTful path, which includes the FHIR resource identifier, the HTTP method and qualified scopes (patient/Patient.rs, etc)"),(0,o.kt)("li",{parentName:"ol"},"The second phase tokenizes any search/chained resources via query parameters (explicitly ",(0,o.kt)("em",{parentName:"li"},"search"),", ",(0,o.kt)("em",{parentName:"li"},"subject"),", etc)"),(0,o.kt)("li",{parentName:"ol"},"ARC returns three things",(0,o.kt)("ol",{parentName:"li"},(0,o.kt)("li",{parentName:"ol"},"The authentication token received in the request"),(0,o.kt)("li",{parentName:"ol"},"An authorization result (400, 403, etc) and authorization-check token that captures phases of authorization and fields used for authorization (",(0,o.kt)("em",{parentName:"li"},"like subject)"),"."),(0,o.kt)("li",{parentName:"ol"},"The fields ignored in authorization will be captured in the authorization-check token"))),(0,o.kt)("li",{parentName:"ol"},"Authorization will happen locally where our light-weight utility is embedded to achieve microsecond level latencies for authorization in 95th percentile.")),(0,o.kt)("h4",{id:"how-does-katanemo-support-related-resources-via-_include-and-_revinclude-search-parameters"},"How does Katanemo support related resources via _include and _revinclude search parameters?"),(0,o.kt)("p",null,"In the same way that Katanemo offers support for chained resources, related resources retrieved via the ",(0,o.kt)("em",{parentName:"p"},"include and _revinclude parameters follow the same multi-phase authorization approach as outlined above. ARC will evaluate the permissions available in the JWT token (via Role id claims, Tag key/value pairs, etc) and return an authorize/deny response for each related resource. _Note"),", Katanemo only performs authorization and auditing  on FHIR resources captured in the OpenAPI spec. This includes resources defined in the OpenAPI spec that follow the FHIR Extensibility Framework."),(0,o.kt)("h4",{id:"does-katanemo-support-security-labels"},"Does Katanemo support security labels?"),(0,o.kt)("p",null,"Katanemo does not offer any immediate capability to store security labels for resources. Security labels capture the level of sensitivity of the resource type and what to do with it, when shared with trading partners who have agreed to abide by them in a Mutual Trust Framework."))}u.isMDXComponent=!0},765:(e,a,t)=>{t.d(a,{Z:()=>r});const r=t.p+"assets/images/sequence-diagram-2-26c6e0fd6409fdd8242efb242c53ce41.png"},5282:(e,a,t)=>{t.d(a,{Z:()=>r});const r=t.p+"assets/images/sequence-diagram-08db7b62110aa746e804156e1d73103c.png"}}]);