import jwt from 'jsonwebtoken';
import fetch from 'node-fetch';

// const authEndpoint = process.env.AUTH_ENDPOINT || 'http://localhost:8081'
const authEndpoint = "https://c7d8-205-175-106-185.ngrok-free.app"

function extractTokenFromHeader(e) {
  if (e.authorizationToken && e.authorizationToken.split(' ')[0] === 'Bearer') {
    return e.authorizationToken.split(' ')[1];
  } else {
    return e.authorizationToken;
  }
}

function authorizeRequest(token, path, method, methodArn, callback) {
  let body = {
    "Token": token,
    "Path": path,
    "HttpMethod": method,
  }
  fetch(authEndpoint + '/authorize', {
    method: 'POST',
    headers: {
      "Authentication": "Bearer " + token,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body)
  }).then((resp) => {
    if (resp.status == 200) {
      let decoded = jwt.decode(token)
      callback(null, generatePolicy(decoded.sub, 'Allow', methodArn, decoded.accountId))
    } else {
      callback('Unauthorized')
    }
  }).catch((e) => {
    console.log(e)
    callback('Error: call to auth service failed')
  })
}

export function handler(event, _context, callback) {
  let token = extractTokenFromHeader(event) || '';
  let methodArn = event.methodArn
  let apiPath = methodArn.split(':')[5]
  let apiPathTokens = apiPath.split('/')
  let method = apiPathTokens[2]
  let path = '/' + apiPathTokens.slice(3).join('/')
  method = apiPathTokens[2]
  authorizeRequest(token, path, method, methodArn, callback);
}

// Help function to generate an IAM policy
var generatePolicy = function (principalId, effect, resource, tenantId) {
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
  };
  return authResponse;
}
