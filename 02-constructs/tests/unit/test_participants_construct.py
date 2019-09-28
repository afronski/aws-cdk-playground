import unittest

from aws_cdk import core
from aws_cdk import (aws_iam as iam)

from workshop.participants_construct import ParticipantsConstruct

class TestParticipantConstruct(unittest.TestCase):

    def setUp(self):
        self.app = core.App()
        self.stack = core.Stack(self.app, "MainTestStack")
        self.group = iam.Group(self.stack, 'DummyGroup')
        self.password = 'DUMMY'

    def test_num_buckets(self):
        num = 20
        participants = ParticipantsConstruct(
            self.stack,
            "ParicipantsTest1",
            num,
            password=self.password,
            group=self.group
        )

        assert len(participants.buckets) == num

    def test_num_users(self):
        num = 10
        participants = ParticipantsConstruct(
            self.stack,
            "ParicipantsTest2",
            num,
            password=self.password,
            group=self.group
        )

        assert len(participants.users) == num
