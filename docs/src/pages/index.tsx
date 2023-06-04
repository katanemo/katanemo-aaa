import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import styles from './index.module.css';
import "../css/custom.css"
import {Redirect} from "@docusaurus/router";

function HomepageHeader() {
  return (
    <header className={clsx('bg-slate-500', styles.heroBanner)}>
      <div className="container">
          <div className={styles.buttons}>
              <Link
                  className="bg-gray-700 button button--secondary button--lg"
                  to="/docs/overview">
                  Go to Katanemo Docs
              </Link>
          </div>
      </div>
    </header>
  );
}

const Homepage = () => {
    const { siteConfig } = useDocusaurusContext();
    return <Redirect to={`${siteConfig.baseUrl}docs/overview`} />;
};
export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Katanemo Documentation`}
      description="Build winning, enterprise-ready services in minutes.">

      <main>
        <Homepage/>
      </main>
    </Layout>
  );
}
