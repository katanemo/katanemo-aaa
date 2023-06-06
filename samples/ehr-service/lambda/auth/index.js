import jwt from 'jsonwebtoken';
import fetch from 'node-fetch';
const url = require('url');

const arcEndpoint = process.env.AUTH_ENDPOINT
const apiEndpoint = process.env.API_ENDPOINT
const clientKey = process.env.CLIENT_KEY
const serviceId = process.env.SERVICE_ID

console.log(apiEndpoint)

function extractTokenFromHeader(e) {
  
  console.log(e)
  if ('Authorization' in e.headers && e.headers['Authorization'].split(' ')[0] === 'Bearer') {
    return e.headers['Authorization'].split(' ')[1]
  } else {
    return '';
  }
}

function authorizeRequest(userToken, serviceToken, path, method, methodArn, callback) {
  let body = {
    "Token": userToken,
    "Path": path,
    "HttpMethod": method,
  }
  console.log(JSON.stringify(body))
  var now = new Date().getTime();
  const authUrl = arcEndpoint + '/arc/authorize'
  console.log("authUrl: " + authUrl)
  fetch(authUrl, {
    method: 'POST',
    headers: {
      "Authentication": "Bearer " + serviceToken,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body)
  }).then((resp) => {
    const latency = new Date().getTime() - now
    console.log('auth service response time - auth public endpoint: ' + latency + 'ms')
    let decoded = ''
    if (resp.status == 200) {
      decoded = jwt.decode(userToken)
      callback(null, generatePolicy(decoded.sub, 'Allow', methodArn, decoded.accountId, latency))
    } else {
      if(!userToken) {
        const apiAuthPath = apiEndpoint + '/authorize'
        const queryParams = {
          'serviceId': serviceId,
          'clientId': clientKey,
          'state': 'value2',
        };
        const constructedUrl = url.format({ pathname: apiAuthPath, query: queryParams });
        console.log('Redirecting for login: ' + constructedUrl)
        fetch(constructedUrl, {
          method: 'GET',
          headers: {
            "Content-Type": "application/json",
          },
          
        }).then((resp2) => {
          const redirectUrl = resp2.url
          callback(null, generateRedirectPolicy("USER", "Allow", methodArn, redirectUrl));

        }).catch((e) => {
          console.log(e)
          callback('Error: call to api service failed')
        })
      } else {
        callback(null, generatePolicy(decoded.sub, 'Deny', methodArn, decoded.accountId, latency))
      }
      
    }
  }).catch((e) => {
    console.log(e)
    callback('Error: call to auth service failed')
  })
}

export function handler(event, _context, callback) {
  
  let userToken = extractTokenFromHeader(event) || '';
  let serviceToken = userToken
  let methodArn = event.methodArn
  let apiPath = methodArn.split(':')[5]
  let apiPathTokens = apiPath.split('/')
  let method = apiPathTokens[2]
  let path = '/' + apiPathTokens.slice(3).join('/')
  method = apiPathTokens[2]
  authorizeRequest(userToken, serviceToken, path, method, methodArn, callback);
}

// Help function to generate an IAM policy
var generatePolicy = function (principalId, effect, resource, tenantId, latency) {
  var authResponse = {};

  authResponse.principalId = principalId;
  if (effect && resource) {
    var policyDocument = {};
    policyDocument.Version = '2012-10-17';
    policyDocument.Statement = [];
    var statementOne = {};
    statementOne.Action = 'execute-api:Invoke';
    statementOne.Effect = effect;
    statementOne.Resource = resource;
    policyDocument.Statement[0] = statementOne;
    authResponse.policyDocument = policyDocument;
  }

  authResponse.context = {
      "tenantId": tenantId,
      "authLatency": latency
  };
  return authResponse;
}

var generateRedirectPolicy = function (principalId, effect, resource, redirect) {
  var authResponse = {};

  authResponse.principalId = principalId;
  if (effect && resource) {
    var policyDocument = {};
    policyDocument.Version = '2012-10-17';
    policyDocument.Statement = [];
    var statementOne = {};
    statementOne.Action = 'execute-api:Invoke';
    statementOne.Effect = effect;
    statementOne.Resource = resource;
    policyDocument.Statement[0] = statementOne;
    authResponse.policyDocument = policyDocument;
  }

  authResponse.context = {
      "redirectUrl": redirect
  };
  return authResponse;
}
