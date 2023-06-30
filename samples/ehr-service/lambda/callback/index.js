import AWS from 'aws-sdk';
import fetch from 'node-fetch';

const apiEndpoint = process.env.API_ENDPOINT
const clientKey = process.env.CLIENT_KEY
const clientSecret = process.env.CLIENT_SECRET

AWS.config.update({ region: process.env.AWS_REGION || 'us-west-1' });

export async function handler(event, context) {
  console.log("Received event:", JSON.stringify(event, null, 2));
  const queryStringParameters = event.queryStringParameters;
  let body = "Invalid request";
  let statusCode = "403";
  let headers = {
    "Content-Type": "application/json"
  };
  if (!queryStringParameters || !queryStringParameters.code) {
    return {
      statusCode,
      body,
      headers
    };
  }
  const code = queryStringParameters.code;
  let requestBody = {
    "code": code,
    "clientId": clientKey,
    "clientSecret": clientSecret
  };
  let authUrl = apiEndpoint + "/oauth/token";
  try {
    const response = await fetch(authUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(requestBody)
    });
    const resp = await response.json();
    
    if (response.status == 200) {
      return redirectToState(queryStringParameters.state, resp["accessToken"])
    } else {
      console.log("Unexpected status returned by authorize: " + resp.status);
      return {
        statusCode,
        body,
        headers
      };
    }
  } catch (error) {
    console.log(error);
    body = "Call to API service failed";
    return {
      statusCode,
      body,
      headers
    };
  }
};

function redirectToState(state, token) {
  
  const buffer = Buffer.from(state, "base64");
  const url = buffer.toString("utf8");
  console.log("redirect url: " + url);
  let headers = {
    "Content-Type": "application/json",
    "Location": url,
    "Set-Cookie": `katanemo.accessToken=${token}; Secure; HttpOnly; SameSite=Lax; Max-Age=10;`
  };
  
  console.log(headers)
  return {
    "statusCode": 302,
    "body": "",
    "headers": headers,
  };
}