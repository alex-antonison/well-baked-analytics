from aws_cdk import App, Stack
from aws_cdk import aws_s3 as s3


class GbboBucket(Stack):
    def __init__(self, app: App, id: str, env: str) -> None:
        super().__init__(app, id)

        # data buckets
        source_bucket_name = f"{env}-wba-gbbo-data-lake-source"
        preprocess_bucket_name = f"{env}-wba-gbbo-data-lake-preprocess"
        staged_bucket_name = f"{env}-wba-gbbo-data-lake-staged"
        athena_query_bucket_name = f"{env}-wba-athena-query-result"

        source_bucket = s3.Bucket(
            self,
            source_bucket_name,
            bucket_name=source_bucket_name,
            access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )

        preprocess_bucket = s3.Bucket(
            self,
            preprocess_bucket_name,
            bucket_name=preprocess_bucket_name,
            access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )

        staged_bucket = s3.Bucket(
            self,
            staged_bucket_name,
            bucket_name=staged_bucket_name,
            access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )

        athena_query_bucket = s3.Bucket(
            self,
            athena_query_bucket_name,
            bucket_name=athena_query_bucket_name,
            access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )
