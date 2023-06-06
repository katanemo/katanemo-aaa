"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[175],{4137:(e,t,n)=>{n.d(t,{Zo:()=>l,kt:()=>d});var a=n(7294);function o(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function r(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?r(Object(n),!0).forEach((function(t){o(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):r(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,a,o=function(e,t){if(null==e)return{};var n,a,o={},r=Object.keys(e);for(a=0;a<r.length;a++)n=r[a],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);for(a=0;a<r.length;a++)n=r[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var c=a.createContext({}),p=function(e){var t=a.useContext(c),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},l=function(e){var t=p(e.components);return a.createElement(c.Provider,{value:t},e.children)},u="mdxType",h={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},m=a.forwardRef((function(e,t){var n=e.components,o=e.mdxType,r=e.originalType,c=e.parentName,l=s(e,["components","mdxType","originalType","parentName"]),u=p(n),m=o,d=u["".concat(c,".").concat(m)]||u[m]||h[m]||r;return n?a.createElement(d,i(i({ref:t},l),{},{components:n})):a.createElement(d,i({ref:t},l))}));function d(e,t){var n=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var r=n.length,i=new Array(r);i[0]=m;var s={};for(var c in t)hasOwnProperty.call(t,c)&&(s[c]=t[c]);s.originalType=e,s[u]="string"==typeof e?e:o,i[1]=s;for(var p=2;p<r;p++)i[p]=n[p];return a.createElement.apply(null,i)}return a.createElement.apply(null,n)}m.displayName="MDXCreateElement"},7078:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>c,contentTitle:()=>i,default:()=>h,frontMatter:()=>r,metadata:()=>s,toc:()=>p});var a=n(7462),o=(n(7294),n(4137));const r={sidebar_position:1},i="How to Integrate the Katanemo SDK in your application (Authorization Runtime Client)?",s={unversionedId:"how-to-guides/katanemo-sdk-integration",id:"how-to-guides/katanemo-sdk-integration",title:"How to Integrate the Katanemo SDK in your application (Authorization Runtime Client)?",description:"Katanemo\u2019s Authorization Runtime Client (ARC) is the leight-weight utility that does the intelligent heavy lifting of protecting who can do what on which resource (authorization). As a developer, you can configure ARC at the gateway layer of your SaaS (API) service in minutes. Katanemo offers two primary integration points with varying levels of support to suit your specific environment needs.",source:"@site/docs/how-to-guides/katanemo-sdk-integration.md",sourceDirName:"how-to-guides",slug:"/how-to-guides/katanemo-sdk-integration",permalink:"/docs/how-to-guides/katanemo-sdk-integration",draft:!1,tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"defaultSidebar",previous:{title:"How-To Guides",permalink:"/docs/category/how-to-guides"},next:{title:'How to Modify the default "tagging match\u201d behavior of Katanemo?',permalink:"/docs/how-to-guides/all-tags-must-match-modification"}},c={},p=[{value:"1. Using the Katanemo SDK",id:"1-using-the-katanemo-sdk",level:4},{value:"2. Integrated as part of Amazon API Gateway or NGINX servers or Envoy Proxy",id:"2-integrated-as-part-of-amazon-api-gateway-or-nginx-servers-or-envoy-proxy",level:4}],l={toc:p},u="wrapper";function h(e){let{components:t,...n}=e;return(0,o.kt)(u,(0,a.Z)({},l,n,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"how-to-integrate-the-katanemo-sdk-in-your-application-authorization-runtime-client"},"How to Integrate the Katanemo SDK in your application (Authorization Runtime Client)?"),(0,o.kt)("p",null,"Katanemo\u2019s Authorization Runtime Client (ARC) is the leight-weight utility that does the intelligent heavy lifting of protecting who can do what on which resource (authorization). As a developer, you can configure ARC at the gateway layer of your SaaS (API) service in minutes. Katanemo offers two primary integration points with varying levels of support to suit your specific environment needs."),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},'import http\nimport os\nfrom katanemo_sdk import arc\n\n def init():\n     api_key = os.getenv("KATANEMO_CLIENT_KEY")\n     api_key_secret = os.getenv("KATANEMO_CLIENT_SECRET")\n     service_id = os.getenv("KATANEMO_SERVICE_ID")\n     arc.configure(api_key, api_key_secret, service_id)\n\n def authorize(request: http.Request, next_handler: http.Handler):\n     response, error = arc.authorize(request)\n     if error is not None:\n         # Handle authentication and authorization error\n         return response\n     return next_handler\n')),(0,o.kt)("h4",{id:"1-using-the-katanemo-sdk"},"1. Using the Katanemo SDK"),(0,o.kt)("p",null,"You can use the Katanemo SDK and embed that in your code (as shown below) to authorize calls that hit your front-end servers. In the code below, ARC will look for and validate the JWT Bearer Token, extract Role details for the authorization principal, and perform authorization. Katanemo\u2019s SDK will make calls to the closest region by looking at the host headers of the HTTP request, and makes all authorization calls to its cloud service over a highly secure TLS 1.3 connection."),(0,o.kt)("p",null,(0,o.kt)("em",{parentName:"p"},"Configure AWS Private Link (interface endpoint) with Katanemo")),(0,o.kt)("p",null,"Katanemo also supports ",(0,o.kt)("a",{parentName:"p",href:"https://aws.amazon.com/privatelink/"},"AWS Private Link")," for workloads hosted in AWS where authorization traffic should not go over the internet. There is no additional charge for using Private Link with Katanemo. Once configured correctly, authorization traffic between your VPC  and the Katanemo endpoint service traverses through the AWS backbone. Follow the steps below to configure AWS Private Link with Katanemo. ",(0,o.kt)("em",{parentName:"p"},"Note: Configuring an AWS Private Link interface endpoint must be done via VPC, Subnet, Security Group semantics (vs OpenAPI RESTful semantics) -\ud83e\udd2e we have made our friends at AWS aware of our feelings here.")),(0,o.kt)("p",null,"To configure the use of AWS Private Link with Katanemo, first navigate to the Katanemo Service Console and select the ",(0,o.kt)("strong",{parentName:"p"},(0,o.kt)("em",{parentName:"strong"},"Service"))," that you are interested to enable Private Link support for. Next select ",(0,o.kt)("strong",{parentName:"p"},(0,o.kt)("em",{parentName:"strong"},"Client Keys ")),"from the left hand menu, and then click on the ",(0,o.kt)("strong",{parentName:"p"},(0,o.kt)("em",{parentName:"strong"},"\u201cAWS Private Link\u201d"))," tab on the top of that page. Here you will be asked to provide your AWS account id ( used for permissions), select the region where you\u2019d like Private Link turned on, and AZs from which traffic will originate from your side to Katanemo\u2019s endpoint service. Click ",(0,o.kt)("strong",{parentName:"p"},"save"),", and in a few moments will get an ",(0,o.kt)("em",{parentName:"p"},"endpoint interface id")," and a ",(0,o.kt)("em",{parentName:"p"},"private DNS name")," that you will use to ",(0,o.kt)("a",{parentName:"p",href:"https://docs.aws.amazon.com/vpc/latest/privatelink/interface-endpoints.html"},"create an interface endpoint "),"in your AWS account."),(0,o.kt)("p",null,"Today, Katanemo supports Private Link in the us-east-1, us-east-2 and the us-west-1 regions, and is deployed in three AZs in each of those regions. When selecting an AZ make sure that the AZ id where Katanemo hosts its\u2019 endpoint service matches the AZ id where traffic will originate from your VPC, else you\u2019ll fail to ",(0,o.kt)("a",{parentName:"p",href:"https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html"},"create an interface endpoint")," in AWS."),(0,o.kt)("p",null,"Now, log in to the AWS management console, and follow steps in their guide to create an ",(0,o.kt)("a",{parentName:"p",href:"https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html"},"interface endpoint"),". Make sure that you select \u201c",(0,o.kt)("strong",{parentName:"p"},"Service Defined\u201d "),"for the ",(0,o.kt)("strong",{parentName:"p"},"DNS record IP type")," and for \u201cService Name\u201d use the endpoint interface id that you got from the previous step above. ",(0,o.kt)("em",{parentName:"p"},"Note"),", Katanemo accepts all interface endpoint connections and manages permissions to its endpoint interface via the AWS account id that you configured in the Katanemo Service Console."),(0,o.kt)("h4",{id:"2-integrated-as-part-of-amazon-api-gateway-or-nginx-servers-or-envoy-proxy"},"2. Integrated as part of Amazon API Gateway or NGINX servers or Envoy Proxy"),(0,o.kt)("p",null,"MISSING SECTION?"))}h.isMDXComponent=!0}}]);