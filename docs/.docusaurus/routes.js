import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/__docusaurus/debug',
    component: ComponentCreator('/__docusaurus/debug', 'ccc'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/config',
    component: ComponentCreator('/__docusaurus/debug/config', '779'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/content',
    component: ComponentCreator('/__docusaurus/debug/content', '8c2'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/globalData',
    component: ComponentCreator('/__docusaurus/debug/globalData', '4ed'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/metadata',
    component: ComponentCreator('/__docusaurus/debug/metadata', '3f4'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/registry',
    component: ComponentCreator('/__docusaurus/debug/registry', 'a01'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/routes',
    component: ComponentCreator('/__docusaurus/debug/routes', '7f0'),
    exact: true
  },
  {
    path: '/markdown-page',
    component: ComponentCreator('/markdown-page', '2c3'),
    exact: true
  },
  {
    path: '/docs',
    component: ComponentCreator('/docs', '43e'),
    routes: [
      {
        path: '/docs/accounts',
        component: ComponentCreator('/docs/accounts', '53b'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/category/concepts',
        component: ComponentCreator('/docs/category/concepts', '499'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/category/how-to-guides',
        component: ComponentCreator('/docs/category/how-to-guides', 'c02'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/category/use-cases',
        component: ComponentCreator('/docs/category/use-cases', '53b'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/concepts/authorization-evaluation-logic',
        component: ComponentCreator('/docs/concepts/authorization-evaluation-logic', '2a6'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/concepts/authorization-principles',
        component: ComponentCreator('/docs/concepts/authorization-principles', '511'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/concepts/connections',
        component: ComponentCreator('/docs/concepts/connections', 'b2b'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/concepts/crypto-offload-and-sessions-tokens',
        component: ComponentCreator('/docs/concepts/crypto-offload-and-sessions-tokens', '052'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/concepts/keys',
        component: ComponentCreator('/docs/concepts/keys', '90a'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/concepts/organizations',
        component: ComponentCreator('/docs/concepts/organizations', 'd4e'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/concepts/resource-access-via-tags',
        component: ComponentCreator('/docs/concepts/resource-access-via-tags', 'c64'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/concepts/roles',
        component: ComponentCreator('/docs/concepts/roles', '47f'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/concepts/scopes-oauth',
        component: ComponentCreator('/docs/concepts/scopes-oauth', '226'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/concepts/service',
        component: ComponentCreator('/docs/concepts/service', '8ee'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/customer-quick-start',
        component: ComponentCreator('/docs/customer-quick-start', '19e'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/developer-quick-start-guide',
        component: ComponentCreator('/docs/developer-quick-start-guide', 'fb1'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/how-to-guides/all-tags-must-match-modification',
        component: ComponentCreator('/docs/how-to-guides/all-tags-must-match-modification', '6d4'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/how-to-guides/existing-identity-provider',
        component: ComponentCreator('/docs/how-to-guides/existing-identity-provider', '1e9'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/how-to-guides/field-level-access-control-via-katanemo',
        component: ComponentCreator('/docs/how-to-guides/field-level-access-control-via-katanemo', '5f9'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/how-to-guides/how-to-add-oauth',
        component: ComponentCreator('/docs/how-to-guides/how-to-add-oauth', '7aa'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/how-to-guides/how-to-invite-users',
        component: ComponentCreator('/docs/how-to-guides/how-to-invite-users', 'bd8'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/how-to-guides/katanemo-sdk-integration',
        component: ComponentCreator('/docs/how-to-guides/katanemo-sdk-integration', 'b67'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/how-to-guides/oidc-connection',
        component: ComponentCreator('/docs/how-to-guides/oidc-connection', '010'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/how-to-guides/okta-saml-connection',
        component: ComponentCreator('/docs/how-to-guides/okta-saml-connection', 'd9b'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/overview',
        component: ComponentCreator('/docs/overview', 'ae7'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/use-cases/health-records-use-case',
        component: ComponentCreator('/docs/use-cases/health-records-use-case', '7bb'),
        exact: true,
        sidebar: "katanemoSidebar"
      },
      {
        path: '/docs/use-cases/oidc-connection',
        component: ComponentCreator('/docs/use-cases/oidc-connection', '9cc'),
        exact: true,
        sidebar: "katanemoSidebar"
      }
    ]
  },
  {
    path: '/',
    component: ComponentCreator('/', '1dc'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
