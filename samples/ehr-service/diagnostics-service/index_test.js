import { handler } from './index.js';

handler({ httpMethod: 'GET', pathParameters: {patientId: "1"}}, null).then((res) => {
  console.log(res);
});

// handler({ httpMethod: 'POST', body: '{"patientId": "1"}' }, null).then((res) => {
//   console.log(res);
// });
