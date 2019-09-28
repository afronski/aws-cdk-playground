from aws_cdk import (
    aws_iam as iam,
    aws_s3 as s3,
    core as core
)


class ParticipantsConstruct(core.Construct):

    @property
    def buckets(self):
        return tuple(self._buckets)

    @property
    def users(self):
        return tuple(self._users)

    def __init__(self, scope: core.Construct, id: str, num: int, password: str, group: iam.Group) -> None:
        super().__init__(scope, id)

        self._buckets = []
        self._users = []

        for i in range(1, num + 1):
            user = iam.User(
                self, f"workshop-user-{i}",
                password = core.SecretValue.plain_text(password), groups = [group]
            )

            self._users.append(user)

            bucket = s3.Bucket(self, f"bucket-for-user-{i}")

            self._buckets.append(bucket)

            bucket.grant_read_write(user)
