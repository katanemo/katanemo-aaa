"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[773],{4137:(e,t,a)=>{a.d(t,{Zo:()=>u,kt:()=>h});var o=a(7294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function n(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,o)}return a}function s(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?n(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):n(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function i(e,t){if(null==e)return{};var a,o,r=function(e,t){if(null==e)return{};var a,o,r={},n=Object.keys(e);for(o=0;o<n.length;o++)a=n[o],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);for(o=0;o<n.length;o++)a=n[o],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var l=o.createContext({}),c=function(e){var t=o.useContext(l),a=t;return e&&(a="function"==typeof e?e(t):s(s({},t),e)),a},u=function(e){var t=c(e.components);return o.createElement(l.Provider,{value:t},e.children)},p="mdxType",m={inlineCode:"code",wrapper:function(e){var t=e.children;return o.createElement(o.Fragment,{},t)}},d=o.forwardRef((function(e,t){var a=e.components,r=e.mdxType,n=e.originalType,l=e.parentName,u=i(e,["components","mdxType","originalType","parentName"]),p=c(a),d=r,h=p["".concat(l,".").concat(d)]||p[d]||m[d]||n;return a?o.createElement(h,s(s({ref:t},u),{},{components:a})):o.createElement(h,s({ref:t},u))}));function h(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var n=a.length,s=new Array(n);s[0]=d;var i={};for(var l in t)hasOwnProperty.call(t,l)&&(i[l]=t[l]);i.originalType=e,i[p]="string"==typeof e?e:r,s[1]=i;for(var c=2;c<n;c++)s[c]=a[c];return o.createElement.apply(null,s)}return o.createElement.apply(null,a)}d.displayName="MDXCreateElement"},9054:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>l,contentTitle:()=>s,default:()=>m,frontMatter:()=>n,metadata:()=>i,toc:()=>c});var o=a(7462),r=(a(7294),a(4137));const n={sidebar_position:2},s="How to Modify the Default \u201call tags must match\u201d Behavior of Katanemo?",i={unversionedId:"how-to-guides/all-tags-must-match-modification",id:"how-to-guides/all-tags-must-match-modification",title:"How to Modify the Default \u201call tags must match\u201d Behavior of Katanemo?",description:"Katanemo\u2019s default behavior is to match all tags associated with a resource against tags present in the session token (of the principal) making the call. However, you can alter this default behavior for your particular use case by adding the \u201cwhere\u201d clause to your Role definition (aka. Role policies).",source:"@site/docs/how-to-guides/all-tags-must-match-modification.md",sourceDirName:"how-to-guides",slug:"/how-to-guides/all-tags-must-match-modification",permalink:"/katanemo-aaa/docs/how-to-guides/all-tags-must-match-modification",draft:!1,tags:[],version:"current",sidebarPosition:2,frontMatter:{sidebar_position:2},sidebar:"defaultSidebar",previous:{title:"How to Integrate the Katanemo SDK in your application (Authorization Runtime Client)?",permalink:"/katanemo-aaa/docs/how-to-guides/katanemo-sdk-integration"},next:{title:"How to Configure a New OIDC connection?",permalink:"/katanemo-aaa/docs/how-to-guides/oidc-connection"}},l={},c=[],u={toc:c},p="wrapper";function m(e){let{components:t,...a}=e;return(0,r.kt)(p,(0,o.Z)({},u,a,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"how-to-modify-the-default-all-tags-must-match-behavior-of-katanemo"},"How to Modify the Default \u201call tags must match\u201d Behavior of Katanemo?"),(0,r.kt)("p",null,"Katanemo\u2019s default behavior is to match ",(0,r.kt)("strong",{parentName:"p"},"all")," tags associated with a resource against tags present in the session token (of the principal) making the call. However, you can alter this default behavior for your particular use case by adding the \u201cwhere\u201d clause to your Role definition (aka. Role policies)."),(0,r.kt)("p",null,(0,r.kt)("em",{parentName:"p"},"Where clause (via Role policies)"),"\nIn cases where the default behavior of ",(0,r.kt)("strong",{parentName:"p"},"all")," tags associated with a resource doesn\u2019t satisfy your particular use case, you can define conditional policies using the \u201cwhere\u201d clause to match tags as per your use case. Note, the above UI experience hides the details of how to construct permission boundaries of a Role, however the following use cases showcase ",(0,r.kt)("em",{parentName:"p"},"policies")," using the OpenAPI-based semantics and the \u201cwhere\u201d clause to construct simple, yet highly powerful authorization rules."),(0,r.kt)("p",null,(0,r.kt)("em",{parentName:"p"},"Use Case #1: Some users will have READ/WRITE access to dev clusters, and READ access to stage & prod clusters.")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-yaml"}," allow:\n  api: \n    \u2013 PUT:/cluster/{clusterId}\n    \u2013 GET:/cluster/{clusterId}\n  where: $resourceTags:clustertag = 'dev'\n  api:\n   - GET:/cluster/{clusterId}\n  where: $resourceTags:clustertag IN ('staging', 'production')\n")),(0,r.kt)("p",null,(0,r.kt)("em",{parentName:"p"},"Use Case #2: Some users will have READ/WRITE access to dev clusters of type EKS.")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-yaml"}," allow:\n  api: \n   \u2013 PUT:/cluster/{clusterId}\n   \u2013 GET:/cluster/{clusterId}\n  where: $resourceTags:clustertag = 'EKS'\n")),(0,r.kt)("p",null,(0,r.kt)("em",{parentName:"p"},"Use Case #3: Some users will have the ability to create promotions only up to a maximum of 10% off.")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-yaml"}," allow:\n  api: \n   \u2013 POST:/api-offers/promo/create\n  where: $request:promo:discount:value < 10 AND $request:promo:targetProducts:value IN ('SKU-124')\n")),(0,r.kt)("p",null,(0,r.kt)("em",{parentName:"p"},"Use Case #3a: Some users will have the ability to UPDATE promotions where tag = \u201cindependence-day\u201d")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-yaml"},' allow:\n  api: \n   \u2013 PUT:/api-offers/promo/update/{promoId}\n  where: $resourceTag:note = "independence day promos"\n')),(0,r.kt)("p",null,(0,r.kt)("inlineCode",{parentName:"p"},"$resourceTags,")," ",(0,r.kt)("inlineCode",{parentName:"p"},"$request"),", and ",(0,r.kt)("inlineCode",{parentName:"p"},"$principalTags")," are system variables that can be used in the ",(0,r.kt)("em",{parentName:"p"},"where")," clause to get tags for the resource or the principal, respectively. The ",(0,r.kt)("inlineCode",{parentName:"p"},"$resourceTags:tagkey")," directive allows you to look for a particular tag key for a resource."))}m.isMDXComponent=!0}}]);