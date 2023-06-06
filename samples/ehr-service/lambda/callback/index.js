import AWS from 'aws-sdk';

const apiEndpoint = process.env.API_ENDPOINT
const clientKey = process.env.CLIENT_KEY
const clientSecret = process.env.CLIENT_SECRET

AWS.config.update({ region: process.env.AWS_REGION || 'us-west-1' });

export async function handler(event, context) {
  console.log('Received event:', JSON.stringify(event, null, 2));

  const queryStringParameters = event.queryStringParameters;
  
  let body = 'Invalid request';
  let statusCode = '403';
  const headers = {
    'Content-Type': 'application/json',
  };

  if (!queryStringParameters || !queryStringParameters.code) {
    return {
      statusCode,
      body,
      headers,
    };
  }
    // Access individual query parameters
    const code = queryStringParameters.code;
    let requestBody = {
      "code": code,
      "clientId": clientKey,
      "clientSecret": clientSecret,
    }
    let authUrl = apiEndpoint + "/oauth/token"
    fetch(authUrl, {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody)
    }).then((resp) => {
      if (resp.status == 200) {
        console.log('response from api service: ' + resp)
        
      } else {
        return {
          statusCode,
          body,
          headers,
        };
      }
    }).catch((e) => {
      console.log(e)
      body = 'Call to api service failed'
      return {
        statusCode,
        body,
        headers,
      };
    })

  return {
    statusCode,
    body,
    headers,
  };
};
