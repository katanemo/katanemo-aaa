import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ecs from 'aws-cdk-lib/aws-ecs';
import * as ecsp from 'aws-cdk-lib/aws-ecs-patterns';
import { CfnParameter } from 'aws-cdk-lib';
import { ApplicationProtocol } from 'aws-cdk-lib/aws-elasticloadbalancingv2';

export class ArcStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const apiEndpoint = new CfnParameter(this, 'apiEndpoint');
    const arcosEndpoint = new CfnParameter(this, 'arcosEndpoint');
    const serviceId = new CfnParameter(this, 'serviceId');
    const clientKey = new CfnParameter(this, 'clientKey');
    const clientSecret = new CfnParameter(this, 'clientSecret');
    const arcSha = new CfnParameter(this, 'arcSha');

    const service = new ecsp.ApplicationLoadBalancedFargateService(this, 'Katanemo-Arc', {
      taskImageOptions: {
        image: ecs.ContainerImage.fromRegistry('public.ecr.aws/c2g2h4e5/repo/aaa-public:arc_' + arcSha.valueAsString),
        environment: {
          API_ENDPOINT: apiEndpoint.valueAsString,
          ARCOS_ENDPOINT: arcosEndpoint.valueAsString,
          SERVICE_ID: serviceId.valueAsString,
          CLIENT_KEY: clientKey.valueAsString,
          CLIENT_SECRET: clientSecret.valueAsString,
        },
        containerPort: 8083,
      },
      publicLoadBalancer: true,
      //TODO: enable HTTPS (protocol: ApplicationProtocol.HTTPS,)
    });
    service.targetGroup.configureHealthCheck({
      path: '/healthz',
      port: '8083',
    });
  }
}
