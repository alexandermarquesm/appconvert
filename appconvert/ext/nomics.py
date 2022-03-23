import pickle
import time
from typing import Dict

import requests

from config import settings


def make_request(url: str):
    response = requests.get(url)
    return response


def valid_get_price(token1: str, token2: str, amount: float) -> Dict:
    url = f"https://api.nomics.com/v1/currencies/ticker?key={settings['SECRET_KEY_NOMICS_API']}&ids={token1}&interval=1d&convert={token2}&per-page=1"
    resp_json = make_request(url=url).json()
    if resp_json:
        return float(resp_json[0]["price"]) * amount
    return None


def token_is_valid(token: str) -> Dict:
    token_lista = []
    with open("appconvert/tokens.json", "rb") as file:
        data = pickle.load(file)
        for token_data in data:
            if token_data["symbol"] == token:
                if token_data["logo_url"]:
                    token_lista.append(
                        {
                            "id": token_data["id"],
                            "symbol": token_data["symbol"],
                            "name": token_data["name"],
                            "logo_url": token_data["logo_url"],
                        }
                    )
    time.sleep(1)
    return {"tokens": token_lista}
