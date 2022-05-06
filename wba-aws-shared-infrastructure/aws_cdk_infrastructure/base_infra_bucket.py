from aws_cdk import App, Stack
from aws_cdk import aws_s3 as s3

# app resources
serverless_main_bucket_name = "wba-serverless-main"


class BaseInfraBucket(Stack):
    def __init__(self, app: App, id: str) -> None:
        super().__init__(app, id)

        serverless_main_bucket = s3.Bucket(
            self,
            serverless_main_bucket_name,
            bucket_name=serverless_main_bucket_name,
            access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )
