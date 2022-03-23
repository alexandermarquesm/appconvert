from flask import jsonify
from flask_restful import Resource

from appconvert.ext.nomics import valid_get_price


class ConvertCrypt(Resource):
    def get(self, token1: str, token2: str, amount: int):
        price = valid_get_price(token1, token2, amount)
        return jsonify(price=price)
