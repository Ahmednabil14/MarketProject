#!/usr/bin/python3
"""routes of the application"""
from web_flask import app, db
from flask import render_template, redirect, url_for
from web_flask.models import Item, User
from web_flask.forms import Register


@app.route("/", strict_slashes=False)
@app.route("/home", strict_slashes=False)
def home_page():
    return render_template("home.html")

@app.route("/market", strict_slashes=False)
def market_page():
    items = Item.query.all()
    return render_template("market.html", items=items)

@app.route("/register", strict_slashes=False, methods=["POST", "GET"])
def register_page():
    register_form = Register()
    if register_form.validate_on_submit():
        new_user = User(user_name=register_form.user_name.data,
        email=register_form.email.data,
        password=register_form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("home_page"))
    if register_form.errors:
        for err in register_form.errors.values():
            print(err)
    return render_template("register.html", form=register_form)
