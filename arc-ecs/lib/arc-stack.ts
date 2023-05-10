import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ecs from 'aws-cdk-lib/aws-ecs';
import * as ecsp from 'aws-cdk-lib/aws-ecs-patterns';
import { CfnParameter } from 'aws-cdk-lib';

export class ArcStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const apiEndpoint = new CfnParameter(this, 'apiEndpoint');
    const accountId = new CfnParameter(this, 'accountId');
    const serviceId = new CfnParameter(this, 'serviceId');
    const clientKey = new CfnParameter(this, 'clientKey');
    const clientSecret = new CfnParameter(this, 'clientSecret');

    new ecsp.ApplicationLoadBalancedFargateService(this, 'Katanemo-Arc', {
      taskImageOptions: {
        image: ecs.ContainerImage.fromRegistry('public.ecr.aws/c2g2h4e5/repo/aaa-staging-public:arc_latest'),
        environment: {
          API_ENDPOINT: apiEndpoint.valueAsString,
          ACCOUNT_ID: accountId.valueAsString,
          SERVICE_ID: serviceId.valueAsString,
          CLIENT_KEY: clientKey.valueAsString,
          CLIENT_SECRET: clientSecret.valueAsString,
        },
      },
      publicLoadBalancer: true
    });
  }
}
