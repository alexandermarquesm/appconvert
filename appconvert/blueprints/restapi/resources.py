from typing import Dict
from flask import Response, jsonify
from flask_restful import Resource
from appconvert.ext.nomics import valid_get_price, token_is_valid


class ConvertCrypt(Resource):
    def get(self, token1: str, token2: str, amount: int) -> Response:
        price = valid_get_price(token1, token2, amount)
        return jsonify(price)


class ValidToken(Resource):
    def get(self, token: str) -> Response:
        token_list = token_is_valid(token)
        return jsonify(token_list)
