"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[403],{4137:(e,t,n)=>{n.d(t,{Zo:()=>l,kt:()=>y});var a=n(7294);function o(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function r(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?r(Object(n),!0).forEach((function(t){o(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):r(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,a,o=function(e,t){if(null==e)return{};var n,a,o={},r=Object.keys(e);for(a=0;a<r.length;a++)n=r[a],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);for(a=0;a<r.length;a++)n=r[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var c=a.createContext({}),p=function(e){var t=a.useContext(c),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},l=function(e){var t=p(e.components);return a.createElement(c.Provider,{value:t},e.children)},u="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},f=a.forwardRef((function(e,t){var n=e.components,o=e.mdxType,r=e.originalType,c=e.parentName,l=s(e,["components","mdxType","originalType","parentName"]),u=p(n),f=o,y=u["".concat(c,".").concat(f)]||u[f]||d[f]||r;return n?a.createElement(y,i(i({ref:t},l),{},{components:n})):a.createElement(y,i({ref:t},l))}));function y(e,t){var n=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var r=n.length,i=new Array(r);i[0]=f;var s={};for(var c in t)hasOwnProperty.call(t,c)&&(s[c]=t[c]);s.originalType=e,s[u]="string"==typeof e?e:o,i[1]=s;for(var p=2;p<r;p++)i[p]=n[p];return a.createElement.apply(null,i)}return a.createElement.apply(null,n)}f.displayName="MDXCreateElement"},1608:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>c,contentTitle:()=>i,default:()=>d,frontMatter:()=>r,metadata:()=>s,toc:()=>p});var a=n(7462),o=(n(7294),n(4137));const r={sidebar_position:9},i="Crypto Offload",s={unversionedId:"concepts/crypto-offload-and-sessions-tokens",id:"concepts/crypto-offload-and-sessions-tokens",title:"Crypto Offload",description:"Katanemo is an OIDC compliant 3xA service, which means that it generates an idtoken, an accesstoken for users and API keys, and optionally a refresh_token as per the ODIC spec. These tokens are encrypted with an RSA256 (RS-256) signature key. You can retrieve the RSA public key via Katanemo\u2019s JSON Web Key Set (JWKS).",source:"@site/docs/concepts/crypto-offload-and-sessions-tokens.md",sourceDirName:"concepts",slug:"/concepts/crypto-offload-and-sessions-tokens",permalink:"/katanemo-aaa/docs/concepts/crypto-offload-and-sessions-tokens",draft:!1,tags:[],version:"current",sidebarPosition:9,frontMatter:{sidebar_position:9},sidebar:"defaultSidebar",previous:{title:"Scopes (OAuth 2.0)",permalink:"/katanemo-aaa/docs/concepts/scopes-oauth"},next:{title:"Authorization Evaluation Logic",permalink:"/katanemo-aaa/docs/concepts/authorization-evaluation-logic"}},c={},p=[],l={toc:p},u="wrapper";function d(e){let{components:t,...n}=e;return(0,o.kt)(u,(0,a.Z)({},l,n,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"crypto-offload"},"Crypto Offload"),(0,o.kt)("p",null,"Katanemo is an OIDC compliant 3xA service, which means that it generates an ",(0,o.kt)("inlineCode",{parentName:"p"},"id_token"),", an ",(0,o.kt)("inlineCode",{parentName:"p"},"access_token")," for users and API keys, and optionally a ",(0,o.kt)("inlineCode",{parentName:"p"},"refresh_token")," as per the ODIC spec. These tokens are encrypted with an RSA256 (RS-256) signature key. You can retrieve the RSA public key via Katanemo\u2019s JSON Web Key Set (JWKS)."),(0,o.kt)("p",null,"If you are using Katanemo as an IDP, it creates a token that contains information about the user and additional meta-data like Tags and Role detail, and signs the JWT token using its private key. Katanemo secures the private key, which is unique per tenant (developer or subscriber). To verify that the token is valid and originated from Katanemo, your application can validate the token\u2019s signature using the public key.  For example, you'll provide the client with the JWKS endpoint which exposes Katanemo\u2019 signing keys. Using the getSigningKey you can then get the signing key that matches a specific kid."),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-js"},"const jwksClient = require('jwks-rsa');\nconst client = jwksClient({\n  jwksUri: 'https://api.katanemo.com/service/{serviceId}/.well-known/jwks.json',\n  requestHeaders: {}, // Optional\n  timeout: 30000 // Defaults to 30s\n});\n\nconst kid = 'RkI5MjI5OUY5ODc1N0Q4QzM0OUYzNkVGMTJDOUEzQkFCOTU3NjE2Rg'; \nconst key = await client.getSigningKey(kid);\nconst signingKey = key.getPublicKey();\n")))}d.isMDXComponent=!0}}]);