from flask import Blueprint
from flask_restful import Api

from .resources.convertcrypt import ConvertCrypt
from .resources.gettokensbycategory import GetTokensByCategory
from .resources.validtoken import ValidToken


bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(
        ConvertCrypt, "/ConvertCrypt" ,"/convert/<string:token1>&<string:token2>&<int:amount>"
    )
    api.add_resource(ValidToken, "/ValidToken", "/isvalid/<string:token>")
    api.add_resource(GetTokensByCategory, "/GetTokensByCategory", "/category/<string:category>")
    app.register_blueprint(bp)
