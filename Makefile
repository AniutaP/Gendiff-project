install:
	poetry install

gendiff:
	poetry run gendiff

package-install:
	poetry -m pip install --user dist/*.whl

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build:
	poetry build

.PHONY: install test lint selfcheck check build gendiff
