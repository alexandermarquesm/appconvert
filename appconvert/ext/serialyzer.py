from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields
from appconvert.models import Category

ma = Marshmallow()


class TokenSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("currency", "symbol", "name", "logo_url","marketcap", "price", "blockchain")


token_schema = TokenSchema()
tokens_schema = TokenSchema(many=True)


def init_app(app):
    ma.init_app(app)
