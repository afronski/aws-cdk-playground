import cdk = require('@aws-cdk/core');
import s3 = require('@aws-cdk/aws-s3');

export class ExistingBucketViaOverride extends cdk.Stack {
    constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        const bucket = new s3.Bucket(this, "ExistingS3Bucket", {
            versioned: true,
            // removalPolicy: cdk.RemovalPolicy.DESTROY
        });

        // const cfnBucket = bucket.node.defaultChild as s3.CfnBucket;
        // cfnBucket.overrideLogicalId("ExistingS3Bucket");
    }
}
