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
	poetry run black app.py

run-flake8:
	poetry run flake8 aws_cdk_infrastructure
	poetry run flake8 app.py

run-isort:
	poetry run isort aws_cdk_infrastructure --check
	poetry run isort app.py

run-ci: run-black run-isort run-flake8

run-pytest:
	PYTHONPATH=. poetry run pytest