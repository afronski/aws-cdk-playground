from aws_cdk import (
    aws_iam as iam,
    aws_s3 as s3,
    core
)

from .participants_construct import ParticipantsConstruct


class WorkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        sageMakerPrincipal = iam.ServicePrincipal('sagemaker.amazonaws.com')

        role = iam.Role(
            self, 'WorkshopRole',
            assumed_by = sageMakerPrincipal, role_name = 'amazon-sagemaker-in-practice-workshop-role'
        )

        managed_policy_arn = 'arn:aws:iam::aws:policy/AmazonSageMakerFullAccess'
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name(managed_policy_arn))

        participants_group = iam.Group(self, 'WorkshopParticipantsGroup');
        policy = iam.Policy(self, 'WorkshopParticipantsPolicy');

        permissions = [
          "sagemaker:*",
          "ecr:*",
          "cloudwatch:*",
          "logs:*",

          "s3:GetBucketLocation",
          "s3:ListAllMyBuckets",

          "iam:ListRoles",
          "iam:GetRole"
        ];

        defaultStatement = iam.PolicyStatement(effect=iam.Effect.ALLOW)
        defaultStatement.add_all_resources()
        defaultStatement.add_actions(*permissions)

        value = { 'iam:PassedToService': sageMakerPrincipal.to_string() }

        passRole = iam.PolicyStatement(effect=iam.Effect.ALLOW)
        passRole.add_all_resources()
        passRole.add_actions("iam:PassRole")
        passRole.add_condition("StringEquals", value)

        policy.add_statements(defaultStatement, passRole);

        participants_group.attach_inline_policy(policy);

        existing_bucket_arn = 'arn:aws:s3:::existing-bucket-for-workshop'
        data_source = s3.Bucket.from_bucket_arn(self, 'DataSourceBucket', existing_bucket_arn)

        data_source.grant_read(participants_group)

        amount = kwargs.get("env").get("participants_count")
        password = kwargs.get("env").get("password")

        ParticipantsConstruct(
            self, "WorkshopParticipantsConstruct",
            num=amount, password=password, group=participants_group
        )
