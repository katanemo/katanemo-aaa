"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[843],{4137:(e,a,t)=>{t.d(a,{Zo:()=>p,kt:()=>h});var s=t(7294);function n(e,a,t){return a in e?Object.defineProperty(e,a,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[a]=t,e}function o(e,a){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);a&&(s=s.filter((function(a){return Object.getOwnPropertyDescriptor(e,a).enumerable}))),t.push.apply(t,s)}return t}function r(e){for(var a=1;a<arguments.length;a++){var t=null!=arguments[a]?arguments[a]:{};a%2?o(Object(t),!0).forEach((function(a){n(e,a,t[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):o(Object(t)).forEach((function(a){Object.defineProperty(e,a,Object.getOwnPropertyDescriptor(t,a))}))}return e}function i(e,a){if(null==e)return{};var t,s,n=function(e,a){if(null==e)return{};var t,s,n={},o=Object.keys(e);for(s=0;s<o.length;s++)t=o[s],a.indexOf(t)>=0||(n[t]=e[t]);return n}(e,a);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(s=0;s<o.length;s++)t=o[s],a.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(n[t]=e[t])}return n}var c=s.createContext({}),l=function(e){var a=s.useContext(c),t=a;return e&&(t="function"==typeof e?e(a):r(r({},a),e)),t},p=function(e){var a=l(e.components);return s.createElement(c.Provider,{value:a},e.children)},u="mdxType",m={inlineCode:"code",wrapper:function(e){var a=e.children;return s.createElement(s.Fragment,{},a)}},d=s.forwardRef((function(e,a){var t=e.components,n=e.mdxType,o=e.originalType,c=e.parentName,p=i(e,["components","mdxType","originalType","parentName"]),u=l(t),d=n,h=u["".concat(c,".").concat(d)]||u[d]||m[d]||o;return t?s.createElement(h,r(r({ref:a},p),{},{components:t})):s.createElement(h,r({ref:a},p))}));function h(e,a){var t=arguments,n=a&&a.mdxType;if("string"==typeof e||n){var o=t.length,r=new Array(o);r[0]=d;var i={};for(var c in a)hasOwnProperty.call(a,c)&&(i[c]=a[c]);i.originalType=e,i[u]="string"==typeof e?e:n,r[1]=i;for(var l=2;l<o;l++)r[l]=t[l];return s.createElement.apply(null,r)}return s.createElement.apply(null,t)}d.displayName="MDXCreateElement"},8260:(e,a,t)=>{t.r(a),t.d(a,{assets:()=>c,contentTitle:()=>r,default:()=>m,frontMatter:()=>o,metadata:()=>i,toc:()=>l});var s=t(7462),n=(t(7294),t(4137));const o={sidebar_position:5},r="Resource Access (via Tags)",i={unversionedId:"concepts/resource-access-via-tags",id:"concepts/resource-access-via-tags",title:"Resource Access (via Tags)",description:"Tags consist of a key and value pair, and are part of a resource\u2019s meta-data. Tags are used to ensure that API resources that belong to a set of principals are only accessible by those principals. Tags and Roles complement each other to create a powerful, yet simple authorization strategy. Roles capture what API operations can be performed by a principal, and Tags capture which resources are accessible to a set of principals. SaaS developers store Tags for resources created by their customers, and customers attach Tags to authorization principals to be used in authorization.",source:"@site/docs/concepts/resource-access-via-tags.md",sourceDirName:"concepts",slug:"/concepts/resource-access-via-tags",permalink:"/docs/concepts/resource-access-via-tags",draft:!1,tags:[],version:"current",sidebarPosition:5,frontMatter:{sidebar_position:5},sidebar:"defaultSidebar",previous:{title:"Roles",permalink:"/docs/concepts/roles"},next:{title:"Connections",permalink:"/docs/concepts/connections"}},c={},l=[{value:"Set Tags on Resources",id:"set-tags-on-resources",level:4},{value:"Tag Storage in Katanemo",id:"tag-storage-in-katanemo",level:4},{value:"Access Tags",id:"access-tags",level:2},{value:"System Defined Access Tags",id:"system-defined-access-tags",level:3}],p={toc:l},u="wrapper";function m(e){let{components:a,...t}=e;return(0,n.kt)(u,(0,s.Z)({},p,t,{components:a,mdxType:"MDXLayout"}),(0,n.kt)("h1",{id:"resource-access-via-tags"},"Resource Access (via Tags)"),(0,n.kt)("p",null,"Tags consist of a key and value pair, and are part of a resource\u2019s meta-data. Tags are used to ensure that API resources that belong to a set of ",(0,n.kt)("a",{parentName:"p",href:"/docs/concepts/authorization-principles"},"principals")," are only accessible by those principals. Tags and Roles complement each other to create a powerful, yet simple authorization strategy. ",(0,n.kt)("strong",{parentName:"p"},"Roles capture what API operations can be performed by a principal, and Tags capture which resources are accessible to a set of ",(0,n.kt)("a",{parentName:"strong",href:"/docs/concepts/authorization-principles"},"principals"),".")," SaaS developers store Tags for resources created by their customers, and customers attach Tags to authorization principals to be used in authorization. "),(0,n.kt)("h4",{id:"set-tags-on-resources"},"Set Tags on Resources"),(0,n.kt)("p",null,"In order for tag-based authorization to work, tags must be applied on a customer's resources managed by a SaaS (API) service, and attached to authorization ",(0,n.kt)("a",{parentName:"p",href:"/docs/concepts/authorization-principles"},"principals")," that can operate on those resources. For example, a user ",(0,n.kt)("em",{parentName:"p"},"(a principal)")," in the marketing department ",(0,n.kt)("em",{parentName:"p"},"(a tag)")," should only be able to operate only on the marketing departments\u2019 expense sheets ",(0,n.kt)("em",{parentName:"p"},"(a resource)"),". API subscribers can apply tags to Users, Client Keys and Roles via the Katanemo API Service Console or via the Katanemo SDK. Tag key/value pairs are set in the JWT session token generated by Katanemo for the principal and matched against tags available on the OpenAPI defined resource."),(0,n.kt)("p",null,(0,n.kt)("em",{parentName:"p"},"Note"),": If you are using an OIDC-compliant Idp integration with Katanemo (via Connections), you will need to ensure that the session token generated by the IDP includes tags for Katanemo to perform authorization against for federated users."),(0,n.kt)("h4",{id:"tag-storage-in-katanemo"},"Tag Storage in Katanemo"),(0,n.kt)("p",null,"Katanemo offers a tagging API for developers to easily store tags for resources created by an API Subscriber. With the ",(0,n.kt)("a",{parentName:"p",href:"#"},"Tagging API"),", developers offload undifferentiated ABAC (attribute-based authorization control) infrastructure muck so that they can continue to focus just on what matters most to their business: building capabilities on behalf of their customers."),(0,n.kt)("p",null,"Katanemo\u2019s focus on OpenAPI (once again) makes the storage and retrieval of resource Tags simple. With an OpenAPI spec developers can neatly capture resource schemas, and Katanemo uses those schemas to store and retrieve Tags. "),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-yaml"},'...\npaths:\n  "/catalog/images/{imageId}":\n    get:\n      operationId: getImage\n      parameters:\n          - name: imageId\n            in: path\n            required: true\n            schema:\n                type: string\n                pattern: ^[a-zA-Z0-9\\-]{3,128}$\n')),(0,n.kt)("p",null,"For example, the OpenAPI spec above captures the definition of an ",(0,n.kt)("inlineCode",{parentName:"p"},"{imageId}")," resource. Developers simply call the Tagging API with the imageId resource name, a resource id, and list of tags that must be associated with that image resource. For example, when a user calls the API ",(0,n.kt)("inlineCode",{parentName:"p"},"/catalog/images/12345"),", Katanemo matches ",(0,n.kt)("a",{parentName:"p",href:"./crypto-offload-and-sessions-tokens"},"session token")," tags with tags on that image resource. If ",(0,n.kt)("strong",{parentName:"p"},"all")," the tags associated with the image resource 12345 match tags in the session token of the principal, then the ",(0,n.kt)("a",{parentName:"p",href:"./authorization-evaluation-logic"},"authorization evaluation logic")," proceeds to the next step."),(0,n.kt)("p",null,"Tags consist of a key name and a value, and the following restrictions apply to tags:"),(0,n.kt)("ol",null,(0,n.kt)("li",{parentName:"ol"},"Resource names must be fully qualified in the OpenAPI specification"),(0,n.kt)("li",{parentName:"ol"},"Resource ids should be unique and must match the schema defined in the OpenAPI specification"),(0,n.kt)("li",{parentName:"ol"},"You can optionally pass in a namespace qualifier if resource ids are not globally scoped. The combination of namespace and resource id must be unique so that Katanemo can store and retrieve tags effectively"),(0,n.kt)("li",{parentName:"ol"},"Maximum tag key length: 127 Unicode characters in UTF-8"),(0,n.kt)("li",{parentName:"ol"},"Maximum tag value length: 255 Unicode characters in UTF-8. You can also include a list of tag values for a unique tag key via the ",(0,n.kt)("inlineCode",{parentName:"li"},"[]")," directive. For example: ",(0,n.kt)("inlineCode",{parentName:"li"},'\u201cdepartment": [ "finance", "hr", "legal" ].')),(0,n.kt)("li",{parentName:"ol"},"Tag keys and values are case insensitive."),(0,n.kt)("li",{parentName:"ol"},"Maximum number of tag keys per resource: 50")),(0,n.kt)("h2",{id:"access-tags"},"Access Tags"),(0,n.kt)("p",null,"The above approach is commonly referred to as attribute-based access control. Tags are essentially attributes of principals (for e.g. a User) and resources. This works well for access control mechanisms of resources belonging to a single (domain) subscriber ",(0,n.kt)("a",{parentName:"p",href:"/docs/accounts"},"account")," - they can apply tags to their resources and principals without friction. But this approach becomes cumbersome if resources owned by one account should be accessible to other accounts. For example, Katanemo\u2019s Service resource is owned by an API developer (a subscriber of Katanemo), ",(0,n.kt)("em",{parentName:"p"},"but how should an API developer give access to select Service(s) to other potential subscribers?")),(0,n.kt)("p",null,"Traditionally, access and authorization mechanisms are buried deep in complex code paths with clunky if/else statements, but Katanemo solves this problem elegantly via Access Tags: RESTful access semantics encoded as tags to enable cross account resource sharing in simple, yet strictly-accurate ways. "),(0,n.kt)("p",null,"For example, when you want to make your ",(0,n.kt)("a",{parentName:"p",href:"/docs/concepts/service"},"OpenAPI Service")," instance accessible to anyone, simply add the following tag to your Service instance: "),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-yaml"},"access-tag:GET:*principals:[*]\n")),(0,n.kt)("p",null,"In the above example, ",(0,n.kt)("inlineCode",{parentName:"p"},"access-tag:GET:*")," allows GET operations on any RESTful path to the resource, ",(0,n.kt)("inlineCode",{parentName:"p"},"{serviceId}")," is the Service resource to which access is being granted. And, ",(0,n.kt)("inlineCode",{parentName:"p"},"principals")," are ",(0,n.kt)("a",{parentName:"p",href:"/docs/concepts/authorization-principles"},"authorization principals")," to whom access should be granted; ",(0,n.kt)("inlineCode",{parentName:"p"},"[*]")," denotes anyone. Now, when a potential subscriber navigates to ",(0,n.kt)("a",{parentName:"p",href:"https://Katanemo.com/sign-up/%7Bservice-id%7D"},"https://Katanemo.com/sign-up/{service-id}"),", Katanemo grants access to that sign-up page."),(0,n.kt)("h3",{id:"system-defined-access-tags"},"System Defined Access Tags"),(0,n.kt)("p",null,"To facilitate critical interactions between SaaS developers and their customers, you\u2019ll notice that Katanemo adds tags on select Katanemo API resources (like /org/{accountId}). These system-defined Access Tags can only be updated or deleted by Katanemo. "),(0,n.kt)("p",null,"For example, when a customer creates a Role for a particular SaaS service, the Role resource is owned by that customer. But developers must be able to get Role details so that their ",(0,n.kt)("a",{parentName:"p",href:"../how-to-guides/katanemo-sdk-integration"},"ARC")," instances can pull role policies and perform auth(z). Katanemo adds the following Access Tag:"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-yaml"},"katanemo:access-tag:GET:*:{role-id}:prinicipals=[999113]\n")),(0,n.kt)("p",null,"999113 is the Katanemo account ID of the developer that needs policy details of the Role owned by their customer."))}m.isMDXComponent=!0}}]);