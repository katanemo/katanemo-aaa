import jwt from 'jsonwebtoken';
import fetch from 'node-fetch';
const url = require('url');

const arcEndpoint = process.env.AUTH_ENDPOINT
const apiEndpoint = process.env.API_ENDPOINT
const clientKey = process.env.CLIENT_KEY
const serviceId = process.env.SERVICE_ID
const AUTHORIZATION_HEADER = "Authorization"
const TOKEN_COOKIE_NAME = "katanemo.accessToken"

/**
 * This is the entry point for Lambda Authorizer.
 * It extracts token from the header and prepares other necessary params
 * and then calls the main handler function
 */
export function handler(event, _context, callback) {
  
  let userToken = extractTokenFromHeader(event) || '';
  let serviceToken = userToken
  let methodArn = event.methodArn
  let apiPath = methodArn.split(':')[5]
  let apiPathTokens = apiPath.split('/')
  let method = apiPathTokens[2]
  let path = '/' + apiPathTokens.slice(3).join('/')

  authorizeRequestOrRedirectForLogin(event, userToken, serviceToken, path, method, methodArn, callback);
}

/**
 * This is the core function. It does following:
 * 1. Calls ARC with required params
 * 2. Based on decision (status code) returned by ARC it either:
 *    2.a: Allows the call if the status was 200
 *    2.b: If a protected resource was accessed without a token, setup redirect to login page
 *    2.c: If a protected resource was accessed with an invalid token; Deny
 */
function authorizeRequestOrRedirectForLogin(event, userToken, serviceToken, path, method, methodArn, callback) {
  let body = {
    "Token": userToken,
    "Path": path,
    "HttpMethod": method,
  }
  console.log(JSON.stringify(body))
  var now = new Date().getTime();
  const authUrl = arcEndpoint + '/arc/authorize'
  
  fetch(authUrl, {
    method: 'POST',
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      "Token": userToken,
      "Path": path,
      "HttpMethod": method,
    })
  }).then((resp) => {
    const latency = new Date().getTime() - now
    console.log('auth service response time - auth public endpoint: ' + latency + 'ms')
    let decoded = ''
    
    if (resp.status == 200) {
      let user = "USER"
      let org = ""
      if (userToken) {
        let decoded = jwt.decode(userToken)
        user = decoded.sub
        org = decoded.accountId
      } 
        callback(null, generatePolicy(user, "Allow", methodArn, org, latency));
    } else {
      
      // No token was found for a protected path
      // Need to redirect for login
      if(!userToken) {
        loginRedirectHandler(event, methodArn, callback)
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

/**
 *  This method encapsulates the logic of calling OAuth /authorize and set up context
 *  for downstream lambdas to trigger redirect since Lambda Authorizer cannot redirect by itself
 */
function loginRedirectHandler(event, methodArn, callback) {
  
  let state = "https://" + event.requestContext.domainName + event.requestContext.path
        
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
    
  }).then((resp) => {
    const redirectUrl = resp.url
    callback(null, generateRedirectPolicy("USER", "Allow", methodArn, redirectUrl));

  }).catch((exp) => {
    console.log(exp)
    callback('Error: call to api service failed')
  })
}

/**
 ****************************************
          Helpers
 ****************************************
 */
function extractTokenFromHeader(event) {
  console.log(event);
  let token = ''
  if (AUTHORIZATION_HEADER in event.headers && event.headers[AUTHORIZATION_HEADER].split(" ")[0] === "Bearer") { 
    token = event.headers[AUTHORIZATION_HEADER].split(" ")[1];
  
  } else  {
    token = findTokenInCookies(event)
  } 
  return token;
}

function findTokenInCookies(event) {
  if ( !("Cookie" in event.headers) ) {
    return ''
  }

  let cookies = event.headers["Cookie"];
  const cookiesArray = cookies.split(';');

  for (let i = 0; i < cookiesArray.length; i++) {
    const cookieString = cookiesArray[i].trim();
    let cookieParts = cookieString.split('=');
    let name = cookieParts[0].trim();
    
    if (name !== TOKEN_COOKIE_NAME) {
      continue;
    }
    
    console.log('Found access token cookie: ' + cookieString);
    let value = cookieParts[1].trim();
    return value;
  }
  return ''
}

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
