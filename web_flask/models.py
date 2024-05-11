#!/usr/bin/python3
"""models of the app"""
from web_flask import db, login_manager
from web_flask import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# should extends from USerMix in class
class User(db.Model, UserMixin):
    """handel users table"""
    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=60), nullable=False, unique=True)
    hash_password = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), default=10000)
    items = db.relationship("Item", backref="owned_user", lazy=True)

    def can_purchase(self, item_obj):
        return self.budget >= item_obj.price
    @property
    def password(self):
        return self.hash_password
    
    @password.setter
    def password(self, password):
        self.hash_password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password_match(self, password):
        return bcrypt.check_password_hash(self.hash_password, password)

    @property
    def budget_in_digits(self):
        budget_string = str(self.budget)
        if len(budget_string) > 4:
            return ("{}, {}".format(budget_string[:-3], budget_string[-3:]))
        return self.budget


        return self.budget
    
    def __repr__(self):
        return ("User: {}".format(self.user_name))


class Item(db.Model):
    """items data base"""
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    in_stock = db.Column(db.Integer(), nullable=False, default=3)
    description = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def __repr__(self):
        return ("Item: {}".format(self.name))
