import AWS from 'aws-sdk';

AWS.config.update({ region: 'us-west-1' });

const dynamo = new AWS.DynamoDB.DocumentClient()
const tableName = process.env.DIAGNOSTIC_TABLE_NAME || 'diagnostic'

export async function handler(event, context) {
  console.log('Received event:', JSON.stringify(event, null, 2));

  let body;
  let statusCode = '200';
  const headers = {
    'Content-Type': 'application/json',
  };

  try {
    let tenantId = getTenantId(event)
    switch (event.httpMethod) {
      case 'DELETE': {
        await deleteDiagnostic(event['pathParameters']['diagnosticId']);
        break;
      }
      case 'GET':
        body = await getDiagnostic(event['pathParameters']['diagnosticId']);
        if (body.Item == null) {
          statusCode = '404'
          body = 'diagnostic not found'
        }
        break;
      case 'POST': {
        let parsedBody = JSON.parse(event.body)
        body = await createDiagnostic(tenantId, parsedBody)
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

async function createDiagnostic(tenantId, diagnostic) {
  if (diagnostic.diagnosticId != null) {
    throw new Error('diagnosticId must be nil when creating a new diagnostic')
  }
  let diagnosticId = [tenantId, randomString(6)].join('_')
  diagnostic['diagnosticId'] = diagnosticId

  return new Promise(function (resolve, reject) {
    dynamo.put(
      {
        TableName: tableName,
        Item: diagnostic
      }
    ).promise().then((_res) => {
      dynamo.get(
        {
          TableName: tableName,
          Key: {
            diagnosticId: diagnosticId
          }
        }
      ).promise().then((res) => resolve(res))
    }).catch((err) => reject(err))
  }).catch((err) => reject(err))
}

async function deleteDiagnostic(diagnosticId) {
  return dynamo.delete(
    {
      TableName: tableName,
      Key: {
        diagnosticId: diagnosticId
      }
    }
  ).promise()
}

async function getDiagnostic(diagnosticId) {
  return dynamo.get(
    {
      TableName: tableName,
      Key: {
        diagnosticId: diagnosticId
      }
    }
  ).promise();
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
