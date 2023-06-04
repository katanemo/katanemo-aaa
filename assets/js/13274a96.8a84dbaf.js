"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[162],{4137:(e,t,a)=>{a.d(t,{Zo:()=>u,kt:()=>f});var n=a(7294);function o(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function r(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function i(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?r(Object(a),!0).forEach((function(t){o(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):r(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function s(e,t){if(null==e)return{};var a,n,o=function(e,t){if(null==e)return{};var a,n,o={},r=Object.keys(e);for(n=0;n<r.length;n++)a=r[n],t.indexOf(a)>=0||(o[a]=e[a]);return o}(e,t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);for(n=0;n<r.length;n++)a=r[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(o[a]=e[a])}return o}var c=n.createContext({}),p=function(e){var t=n.useContext(c),a=t;return e&&(a="function"==typeof e?e(t):i(i({},t),e)),a},u=function(e){var t=p(e.components);return n.createElement(c.Provider,{value:t},e.children)},l="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},m=n.forwardRef((function(e,t){var a=e.components,o=e.mdxType,r=e.originalType,c=e.parentName,u=s(e,["components","mdxType","originalType","parentName"]),l=p(a),m=o,f=l["".concat(c,".").concat(m)]||l[m]||d[m]||r;return a?n.createElement(f,i(i({ref:t},u),{},{components:a})):n.createElement(f,i({ref:t},u))}));function f(e,t){var a=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var r=a.length,i=new Array(r);i[0]=m;var s={};for(var c in t)hasOwnProperty.call(t,c)&&(s[c]=t[c]);s.originalType=e,s[l]="string"==typeof e?e:o,i[1]=s;for(var p=2;p<r;p++)i[p]=a[p];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}m.displayName="MDXCreateElement"},735:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>c,contentTitle:()=>i,default:()=>d,frontMatter:()=>r,metadata:()=>s,toc:()=>p});var n=a(7462),o=(a(7294),a(4137));const r={sidebar_position:3},i="Developer Quick Start Guide",s={unversionedId:"developer-quick-start-guide",id:"developer-quick-start-guide",title:"Developer Quick Start Guide",description:"Katanemo supports an OpenAPI-based development workflow. You simply define RESTful APIs just like you would today via the OpenAPI spec, publish that spec to Katanemo and instantly add user/federated authentication to your application and build powerful privacy and collaboration features via Katanemo\u2019s Role-based Access Control (RBAC) and Attribute-based Access Control (ABAC) capabilities. Katanemo offers a holistic approach to identity, privacy, and safe collaboration that empowers developers to focus on what matters most: moving fast in building features and capabilities unique to their business.",source:"@site/docs/developer-quick-start-guide.md",sourceDirName:".",slug:"/developer-quick-start-guide",permalink:"/katanemo-aaa/docs/developer-quick-start-guide",draft:!1,tags:[],version:"current",sidebarPosition:3,frontMatter:{sidebar_position:3},sidebar:"defaultSidebar",previous:{title:"Accounts",permalink:"/katanemo-aaa/docs/accounts"},next:{title:"Customer Quick Start Guide",permalink:"/katanemo-aaa/docs/customer-quick-start"}},c={},p=[{value:"<strong>Step 1: Create a Service in Katanemo via your OpenAPI service specification</strong>",id:"step-1-create-a-service-in-katanemo-via-your-openapi-service-specification",level:2},{value:"<strong>Step 2: Integrate the Katanemo SDK for authentication and authorization.</strong>",id:"step-2-integrate-the-katanemo-sdk-for-authentication-and-authorization",level:2}],u={toc:p},l="wrapper";function d(e){let{components:t,...r}=e;return(0,o.kt)(l,(0,n.Z)({},u,r,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"developer-quick-start-guide"},"Developer Quick Start Guide"),(0,o.kt)("p",null,"Katanemo supports an OpenAPI-based development workflow. You simply define RESTful APIs just like you would today via the ",(0,o.kt)("a",{parentName:"p",href:"https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md"},"OpenAPI spec"),", publish that spec to Katanemo and instantly add user/federated authentication to your application and build powerful privacy and collaboration features via Katanemo\u2019s Role-based Access Control (RBAC) and Attribute-based Access Control (",(0,o.kt)("a",{parentName:"p",href:"https://en.wikipedia.org/wiki/Attribute-based_access_control"},"ABAC"),") capabilities. Katanemo offers a holistic approach to identity, privacy, and safe collaboration that empowers developers to focus on what matters most: moving fast in building features and capabilities unique to their business."),(0,o.kt)("h2",{id:"step-1-create-a-service-in-katanemo-via-your-openapi-service-specification"},(0,o.kt)("strong",{parentName:"h2"},"Step 1: Create a Service in Katanemo via your OpenAPI service specification")),(0,o.kt)("p",null,"To get started, you must have a Katanemo account. If you don\u2019t already have one, visit the ",(0,o.kt)("a",{parentName:"p",href:"https://console.katanemo.com/sign-up"},"Katanemo signup page")," to register. You are now ready to publish your ",(0,o.kt)("a",{parentName:"p",href:"https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md"},"OpenAPI")," spec to Katanemo, and in minutes offer self-service on-boarding workflows, powerful authorization and auditing capabilities for your SaaS APIs."),(0,o.kt)("p",null,(0,o.kt)("img",{alt:"service-dashboard.png",src:a(6057).Z,width:"1999",height:"1625"})),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},"Give your service a name, a description and configure a ",(0,o.kt)("em",{parentName:"li"},"redirect_uri")," where Katanemo redirects users upon a successful sign-up/log-in attempt."),(0,o.kt)("li",{parentName:"ol"},"Click ",(0,o.kt)("strong",{parentName:"li"},"Publish")," to create a Katanemo Service."),(0,o.kt)("li",{parentName:"ol"},"Copy the ",(0,o.kt)("strong",{parentName:"li"},"Sign-Up/Login")," ",(0,o.kt)("strong",{parentName:"li"},"URL"),"s generated by Katanemo. You will need to add these links to your website so that your customers can easily sign-up and login to your SaaS application.")),(0,o.kt)("h2",{id:"step-2-integrate-the-katanemo-sdk-for-authentication-and-authorization"},(0,o.kt)("strong",{parentName:"h2"},"Step 2: Integrate the Katanemo SDK for authentication and authorization.")),(0,o.kt)("p",null,"Once you have registered your service with Katanemo, you can use the Katanemo SDK to perform authorization and authentication. To get started:"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},"Sign in to the ",(0,o.kt)("a",{parentName:"li",href:"https://console.katanemo.com/service"},"Katanemo SaaS developer console"),", and choose ",(0,o.kt)("strong",{parentName:"li"},"Create New ",(0,o.kt)("a",{parentName:"strong",href:"./concepts/keys"},"Keys")),". ",(0,o.kt)("em",{parentName:"li"},"Note"),": a client key is bound (by default) to a default role that can perform all Katanemo API actions. For more information on roles, see ",(0,o.kt)("a",{parentName:"li",href:"./concepts/roles"},"Roles"),".")),(0,o.kt)("ol",{start:2},(0,o.kt)("li",{parentName:"ol"},"Use the Katanemo SDK to enforce authentication and authorization for your SaaS application. The sample python code below shows how you can add authentication and fine-grained authorization via a few line of code.")),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},'# Katanemo Authentication\n\nimport http\nimport os\nfrom katanemo_sdk import arc\n\ndef init():\n    api_key = os.getenv("KATANEMO_CLIENT_KEY")\n    api_key_secret = os.getenv("KATANEMO_CLIENT_SECRET")\n    service_id = os.getenv("KATANEMO_SERVICE_ID")\n    arc.configure(api_key, api_key_secret, service_id)\n\ndef authorize(request: http.Request, next_handler: http.Handler):\n    response, error = arc.authorize(request)\n    if error is not None:\n        # Handle authentication and authorization error\n        return response\n    return next_handler\n\n')))}d.isMDXComponent=!0},6057:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/service-dashboard-026189bf0901e08caeafa447980358ea.png"}}]);