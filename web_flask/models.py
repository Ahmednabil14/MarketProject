#!/usr/bin/python3
"""models of the app"""
from web_flask import db


class User(db.Model):
    """handel users table"""
    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=60), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), default=10000)
    items = db.relationship("Item", backref="owned_user", lazy=True)

    def __repr__(self):
        return ("User: {}".format(self.user_name))


class Item(db.Model):
    """items data base"""
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def __repr__(self):
        return ("Item: {}".format(self.name))
