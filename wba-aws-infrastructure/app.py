#!/usr/bin/env python3

import aws_cdk as cdk

from aws_infrastructure.aws_infrastructure_stack import AwsInfrastructureStack


app = cdk.App()
AwsInfrastructureStack(app, "aws-infrastructure")

app.synth()
