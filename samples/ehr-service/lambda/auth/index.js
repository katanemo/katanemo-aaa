import jwt from 'jsonwebtoken';
import fetch from 'node-fetch';
const url = require('url');

const arcEndpoint = process.env.AUTH_ENDPOINT
const apiEndpoint = process.env.API_ENDPOINT
const clientKey = process.env.CLIENT_KEY
const serviceId = process.env.SERVICE_ID
const AUTHORIZATION_HEADER = "Authorization"

/**
 * This is the entry point for the Lambda authorizer. It does three things
 * 
 * 1. 
 * 2. 
 * 3. 
 * 
 * @param {*} event 
 * @param {*} _context 
 * @param {*} callback 
 */
export function handler(event, _context, callback) {
  
  let userToken = extractTokenFromHeader(event) || '';
  let serviceToken = userToken
  let methodArn = event.methodArn
  let apiPath = methodArn.split(':')[5]
  let apiPathTokens = apiPath.split('/')
  let method = apiPathTokens[2]
  let path = '/' + apiPathTokens.slice(3).join('/')
  method = apiPathTokens[2]
  let policy = authorieRequestOrSetRedirectContextForUserViaPolicy(event, userToken, serviceToken, path, method, methodArn);
  callback()
}

/**
 * 
 * @param {*} event 
 * @param {*} userToken 
 * @param {*} serviceToken 
 * @param {*} path 
 * @param {*} method 
 */
function authorieRequestOrSetRedirectContextForUser(event, userToken, serviceToken, path, method){
  //authorizeRequest
}

/**
 * 
 * @param {*} e 
 * @param {*} userToken 
 * @param {*} serviceToken 
 * @param {*} path 
 * @param {*} method 
 * @param {*} methodArn 
 * @param {*} callback 
 */
function authorizeRequest(e, userToken, serviceToken, path, method, methodArn) {
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
      "Authentication": "Bearer " + serviceToken,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body)
  }).then((resp) => {
    const latency = new Date().getTime() - now
    console.log('auth service response time - auth public endpoint: ' + latency + 'ms')
    
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
        loginRedirectHandler(e, methodArn, callback)
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
 * 
 * @param {*} event 
 * @returns 
 */
function extractTokenFromHeader(event) {
  console.log(event);
  let token = ''
  if (AUTHORIZATION_HEADER in e2.headers && e2.headers[AUTHORIZATION_HEADER].split(" ")[0] === "Bearer") { 
    token = e2.headers[AUTHORIZATION_HEADER].split(" ")[1];
  
  } else  {
    token = findTokenInCookies(e2)
  } 
  return token;
}

/**
 * 
 * @param {*} event
 * @returns 
 */
function findTokenInCookies(event) {
  if ( !("Cookie" in event.headers) ) {
    return ''
  }

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
}


function loginRedirectHandler(e, methodArn, callback) {
  
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
    
  }).then((resp) => {
    const redirectUrl = resp.url
    callback(null, generateRedirectPolicy("USER", "Allow", methodArn, redirectUrl));

  }).catch((exp) => {
    console.log(exp)
    callback('Error: call to api service failed')
  })
}


// Help function to generate an IAM policy
var generatePolicy = function (principalId, effect, resource, tenantId, latency) {
  var authResponse = prepareAuthResponse(principalId, effect, resource)=
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