.PHONY: lint test

lint:
	python -m flake8 gendiff tests

test:
	python -m pytest -v --cov=gendiff --cov-report=xml

test-coverage:
	python -m pytest --cov=gendiff --cov-report term-missing