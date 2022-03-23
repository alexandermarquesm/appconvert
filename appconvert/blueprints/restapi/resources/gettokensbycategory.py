from flask import jsonify
from flask_restful import Resource

from appconvert.ext.serialyzer import tokens_schema
from appconvert.models import Category


class GetTokensByCategory(Resource):
    def get(self, category: str) -> dict:
        resource_category = Category.query.filter_by(name=category).first()
        if resource_category:
            return jsonify(tokens=tokens_schema.dump(resource_category.tokens))
        return jsonify(price=None)
