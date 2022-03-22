ps:
	poetry shell

test:
	pytest tests/ -v --disable-pytest-warnings

test-funcional:
	pytest tests/funcional -v --disable-pytest-warnings

test-unit:
	pytest tests/unit -v --disable-pytest-warnings