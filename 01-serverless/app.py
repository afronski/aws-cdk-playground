#!/usr/bin/env python3

from aws_cdk import core

from serverless.serverless_stack import ServerlessStack


app = core.App()
ServerlessStack(app, "serverless-stack", env={'region': 'eu-central-1'})

app.synth()
