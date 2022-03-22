from dynaconf import FlaskDynaconf

def init_app(app, **config):
    FlaskDynaconf(
        app,
        settings_files=['settings.toml'],
        ENV_FOR_DYNACONF="production",
    )
