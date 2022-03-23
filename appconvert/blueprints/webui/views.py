from flask import render_template

from appconvert.models import Category, Token


def home():
    return render_template("home.html")


def convert():
    tokens = Token.query.filter(Token.symbol.in_(("BTC", "ETH", "USDT"))).all()
    return render_template("convert.html", tokens=tokens)


def cryptogames():
    tokens = [token for token in Token.query.all() if token.categories]
    categories = Category.query.all()

    return render_template("cryptogames.html", tokens=tokens, categories=categories)


def defi():
    return render_template("defi.html")
