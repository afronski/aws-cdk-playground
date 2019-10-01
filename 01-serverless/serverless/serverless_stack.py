from aws_cdk import (
    core,
    aws_apigateway as apigw,
    aws_lambda as _lambda,
)


class ServerlessStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        lambda_handler = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='hello.handler',
            # dead_letter_queue_enabled = True,
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=lambda_handler,
        )
