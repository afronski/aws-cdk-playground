import cdk = require('@aws-cdk/core');
import fs = require('fs');
import path = require('path');
import yaml = require('js-yaml');

export class ExistingBucketViaTemplateInclude extends cdk.Stack {
    constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        const templateFilePath = "./infrastructure/existing-bucket-via-cloudformation-template.yaml";
        const blob = fs.readFileSync(path.resolve(templateFilePath));

        const include = new cdk.CfnInclude(this, "ExistingInfrastructure", {
            template: yaml.safeLoad(blob.toString())
        });
    }
}
