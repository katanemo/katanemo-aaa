import { ApiKeySourceType, LambdaIntegration, RestApi, RequestAuthorizer } from 'aws-cdk-lib/aws-apigateway';
import { AttributeType, Table } from 'aws-cdk-lib/aws-dynamodb';
import { Runtime } from 'aws-cdk-lib/aws-lambda';
import { App, Stack, RemovalPolicy, CfnParameter, Duration } from 'aws-cdk-lib';
import { NodejsFunction, NodejsFunctionProps } from 'aws-cdk-lib/aws-lambda-nodejs';
import { join } from 'path'


export class ApiLambdaEhrServiceStack extends Stack {
  constructor(app: App, id: string) {
    super(app, id);

    const clientKey = new CfnParameter(this, 'clientKey');
    const clientSecret = new CfnParameter(this, 'clientSecret');
    const serviceId = new CfnParameter(this, 'serviceId');
    const apiEndpoint = new CfnParameter(this, 'apiEndpoint');
    const authEndpoint = new CfnParameter(this, 'authEndpoint');

    const patientRecordsTable = new Table(this, 'patient-records', {
      partitionKey: {
        name: 'patientId',
        type: AttributeType.STRING
      },
      tableName: 'patient-records',

      removalPolicy: RemovalPolicy.DESTROY, // NOT recommended for production code
    });

    const diagnosticTable = new Table(this, 'diagnostic-records', {
      partitionKey: {
        name: 'diagnosticId',
        type: AttributeType.STRING
      },
      tableName: 'diagnostic-records',

      removalPolicy: RemovalPolicy.DESTROY, // NOT recommended for production code
    });

    const katanemoAuthLambda = new NodejsFunction(this, 'KatanemoAuthFunction', {
      entry: join(__dirname, 'lambda/auth', 'index.js'),
      depsLockFilePath: join(__dirname, 'lambda/auth', 'package-lock.json'),
      bundling: {
        externalModules: [
          'aws-sdk',
        ],
      },
      runtime: Runtime.NODEJS_18_X,
      environment: {
        AUTH_ENDPOINT: authEndpoint.valueAsString,
        API_ENDPOINT: apiEndpoint.valueAsString,
        CLIENT_KEY: clientKey.valueAsString,
        CLIENT_SECRET: clientSecret.valueAsString,
        SERVICE_ID: serviceId.valueAsString,
      },
    });

    const katanemoTokenAuthorizer = new RequestAuthorizer(this, 'KatanemoTokenAutorizer', {
      identitySources: [],
      handler: katanemoAuthLambda,
      resultsCacheTtl: Duration.seconds(0),
    })

    const nodeJsFunctionProps: NodejsFunctionProps = {
      bundling: {
        externalModules: [
          'aws-sdk',
        ],
      },
      runtime: Runtime.NODEJS_14_X,
      environment: {
        API_ENDPOINT: apiEndpoint.valueAsString,
        CLIENT_KEY: clientKey.valueAsString,
        CLIENT_SECRET: clientSecret.valueAsString,
      }
    }

    // oauth 2.0 callback lambda
    const callbackLambda = new NodejsFunction(this, 'CallbackFunction', {
      entry: join(__dirname, 'lambda/callback', 'index.js'),
      depsLockFilePath: join(__dirname, 'lambda/callback', 'package-lock.json'),
      ...nodeJsFunctionProps,
    });

    const callbackIntegration = new LambdaIntegration(callbackLambda);

    // patient record lambda methods
    const getPatientRecordLambda = new NodejsFunction(this, 'getPatientRecord', {
      entry: join(__dirname, 'lambda/patients', 'index.js'),
      depsLockFilePath: join(__dirname, 'lambda/patients', 'package-lock.json'),
      ...nodeJsFunctionProps,
    });
    patientRecordsTable.grantReadData(getPatientRecordLambda);
    const getPatientRecordIntegration = new LambdaIntegration(getPatientRecordLambda);

    const createPatientRecordLambda = new NodejsFunction(this, 'createPatientRecord', {
      entry: join(__dirname, 'lambda/patients', 'index.js'),
      depsLockFilePath: join(__dirname, 'lambda/patients', 'package-lock.json'),
      environment: {
        CLIENT_KEY: clientKey.valueAsString,
        CLIENT_SECRET: clientSecret.valueAsString,
      },
      ...nodeJsFunctionProps,
    });
    patientRecordsTable.grantReadWriteData(createPatientRecordLambda);
    const createPatientRecordIntegration = new LambdaIntegration(createPatientRecordLambda);

    // patient diagnostic lambda methods
    const getDiagnosticLambda = new NodejsFunction(this, 'getDiagnosticRecord', {
      entry: join(__dirname, 'lambda/diagnostic', 'index.js'),
      depsLockFilePath: join(__dirname, 'lambda/diagnostic', 'package-lock.json'),
      ...nodeJsFunctionProps,
    });
    diagnosticTable.grantReadData(getDiagnosticLambda);
    const getDiagnosticIntegration = new LambdaIntegration(getDiagnosticLambda);

    const createDiagnosticRecordLambda = new NodejsFunction(this, 'createDiagnosticRecord', {
      entry: join(__dirname, 'lambda/diagnostic', 'index.js'),
      depsLockFilePath: join(__dirname, 'lambda/diagnostic', 'package-lock.json'),
      environment: {
        CLIENT_KEY: clientKey.valueAsString,
        CLIENT_SECRET: clientSecret.valueAsString,
      },
      ...nodeJsFunctionProps,
    });
    diagnosticTable.grantReadWriteData(createDiagnosticRecordLambda);
    const createDiagnosticRecordIntegration = new LambdaIntegration(createDiagnosticRecordLambda);

    // Create an API Gateway resource for patient and diagnostic records
    const ehrServiceApiGateway = new RestApi(this, 'patientRecordService', {
      restApiName: 'Patient Record Service',
      apiKeySourceType: ApiKeySourceType.AUTHORIZER,
    });

    // callback route
    const callbackHook = ehrServiceApiGateway.root.addResource('callback');
    callbackHook.addMethod('GET', callbackIntegration, { authorizer: katanemoTokenAuthorizer });
    
    // entry points for patient records
    const createPatientRecord = ehrServiceApiGateway.root.addResource('patient');
    createPatientRecord.addMethod('POST', createPatientRecordIntegration, { authorizer: katanemoTokenAuthorizer });
    const getPatientRecord = createPatientRecord.addResource('{patientId}');
    getPatientRecord.addMethod('GET', getPatientRecordIntegration, { authorizer: katanemoTokenAuthorizer });

    // entry points for diagnostic records
    const createDiagnosticReport = ehrServiceApiGateway.root.addResource('diagnostic');
    createDiagnosticReport.addMethod('POST', createDiagnosticRecordIntegration, { authorizer: katanemoTokenAuthorizer });
    const getDiagnosticReport = createDiagnosticReport.addResource('{diagnosticId}');
    getDiagnosticReport.addMethod('GET', getDiagnosticIntegration, { authorizer: katanemoTokenAuthorizer });
  }
}


const app = new App();
new ApiLambdaEhrServiceStack(app, 'ApiLambdaEhrService');
app.synth();
