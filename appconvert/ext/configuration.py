from dynaconf import FlaskDynaconf

flask_dynaconf = FlaskDynaconf(
    settings_files=["settings.toml"],
    ENV_FOR_DYNACONF="production",
)


def init_app(app):
    flask_dynaconf.init_app(app)
