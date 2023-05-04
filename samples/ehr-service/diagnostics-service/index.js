import AWS from 'aws-sdk';

AWS.config.update({region:'us-west-1'});

const dynamo = new AWS.DynamoDB.DocumentClient()
const tableName = process.env.DIAGNOSTICS_TABLE_NAME || 'diagnostics'

export async function handler(event, context) {
  console.log('Received event:', JSON.stringify(event, null, 2));

  let body;
  let statusCode = '200';
  const headers = {
    'Content-Type': 'application/json',
  };

  try {
    switch (event.httpMethod) {
      case 'DELETE': {
        let patientId = event['pathParameters']['patientId']
        let reportId = event['pathParameters']['reportId']
        body = await dynamo.delete(
          {
            TableName: tableName,
            Key: {
              patientId: patientId,
              reportId: reportId
            }
          }
        ).promise();
        break;
      }
      case 'GET':
        let patientId = event['pathParameters']['patientId']
        let reportId = event['pathParameters']['reportId']
        body = await dynamo.get(
          {
            TableName: tableName,
            Key: {
              patientId: patientId,
              reportId: reportId
            }
          }
        ).promise();
        break;
      case 'POST':
        console.log('adding diagnostics for patient: ' + event.body)
        await dynamo.put(
          {
            TableName: tableName,
            Item: JSON.parse(event.body)
          }
        ).promise();
        break;
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

  const isBase64Encoded = false
  let resp = {
    statusCode,
    body,
    headers,
    isBase64Encoded,
  }

  console.log('sending response back to client: ' + JSON.stringify(resp))

  return {
    statusCode,
    body,
    headers,
  };
};
