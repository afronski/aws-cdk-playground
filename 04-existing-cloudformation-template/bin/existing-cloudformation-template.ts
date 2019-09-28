#!/usr/bin/env node
import 'source-map-support/register';
import { App } from '@aws-cdk/core';
import { ExistingBucketViaOverride } from '../lib/existing-bucket-via-override';
import { ExistingBucketViaTemplateInclude } from '../lib/existing-bucket-via-template-include';

const app = new App();

new ExistingBucketViaOverride(app, 'ExistingBucketViaOverride');
new ExistingBucketViaTemplateInclude(app, 'ExistingBucketViaTemplateInclude');
