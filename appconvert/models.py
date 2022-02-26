from appconvert.ext.database import db
from enum import unique


categories = db.Table(
    "categories",
    db.Column("token_id", db.Integer, db.ForeignKey("token.id"), primary_key=True),
    db.Column(
        "category_id", db.Integer, db.ForeignKey("category.id"), primary_key=True
    ),
)


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_api = db.Column(db.String(8), unique=True, nullable=False)
    currency = db.Column(db.String(8), unique=True, nullable=False)
    symbol = db.Column(db.String(8), unique=False, nullable=False)
    name = db.Column(db.String(25), unique=True, nullable=False)
    logo_url = db.Column(db.String(85), nullable=False)

    marketcap = db.Column(db.String(15), nullable=True)
    price = db.Column(db.String(20), nullable=True)
    blockchain = db.Column(db.String(60), nullable=True)
    address = db.Column(db.String(60), nullable=True)
    site = db.Column(db.String(60), nullable=True)
    categories = db.relationship(
        "Category",
        secondary=categories,
        lazy="subquery",
        backref=db.backref("tokens", lazy=True),
    )


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
