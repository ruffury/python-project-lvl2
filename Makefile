install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test test-coverage lint

build:
	poetry build

gendiff:
	poetry run gendiff

.PHONY: install test test-coverage lint selfcheck check build