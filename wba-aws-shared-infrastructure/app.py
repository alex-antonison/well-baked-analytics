import aws_cdk as cdk

from aws_cdk_infrastructure.gbbo_s3_bucket import GbboBucket
from aws_cdk_infrastructure.base_infra_bucket import BaseInfraBucket

app = cdk.App()
BaseInfraBucket(app, "base-infra-bucket")
GbboBucket(app, "dev-wba-bucket", "dev")
GbboBucket(app, "prod-wba-bucket", "prod")

app.synth()
