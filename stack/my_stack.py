import os
import subprocess

from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    CfnOutput, Duration, aws_apigateway, Aws,
)
from constructs import Construct


class MyStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        entrypoint_name = "my_lambda"
        my_lambda = _lambda.Function(
            self,
            "MyLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset(f'{entrypoint_name}'),
            handler='lambda_handler.handler',
            timeout=Duration.seconds(120),
            layers=[
                self.create_dependencies_layer(self.stack_name, entrypoint_name)
            ],
            environment={  # ADD THIS, FILL IT FOR ACTUAL VALUE
                "OPENAI_API_KEY": os.environ['OPENAI_API_KEY'],
                "DOUYIN_SECRET_ttbaedcc5025d2e24701": os.environ['DOUYIN_SECRET_ttbaedcc5025d2e24701'],
            },

        )

        my_api = aws_apigateway.RestApi(self, "my_api",
                                        rest_api_name="my_api",
                                        )

        lambda_integration = aws_apigateway.LambdaIntegration(my_lambda,
                                                              request_templates={
                                                                  "application/json": '{ "statusCode": "200" }'})

        my_api.root.add_method("POST", lambda_integration)

        CfnOutput(self, "ApiHostUrl",
                  value=f"{my_api.rest_api_id}.execute-api.{Aws.REGION}.amazonaws.com",
                  description="API Host URL"
                  )

    def create_dependencies_layer(self, project_name, function_name: str) -> _lambda.LayerVersion:
        requirements_file = f'{function_name}/requirements.txt'
        output_dir = f'.build/{function_name}'

        if not os.environ.get('SKIP_PIP'):
            subprocess.check_call(
                f'pip install -r {requirements_file} -t {output_dir}/python'.split()
            )

        layer_id = f'{project_name}-{function_name}-dependencies'
        layer_code = _lambda.Code.from_asset(output_dir)

        return _lambda.LayerVersion(self, layer_id, code=layer_code)
