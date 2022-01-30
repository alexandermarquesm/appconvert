from flask import Flask


def create_app():
    app = Flask(__name__, static_folder="blueprints/webui/static")
    return app
