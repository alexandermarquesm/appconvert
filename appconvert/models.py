from appconvert.ext.database import db
from enum import unique


"""class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    ticker = db.Column(db.String(6), unique=True, nullable=False)
    price = db.Column(db.String(20), nullable=False)
    marketcap = db.Column(db.String(15), nullable=False)
    blockchain = db.Column(db.String(60), nullable=False)
    site = db.Column(db.String(60), unique=True, nullable=False)
    categories = db.relationship(
        "Category",
        secondary=categories,
        lazy="subquery",
        backref=db.backref("tokens", lazy=True),
    )


categories = db.Table(
    "categories",
    db.Column("token_id", db.Integer, db.ForeignKey("token.id"), primary_key=True),
    db.Column(
        "category_id", db.Integer, db.ForeignKey("category.id"), primary_key=True
    ),
)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
"""

categories = db.Table(
    "categories",
    db.Column("token_id", db.Integer, db.ForeignKey("token.id"), primary_key=True),
    db.Column(
        "category_id", db.Integer, db.ForeignKey("category.id"), primary_key=True
    ),
)


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    ticker = db.Column(db.String(6), unique=True, nullable=False)
    price = db.Column(db.String(20), nullable=False)
    marketcap = db.Column(db.String(15), nullable=False)
    blockchain = db.Column(db.String(60), nullable=False)
    site = db.Column(db.String(60), unique=True, nullable=False)
    categories = db.relationship(
        "Category",
        secondary=categories,
        lazy="subquery",
        backref=db.backref("tokens", lazy=True),
    )


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
