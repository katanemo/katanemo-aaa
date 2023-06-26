import AWS from 'aws-sdk';

AWS.config.update({ region: process.env.AWS_REGION || 'us-west-1' });

const dynamo = new AWS.DynamoDB.DocumentClient()
const tableName = process.env.PATIENTS_TABLE_NAME || 'patient-records'

export async function handler(event, context) {
  console.log('Received event:', JSON.stringify(event, null, 2));
  let redirectUrl = getRedirect(event)
  if(redirectUrl) {
        return {
        'statusCode': 302,
        'headers': {
           'Location': redirectUrl
       }
    }
  }
  let body;
  let statusCode = '200';
  const headers = {
    'Content-Type': 'application/json',
  };

  try {
    let tenantId = getTenantId(event)
    let latency = getLatency(event)
    switch (event.httpMethod) {
      case 'DELETE': {
        await deletePatient(event['pathParameters']['patientId']);
        break;
      }
      case 'GET':
        body = await getPatient(event['pathParameters']['patientId']);
        body['latency'] = latency
        if (body.Item == null) {
          statusCode = '404'
          body = 'patient not found'
        }
        break;
      case 'POST': {
        let parsedBody = JSON.parse(event.body)
        body = await createPatient(tenantId, parsedBody)
        break;
      }
      default:
        throw new Error(`Unsupported method "${event.httpMethod}"`);
    }
  } catch (err) {
    console.log('error caught while executing lambda function' + err)
    statusCode = '400';
    body = err.message;
  } finally {
    body = JSON.stringify(body);
  }

  return {
    statusCode,
    body,
    headers,
  };
};

async function createPatient(tenantId, patient) {
  if (patient.patientId != null) {
    throw new Error('patientId must be nil when creating a new patient')
  }
  let patientId = [tenantId, randomString(6)].join('_')
  patient['patientId'] = patientId

  return new Promise(function (resolve, reject) {
    dynamo.put(
      {
        TableName: tableName,
        Item: patient
      }
    ).promise().then((_res) => {
      dynamo.get(
        {
          TableName: tableName,
          Key: {
            patientId: patientId
          }
        }
      ).promise().then((res) => resolve(res))
    }).catch((err) => reject(err))
  }).catch((err) => reject(err))
}

async function deletePatient(patientId) {
  return dynamo.delete(
    {
      TableName: tableName,
      Key: {
        patientId: patientId
      }
    }
  ).promise()
}

async function getPatient(patientId) {
  return dynamo.get(
    {
      TableName: tableName,
      Key: {
        patientId: patientId
      }
    }
  ).promise();
}

function getLatency(event) {
  return ((event['requestContext'] ?? {})['authorizer'] ?? {})['authLatency'] ?? null
}

function getTenantId(event) {
  return ((event['requestContext'] ?? {})['authorizer'] ?? {})['tenantId'] ?? null
}

function randomString(length) {
  let result = '';
  const characters = 'abcdefghijklmnopqrstuvwxyz0123456789';
  const charactersLength = characters.length;
  let counter = 0;
  while (counter < length) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
    counter += 1;
  }
  return result;
}
