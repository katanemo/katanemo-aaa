import jwt from 'jsonwebtoken';
import fetch from 'node-fetch';
const url = require('url');

const arcEndpoint = process.env.AUTH_ENDPOINT
const apiEndpoint = process.env.API_ENDPOINT
const clientKey = process.env.CLIENT_KEY
const serviceId = process.env.SERVICE_ID

console.log(apiEndpoint)

function extractTokenFromHeader(e2) {
  console.log(e2);
  if ("Authorization" in e2.headers && e2.headers["Authorization"].split(" ")[0] === "Bearer") {
    return e2.headers["Authorization"].split(" ")[1];
  } else if ("Cookie" in e2.headers) {
    let cookies = e2.headers["Cookie"];
    const stringArray = cookies.split(';');

    for (let i = 0; i < stringArray.length; i++) {
      const currentString = stringArray[i].trim();
      let cookieParts = currentString.split('=');
      let name = cookieParts[0].trim();
      
      if (name !== 'katanemo.accessToken') {
        continue;
      }
      
      console.log('Found access token cookie: ' + currentString);
      let value = cookieParts[1].trim();
      return value;
    }
    return ''
  } else {
    return '';
  }
}

function authorizeRequest(e, userToken, serviceToken, path, method, methodArn, callback) {
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
      if (!userToken) {
        // The path accessed without token found in exclusion list
        // hence ARC returned 200.
        callback(null, generatePolicy("USER", "Allow", methodArn, "", latency));
      } else {
        // A valid access token was found
        let decoded = jwt.decode(userToken)
        callback(null, generatePolicy(decoded.sub, "Allow", methodArn, decoded.accountId, latency));
      }
    } else {
      // No token was found for a path which is not in exclusion list for the service
      // Need to redirect for login
      if(!userToken) {
        let state = "https://" + e.requestContext.domainName + e.requestContext.path
        
        const buffer = Buffer.from(state, "utf8");
        const base64String = buffer.toString("base64");
        const apiAuthPath = apiEndpoint + '/authorize'
        const queryParams = {
          'service': serviceId,
          'clientId': clientKey,
          'state': base64String,
        };
        const constructedUrl = url.format({ pathname: apiAuthPath, query: queryParams });
        console.log('No token found; redirecting for login')
        fetch(constructedUrl, {
          method: 'GET',
          headers: {
            "Content-Type": "application/json",
          },
          
        }).then((resp2) => {
          // Since Lambda Authorizer cannot issue a redirect; pack the requested URL in context
          // and let downstream Lambda to request a redirect.
          const redirectUrl = resp2.url
          callback(null, generateRedirectPolicy("USER", "Allow", methodArn, redirectUrl));

        }).catch((e) => {
          console.log(e)
          callback('Error: call to api service failed')
        })
      } else {
        // A protected path was accessed with an invalid token.
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
  authorizeRequest(event, userToken, serviceToken, path, method, methodArn, callback);
}

// Help function to generate an IAM policy
var generatePolicy = function (principalId, effect, resource, tenantId, latency) {
  var authResponse = prepareAuthResponse(principalId, effect, resource)

  authResponse.context = {
      "tenantId": tenantId,
      "authLatency": latency
  };

  return authResponse;
}

var generateRedirectPolicy = function (principalId, effect, resource, redirect) {
  var authResponse = prepareAuthResponse(principalId, effect, resource)

  authResponse.context = {
      "redirectUrl": redirect
  };
  
  return authResponse;
}

var prepareAuthResponse = function (principalId, effect, resource) {
  var authResponse = {}
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
  return authResponse
}