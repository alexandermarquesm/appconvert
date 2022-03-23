from flask import Flask

from appconvert.ext import configuration


def minimal_app(**config):
    app = Flask(__name__, static_folder="blueprints/webui/static")
    configuration.init_app(app, **config)
    return app


def create_app(**config):
    app = minimal_app(**config)
    app.config.load_extensions()
    return app
