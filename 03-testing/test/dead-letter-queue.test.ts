import { SynthUtils } from '@aws-cdk/assert';
import { Stack } from '@aws-cdk/core';
import '@aws-cdk/assert/jest';
import dlq = require('../lib/dead-letter-queue');

test('each DLQ has an associated CloudWatch alarm', () => {
  const stack = new Stack();
  new dlq.DeadLetterQueue(stack, 'DLQ');

  expect(SynthUtils.toCloudFormation(stack)).toMatchSnapshot();
});

// test('each DLQ has maximum retention period', () => {
//   const stack = new Stack();

//   new dlq.DeadLetterQueue(stack, 'DLQ');

//   expect(stack).toHaveResource('AWS::SQS::Queue', {
//     MessageRetentionPeriod: 1209600
//   });
// });

// test('retention period for DLQ can be configured', () => {
//   const stack = new Stack();

//   new dlq.DeadLetterQueue(stack, 'DLQ', {
//     retentionDays: 7
//   });

//   expect(stack).toHaveResource('AWS::SQS::Queue', {
//     MessageRetentionPeriod: 604800
//   });
// });

// test('configurable retention period for DLQ cannot exceed 14 days', () => {
//   const stack = new Stack();

//   expect(() => {
//     new dlq.DeadLetterQueue(stack, 'DLQ', {
//       retentionDays: 15
//     });
//   }).toThrowError(/retentionDays may not exceed 14 days/);
// });
