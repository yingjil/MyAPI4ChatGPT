#!/usr/bin/env python3
import os

import aws_cdk as cdk

from stack.my_stack import MyStack

app = cdk.App()
MyStack(app, "MyStack",
        env=cdk.Environment(account=os.getenv('MY_AWS_ACCOUNT'), region='us-west-2'),
        )

app.synth()
