"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[185],{4137:(e,t,n)=>{n.d(t,{Zo:()=>d,kt:()=>f});var o=n(7294);function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function r(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,o)}return n}function a(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?r(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):r(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function c(e,t){if(null==e)return{};var n,o,i=function(e,t){if(null==e)return{};var n,o,i={},r=Object.keys(e);for(o=0;o<r.length;o++)n=r[o],t.indexOf(n)>=0||(i[n]=e[n]);return i}(e,t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);for(o=0;o<r.length;o++)n=r[o],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(i[n]=e[n])}return i}var s=o.createContext({}),l=function(e){var t=o.useContext(s),n=t;return e&&(n="function"==typeof e?e(t):a(a({},t),e)),n},d=function(e){var t=l(e.components);return o.createElement(s.Provider,{value:t},e.children)},p="mdxType",u={inlineCode:"code",wrapper:function(e){var t=e.children;return o.createElement(o.Fragment,{},t)}},m=o.forwardRef((function(e,t){var n=e.components,i=e.mdxType,r=e.originalType,s=e.parentName,d=c(e,["components","mdxType","originalType","parentName"]),p=l(n),m=i,f=p["".concat(s,".").concat(m)]||p[m]||u[m]||r;return n?o.createElement(f,a(a({ref:t},d),{},{components:n})):o.createElement(f,a({ref:t},d))}));function f(e,t){var n=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var r=n.length,a=new Array(r);a[0]=m;var c={};for(var s in t)hasOwnProperty.call(t,s)&&(c[s]=t[s]);c.originalType=e,c[p]="string"==typeof e?e:i,a[1]=c;for(var l=2;l<r;l++)a[l]=n[l];return o.createElement.apply(null,a)}return o.createElement.apply(null,n)}m.displayName="MDXCreateElement"},9782:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>s,contentTitle:()=>a,default:()=>u,frontMatter:()=>r,metadata:()=>c,toc:()=>l});var o=n(7462),i=(n(7294),n(4137));const r={sidebar_position:3},a="How to Configure a New OIDC connection?",c={unversionedId:"how-to-guides/oidc-connection",id:"how-to-guides/oidc-connection",title:"How to Configure a New OIDC connection?",description:"Each SSO Identity Provider requires specific information to create and configure a new Connection. Often, the information required to create a Connection will differ by Identity Provider. To create an OpenID Connect (OIDC) Connection, you\u2019ll need five pieces of information: a Redirect URI, a Client ID, a Client Secret, a Discovery Endpoint, and a Role.",source:"@site/docs/how-to-guides/oidc-connection.md",sourceDirName:"how-to-guides",slug:"/how-to-guides/oidc-connection",permalink:"/katanemo-aaa/docs/how-to-guides/oidc-connection",draft:!1,tags:[],version:"current",sidebarPosition:3,frontMatter:{sidebar_position:3},sidebar:"defaultSidebar",previous:{title:'How to Modify the default "tagging match\u201d behavior of Katanemo?',permalink:"/katanemo-aaa/docs/how-to-guides/all-tags-must-match-modification"},next:{title:"How to Configure a New Okta SAML connection?",permalink:"/katanemo-aaa/docs/how-to-guides/okta-saml-connection"}},s={},l=[],d={toc:l},p="wrapper";function u(e){let{components:t,...n}=e;return(0,i.kt)(p,(0,o.Z)({},d,n,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"how-to-configure-a-new-oidc-connection"},"How to Configure a New OIDC connection?"),(0,i.kt)("p",null,"Each SSO Identity Provider requires specific information to create and configure a new ",(0,i.kt)("a",{parentName:"p",href:"../concepts/connections"},"Connection"),". Often, the information required to create a Connection will differ by Identity Provider. To create an OpenID Connect (OIDC) Connection, you\u2019ll need five pieces of information: a Redirect URI, a Client ID, a Client Secret, a Discovery Endpoint, and a Role."),(0,i.kt)("p",null,"Katanemo provides the Redirect URI. It\u2019s readily available in your Connection Settings in the Katanemo Dashboard. The Redirect URI is the location an Identity Provider redirects its authentication response to. In order to integrate you\u2019ll need the Client ID, Client Secret, the Discovery Endpoint, and the Role that is associated with the Connection."),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("strong",{parentName:"li"},"Create an Application with your IdP")," - For SSO to properly function with your Identity Provider, you\u2019ll need to create and configure your OpenID Connect application to support the authorization code grant type and have the redirect URI from Katanemo listed as your login or signup redirect URI."),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("strong",{parentName:"li"},"Add claims to the ID token")," - Add the sub, email, given_name (or name), and family_name claims to the user ID token in your OIDC provider settings. These claims map to the idp_id, email, first_name, and last_name attributes in the user profile returned by Katanemo. For many providers, these claims are included by default, but for other providers you will need to add these claims."),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("strong",{parentName:"li"},"Provide your Client Credentials")," - After creating an OpenID Connection application, a Client ID and Client Secret will be provisioned for you by your Identity Provider. Enter these details in your Connection settings in the Service Console Dashboard."),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("strong",{parentName:"li"},"Add Discovery Endpoint")," - Discovery Endpoint contains important configuration information. Enter this endpoint in your Connection settings in the Katanemo Dashboard. It will always end with ",(0,i.kt)("inlineCode",{parentName:"li"},"/.well-known/openid-configuration")," as described in the OpenID Provider Configuration Request documentation. You can confirm that the endpoint is correct by entering it in a browser window. If there is a JSON object with metadata about the connection returned, the endpoint is correct. "),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("strong",{parentName:"li"},"Configure Role for Connection")," - Before a connection can be made active, you must associate a Role that was previously created. Users that SSO will be assigned this Role against which API operations will be authorized.")),(0,i.kt)("p",null,"Role Mappings to Connections Object:"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},"Katanemo supports creating multiple Connections in a single ",(0,i.kt)("a",{parentName:"li",href:"../concepts/organizations"},"Organization")," which allows you to assign different upstream user groups the appropriate SSO link for their specific access to service capabilities. For example you can create a Connections SSO link shared with \u2018interns\u2019, and another Connections SSO link shared with the \u2018senior developers\u2019 group."),(0,i.kt)("li",{parentName:"ol"},'You can also map OIDC scopes to Roles. For example, if you want to map the user\u2019s group to a Role in Katanemo, you can configure the following mapping "groups:admins=$role-id\u201d in the Connections object. The Connections default role is not used if Katanemo can find a valid scope to role mapping in the SSO request. Note, attribute names and values are case sensitive.')))}u.isMDXComponent=!0}}]);