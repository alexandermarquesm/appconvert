import pytest
from appconvert.app import minimal_app, create_app

@pytest.fixture(scope="module")
def app():
    app = create_app()
    return app
