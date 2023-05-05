import { handler } from './index.js';

function callback(status, policy) {
  console.log("status: " + status)
  console.log("policy:\n" + JSON.stringify(policy, null, 2))
}

let event = {
  // 'requestContext': {
  //   'authorizer': {
  //     'tenantId': '1234'
  //   }
  // },
  'type': 'TOKEN',
  'methodArn': 'arn:aws:execute-api:us-west-1:264380604816:x9annlzrcd/staging/GET/patient/1',
  'authorizationToken': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImFiYWIwYmEyLWRkNGYtNGVjMy05OTIyLWFhYTc5MGJjNTgxYyIsInR5cCI6IkpXVCJ9.eyJLYXRhbmVtb0RlZmF1bHRTZXJ2aWNlSWQiOiJiYzI3MnB2anAiLCJhY2NvdW50SWQiOiJ4ZnFrM2tyZDQiLCJhdWQiOiJiZWU5bTV6emMiLCJleHAiOjE2ODMxOTM3MjQsImlhdCI6MTY4MzE1MDUyNCwiaXNzIjoiaHR0cHM6Ly9pZHAua2F0YW5lbW8uY29tL3hmcWsza3JkNC8ud2VsbC1rbm93bi9qd2tzLmpzb24iLCJuYmYiOjE2ODMxNTA1MjQsInNjcCI6WyJoemU1NHhuNDciXSwic3ViIjoiYWRpbCsyYTU1MmMzNitldmVyZ3JlZW5hZG1pbkBrYXRhbmVtby5jb20ifQ.Bw7ZdS3vX9RQTNmYLzwhS-Yh8GSKuJ0b68FJzYsGUDPekHZReGCZqBb_YSB2QWvfKUPa_S3ZsFNvAjpXIi48r6iWIVpTJMpsqYMgYPB1dL3qeXuLGYg2v-LcPHQ6usqv6rxYwRzY16yRQg0XI8uC-BqFXSjStZeoHNzBkvUuYc7c2mfek0TXrm6TdQD3P4VpNG_me-702IyiDBdqdFBmAUfh7TNA9p_EqSLD0VsI2IXoPv97bez9ON0nIzxzIwAqSJkLXr5VANTbJBjovn_dlwhEOQlLxe31CPkK32oYAGZCaYyymDyp09cNc9bWmrLafK2qt7SKyZuTJ-vtVZtc4thTVtxk4y_-KNVOEmrGiNg0ln8e9MQCEn1eF46IXmmw1NYQo-mu9gBRcA65NuSR8iuRSCRpNu21c5B2jle7cHbKrhX0r96Y6EexDRYinl8SxqduucdvoOK_nVxpshYAJliFLPFbHT6uNqCYu5aN8HiA3lavRn7lCV8Se0d2cKHEu6WWjN4nhwdmTfKGWt12KmKMF121YpXPstWxxuyYJ1thgO-UAdPOH1cEeaR3hLYOSYkBYqSXInefV7ye3INMasr-Ve-_B4Azr3DcQA6nkQ865QFqxsh92A62F73tgykHVFBAggml74PNPBpZ6Vf9cdzOqXo2PivYSI6bfRc_Wko'
}

console.log( ((event['requestContext'] ?? {})['authorizer'] ?? {})['tenantId'] ?? null)

// console.log(event['requestContext']['authorizer']['tenantId'])

handler(event, null, callback)
