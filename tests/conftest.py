import pytest

from appconvert.app import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app()
    yield app
