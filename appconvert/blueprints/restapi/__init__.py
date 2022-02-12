from flask import Blueprint
from flask_restful import Api

from .resources import ConvertCrypt


bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(
        ConvertCrypt, "/convert/<string:token1>&<string:token2>&<int:amount>"
    )

    app.register_blueprint(bp)
