import jwt from 'jsonwebtoken';
import fetch from 'node-fetch';

const authEndpoint = process.env.AUTH_ENDPOINT

function extractTokenFromHeader(e) {
  if (e.authorizationToken && e.authorizationToken.split(' ')[0] === 'Bearer') {
    return e.authorizationToken.split(' ')[1];
  } else {
    return e.authorizationToken;
  }
}

function authorizeRequest(userToken, serviceToken, path, method, methodArn, callback) {
  let body = {
    "Token": userToken,
    "Path": path,
    "HttpMethod": method,
  }
  var now = new Date().getTime();
  fetch(authEndpoint + '/authorize', {
    method: 'POST',
    headers: {
      "Authentication": "Bearer " + serviceToken,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body)
  }).then((resp) => {
    const latency = new Date().getTime() - now
    console.log('auth service response time - auth public endpoint: ' + latency + 'ms')
    let decoded = jwt.decode(userToken)
    if (resp.status == 200) {
      callback(null, generatePolicy(decoded.sub, 'Allow', methodArn, decoded.accountId, latency))
    } else {
      callback(null, generatePolicy(decoded.sub, 'Deny', methodArn, decoded.accountId, latency))
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
