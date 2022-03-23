.PHONY: install format lint test sec

install:
	@poetry install

format:
	@blue .
	@black .

lint:
	@blue --check .
	@isort --check .
	@prospector

sec:
	@pip-audit

test:
	@pytest tests/ -v --disable-pytest-warnings

test-funcional:
	@pytest tests/funcional -v --disable-pytest-warnings

test-unit:
	@pytest tests/unit -v --disable-pytest-warnings

ps:
	@poetry shell