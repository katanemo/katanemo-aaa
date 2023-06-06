"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[389],{4137:(e,t,a)=>{a.d(t,{Zo:()=>p,kt:()=>d});var o=a(7294);function n(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function r(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,o)}return a}function i(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?r(Object(a),!0).forEach((function(t){n(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):r(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function s(e,t){if(null==e)return{};var a,o,n=function(e,t){if(null==e)return{};var a,o,n={},r=Object.keys(e);for(o=0;o<r.length;o++)a=r[o],t.indexOf(a)>=0||(n[a]=e[a]);return n}(e,t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);for(o=0;o<r.length;o++)a=r[o],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(n[a]=e[a])}return n}var l=o.createContext({}),c=function(e){var t=o.useContext(l),a=t;return e&&(a="function"==typeof e?e(t):i(i({},t),e)),a},p=function(e){var t=c(e.components);return o.createElement(l.Provider,{value:t},e.children)},u="mdxType",m={inlineCode:"code",wrapper:function(e){var t=e.children;return o.createElement(o.Fragment,{},t)}},f=o.forwardRef((function(e,t){var a=e.components,n=e.mdxType,r=e.originalType,l=e.parentName,p=s(e,["components","mdxType","originalType","parentName"]),u=c(a),f=n,d=u["".concat(l,".").concat(f)]||u[f]||m[f]||r;return a?o.createElement(d,i(i({ref:t},p),{},{components:a})):o.createElement(d,i({ref:t},p))}));function d(e,t){var a=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var r=a.length,i=new Array(r);i[0]=f;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s[u]="string"==typeof e?e:n,i[1]=s;for(var c=2;c<r;c++)i[c]=a[c];return o.createElement.apply(null,i)}return o.createElement.apply(null,a)}f.displayName="MDXCreateElement"},4077:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>l,contentTitle:()=>i,default:()=>m,frontMatter:()=>r,metadata:()=>s,toc:()=>c});var o=a(7462),n=(a(7294),a(4137));const r={sidebar_position:5},i="How to Configure Field-Level Access Control (and filtering) via Katanemo Roles?",s={unversionedId:"how-to-guides/field-level-access-control-via-katanemo",id:"how-to-guides/field-level-access-control-via-katanemo",title:"How to Configure Field-Level Access Control (and filtering) via Katanemo Roles?",description:"Katanemo allows you (a subscriber of a service) to easily construct Roles via OpenAPI semantics (RESTful paths and http methods) that limit operations for a user/machine. This approach requires little to no learning curve in establishing simple yet powerful authorization rules for consuming a service.",source:"@site/docs/how-to-guides/field-level-access-control-via-katanemo.md",sourceDirName:"how-to-guides",slug:"/how-to-guides/field-level-access-control-via-katanemo",permalink:"/docs/how-to-guides/field-level-access-control-via-katanemo",draft:!1,tags:[],version:"current",sidebarPosition:5,frontMatter:{sidebar_position:5},sidebar:"defaultSidebar",previous:{title:"How to Configure a New Okta SAML connection?",permalink:"/docs/how-to-guides/okta-saml-connection"},next:{title:"How to use an existing Identity Provider (like Okta, Auth0) with Katanemo?",permalink:"/docs/how-to-guides/existing-identity-provider"}},l={},c=[],p={toc:c},u="wrapper";function m(e){let{components:t,...a}=e;return(0,n.kt)(u,(0,o.Z)({},p,a,{components:t,mdxType:"MDXLayout"}),(0,n.kt)("h1",{id:"how-to-configure-field-level-access-control-and-filtering-via-katanemo-roles"},"How to Configure Field-Level Access Control (and filtering) via Katanemo Roles?"),(0,n.kt)("p",null,"Katanemo allows you (a subscriber of a service) to easily construct Roles via OpenAPI semantics (RESTful paths and http methods) that limit operations for a user/machine. This approach requires ",(0,n.kt)("em",{parentName:"p"},"little to no learning curve")," in establishing simple yet powerful authorization rules for consuming a service."),(0,n.kt)("p",null,"Using the same OpenAPI approach, Katanemo also allows you to construct field-level access controls. This is useful if you want certain users or machines to only operate on particular fields of a resource. For example, the following policy allows you to do a PUT operation on the ",(0,n.kt)("em",{parentName:"p"},"metadata")," OR ",(0,n.kt)("em",{parentName:"p"},"nodeGroups.maxSize")," fields of the cluster resource."),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-yaml"}," allow:\n  apis:\n   - PUT:/cluster/{clusterId}:[metadata, nodeGroups.maxSize]\n  where: $resourceTags:cluster = 'dev' AND $resourceTags:namespace IN ('NS1', 'NS2) \n")),(0,n.kt)("p",null,"In the above example if the user tries to PUT on the following path /cluster/1234 with parameters other than ",(0,n.kt)("em",{parentName:"p"},"metadata")," OR ",(0,n.kt)("em",{parentName:"p"},"nodeGroups.maxSize _the request will be denied by Katanemo\u2019s authorizer. _Note,")," nodeGroups.maxSize is a nested field in this case, which means the presence of any other nested field in nodeGroups will also fail the authorization request. Note, the cluster resource must be defined along with its resource (nested) fields in the OpenAPI spec."),(0,n.kt)("p",null,"Similarly, the following policy allows a user or machine to GET Patient resource data only via the identifier and email fields specified in the query parameters of a GET call"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-yaml"}," allow: \n   apis:\n    - GET:/patient:[identifier, email]\n")),(0,n.kt)("p",null,"In the above example if a user tries to GET /patient with request parameters other than ",(0,n.kt)("em",{parentName:"p"},"identifier or email")," the request will be denied by Katanemo. Note, ",(0,n.kt)("em",{parentName:"p"},"identifier _and _email")," must be defined as \u201c_in: query\u201d _OpenAPI parameters on the Patient resource, else you won\u2019t be able to create the Role policy successfully."),(0,n.kt)("p",null,(0,n.kt)("em",{parentName:"p"},"Filtering (coming soon)")),(0,n.kt)("p",null,"Similarly, if you want to filter fields from responses, you can use Katanemo\u2019s filterResponseAPI that uses Role policies to filter fields on your behalf. For example, the following policy filters out fields metadata.name, vpc.subnets.* and secretsEncryption.keyARN fields in the GET response for a cluster resource."),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-yaml"},"filter:\n   GET:/cluster/{clusterId}:[metadata.name, vpc.subnets.*, secretsEncryption.keyARN]\n")),(0,n.kt)("p",null,"Before the response is sent to the client, you simply call Katanemo\u2019s filterResponse API with the auth token received in the request, and Katanemo\u2019s ARC will filter fields based on the Role\u2019s filter policy, and return the final response object that should be sent upstream to the client/user. You can optionally send in a \u201cmask=","<","string-value-8>\u201d parameter to the filterResponseAPI call and instead of filtering out the fields altogether, it will mask the field values with ","<","string-value-8> so that clients experience doesn\u2019t break inadvertently if the presence of the field name is expected in the response."),(0,n.kt)("p",null,(0,n.kt)("em",{parentName:"p"},"Note"),": The filterResponse API is stateless. So if you support a paginated API, then you must call filterResponse every time you want to filter results back to the caller for a paginated API call."),(0,n.kt)("p",null,(0,n.kt)("em",{parentName:"p"},"Note"),": Today, Katanemo allows you to construct field-level access control (and filtering) policies via a allow-list approach. If there is a use case that warrants us supporting blocklists, then please send feedback to ",(0,n.kt)("a",{parentName:"p",href:"mailto:feedback@katanemo.com"},"feedback@Katanemo.com"),"."))}m.isMDXComponent=!0}}]);