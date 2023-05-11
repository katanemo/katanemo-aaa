#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { ArcStack } from './lib/arc-stack';

const app = new cdk.App();
new ArcStack(app, 'ArcStack', {});
