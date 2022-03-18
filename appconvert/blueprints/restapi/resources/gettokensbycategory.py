from flask_restful import Resource
from flask import jsonify
from appconvert.ext.serialyzer import tokens_schema
from appconvert.models import Category


class GetTokensByCategory(Resource):
    def get(self, category: str):
        return jsonify(
            {
                "tokens": tokens_schema.dump(
                    Category.query.filter_by(name=category).first().tokens
                )
            }
        )