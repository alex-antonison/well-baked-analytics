cleanup:
	poetry run black aws_cdk_infrastructure/
	poetry run black app.py
	poetry run black tests/

deploy:
	cdk deploy

diff:
	cdk diff

run-black:
	poetry run black aws_cdk_infrastructure --check


run-flake8:
	poetry run flake8 aws_cdk_infrastructure

run-isort:
	poetry run isort aws_cdk_infrastructure --check

run-ci: run-black run-isort run-flake8

run-pytest:
	PYTHONPATH=. poetry run pytest