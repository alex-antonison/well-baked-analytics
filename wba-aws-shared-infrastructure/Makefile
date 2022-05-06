cleanup:
	poetry run black aws_cdk_infrastructure/
	poetry run black app.py
	poetry run black tests/

deploy:
	cdk deploy

diff:
	cdk diff