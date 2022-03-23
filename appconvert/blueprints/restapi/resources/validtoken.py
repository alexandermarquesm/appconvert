from flask import jsonify
from flask_restful import Resource

from appconvert.ext.nomics import token_is_valid


class ValidToken(Resource):
    def get(self, token: str):
        token_list = token_is_valid(token)
        return jsonify(token_list)
