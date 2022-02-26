from flask import render_template
from appconvert.models import Token


def home():
    return render_template("home.html")


def convert():
    tokens = Token.query.filter(Token.symbol.in_(("BTC", "ETH", "USDT"))).all()
    return render_template("convert.html", tokens=tokens)


def cryptogames():
    return render_template("cryptogames.html")


def defi():
    return render_template("defi.html")
