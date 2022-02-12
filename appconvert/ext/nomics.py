from typing import Dict
from flask import jsonify
from flask_restful import abort
import requests
import os


def make_request(url):
    response = requests.get(url)
    return response.json()


def valid_get_price(token1: str, token2: str, amount: float) -> Dict:
    url = f"https://api.nomics.com/v1/currencies/ticker?key={os.environ.get('SECRET_KEY_NOMICS_API')}&ids={token1}&interval=1d&convert={token2}"
    resp_json = make_request(url=url)
    if resp_json:
        return jsonify({"price": float(resp_json[0]["price"]) * amount})
    abort(404, price=None)
