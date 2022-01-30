from flask import render_template


def home():
    return render_template("home.html")


def convert():
    return render_template("convert.html")


def cryptogames():
    return render_template("cryptogames.html")


def defi():
    return render_template("defi.html")
