import pytest


@pytest.mark.config
def test_if_env_is_production(config):
    assert config["ENV"] == "production"


@pytest.mark.config
def test_if_debug_is_false(config):
    assert config["DEBUG"] == False


@pytest.mark.config
def test_if_have_app(config):
    assert config["app"] == "appconvert/app.py"


@pytest.mark.config
def test_if_title_of_project_is_configconvert(config):
    assert config["TITLE"] == "appconvert"


@pytest.mark.config
def test_if_have_database(config):
    assert config["SQLALCHEMY_DATABASE_URI"] is not None
