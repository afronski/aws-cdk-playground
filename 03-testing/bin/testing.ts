#!/usr/bin/env node
import 'source-map-support/register';
import { App, Stack } from '@aws-cdk/core';
import dlq = require('../lib/dead-letter-queue');

const app = new App();
const stack = new Stack(app, 'MyStackWithDLQ');
new dlq.DeadLetterQueue(stack, 'DLQ');
