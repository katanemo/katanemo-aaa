"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[101],{4137:(e,t,n)=>{n.d(t,{Zo:()=>l,kt:()=>f});var a=n(7294);function r(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){r(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,a,r=function(e,t){if(null==e)return{};var n,a,r={},o=Object.keys(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var c=a.createContext({}),p=function(e){var t=a.useContext(c),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},l=function(e){var t=p(e.components);return a.createElement(c.Provider,{value:t},e.children)},u="mdxType",m={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},d=a.forwardRef((function(e,t){var n=e.components,r=e.mdxType,o=e.originalType,c=e.parentName,l=s(e,["components","mdxType","originalType","parentName"]),u=p(n),d=r,f=u["".concat(c,".").concat(d)]||u[d]||m[d]||o;return n?a.createElement(f,i(i({ref:t},l),{},{components:n})):a.createElement(f,i({ref:t},l))}));function f(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var o=n.length,i=new Array(o);i[0]=d;var s={};for(var c in t)hasOwnProperty.call(t,c)&&(s[c]=t[c]);s.originalType=e,s[u]="string"==typeof e?e:r,i[1]=s;for(var p=2;p<o;p++)i[p]=n[p];return a.createElement.apply(null,i)}return a.createElement.apply(null,n)}d.displayName="MDXCreateElement"},7338:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>c,contentTitle:()=>i,default:()=>m,frontMatter:()=>o,metadata:()=>s,toc:()=>p});var a=n(7462),r=(n(7294),n(4137));const o={sidebar_position:3},i="Organizations",s={unversionedId:"concepts/organizations",id:"concepts/organizations",title:"Organizations",description:"An organization is a container for SaaS customers to organize roles, manage users, machine (API) keys, SSO settings, and pull audit logs. An organization is created when a SaaS customer signs up to a SaaS application managed by Katanemo. Organizations also act as a thin wrapper to facilitate critical interactions between SaaS developers and SaaS customers. Developers can use Organizations in Katanemo to get detailed information about their customers and to set meta-data like subscription tiers, enabled/disable features, support prompts etc.",source:"@site/docs/concepts/organizations.md",sourceDirName:"concepts",slug:"/concepts/organizations",permalink:"/docs/concepts/organizations",draft:!1,tags:[],version:"current",sidebarPosition:3,frontMatter:{sidebar_position:3},sidebar:"defaultSidebar",previous:{title:"Service",permalink:"/docs/concepts/service"},next:{title:"Roles",permalink:"/docs/concepts/roles"}},c={},p=[],l={toc:p},u="wrapper";function m(e){let{components:t,...n}=e;return(0,r.kt)(u,(0,a.Z)({},l,n,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"organizations"},"Organizations"),(0,r.kt)("p",null,"An organization is a container for SaaS customers to organize roles, manage users, machine (API) keys, SSO settings, and pull audit logs. An organization is created when a SaaS customer signs up to a SaaS application managed by Katanemo. Organizations also act as a thin wrapper to facilitate critical interactions between SaaS developers and SaaS customers. Developers can use Organizations in Katanemo to get detailed information about their customers and to set meta-data like subscription tiers, enabled/disable features, support prompts etc. "),(0,r.kt)("p",null,"For more information on Organizations, please visit the ",(0,r.kt)("a",{parentName:"p",href:"/api#tag/organization"},"Public APIs of Katanemo"),"."))}m.isMDXComponent=!0}}]);