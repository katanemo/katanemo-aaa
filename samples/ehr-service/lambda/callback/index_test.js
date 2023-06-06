import { handler } from './index.js';

// handler({ httpMethod: 'GET', pathParameters: {patientId: "1"}}, null).then((res) => {
//   console.log(res);
// });

// handler({ httpMethod: 'POST', pathParameters: {name: "test name 1"}}, null).then((res) => {
//   console.log(res);
// });


handler({ httpMethod: 'POST', body: '{"name": "john walpole"}' }, null).then((res) => {
  console.log(res);
});
