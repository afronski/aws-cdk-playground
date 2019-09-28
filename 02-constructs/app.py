#!/usr/bin/env python3

from aws_cdk import core

from workshop.workshop_stack import WorkshopStack


app = core.App()
WorkshopStack(app, "workshop-stack", env={
    'region': 'eu-central-1',
    'participants_count': app.node.try_get_context("participants_count"),
    'password': app.node.try_get_context("password")
})

app.synth()
