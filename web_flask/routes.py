#!/usr/bin/python3
"""routes of the application"""
from web_flask import app, db
# get_flashed_messages use for collecting error is one list
from flask import render_template, redirect, url_for, flash, get_flashed_messages, request
from web_flask.models import Item, User
from web_flask.forms import Register, Login, PurchaseItems, SellItem
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/", strict_slashes=False)
@app.route("/home", strict_slashes=False)
def home_page():
    return render_template("home.html")

@app.route("/market", strict_slashes=False, methods=["POST", "GET"])
@login_required
def market_page():
    purchase_form = PurchaseItems()
    selling_form = SellItem()
    if request.method == "POST":
        # for purchasing
        purchased_item_id = request.form.get("purchased_item")
        purchased_item_obj = Item.query.filter_by(id=purchased_item_id).first()
        if purchased_item_obj:
            if current_user.can_purchase(purchased_item_obj) and purchased_item_obj.in_stock > 0:
                purchased_item_obj.in_stock -= 1
                purchased_item_obj.user_id = current_user.id
                current_user.budget -= purchased_item_obj.price
                db.session.commit()
                flash("You purchased {} for {}$".format(
                    purchased_item_obj.name, purchased_item_obj.price), category="success")
            else:
                flash("You don't have enough money !", category="danger")
        # for selling items
        sold_item_id = request.form.get("sold_item")
        sold_item_obj = Item.query.filter_by(id=sold_item_id).first()
        if sold_item_obj:
            sold_item_obj.user_id = None
            sold_item_obj.in_stock += 1
            current_user.budget += sold_item_obj.price
            db.session.commit()
            flash("You sold {} for {}$".format(
                sold_item_obj.name, sold_item_obj.price), category="success")
        return redirect(url_for("market_page"))

    if request.method == "GET":
        items = Item.query.filter_by(user_id=None)
        my_items = Item.query.filter_by(user_id=current_user.id)
        # items = Item.query.filter(Item.in_stock > 0)
        return render_template("market.html", items=items, purchase_form=purchase_form,
                               my_items=my_items, selling_form=selling_form)

@app.route("/register", strict_slashes=False, methods=["POST", "GET"])
def register_page():
    register_form = Register()
    if register_form.validate_on_submit():
        new_user = User(user_name=register_form.user_name.data,
        email=register_form.email.data,
        password=register_form.password.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash("Welcome {}".format(new_user.user_name), category='success')
        return redirect(url_for("home_page"))
    if register_form.errors:
        for err in register_form.errors.values():
            flash(err, category='danger')
    return render_template("register.html", form=register_form)

@app.route("/login", strict_slashes=False, methods=["POST", "GET"])
def login_page():
    login_form = Login()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user:
            if user.check_password_match(login_form.password.data):
                login_user(user)
                flash("Welcome {}".format(user.user_name), category='success')
                return redirect(url_for('home_page'))
            else:
                flash("Incorrect password!", category='danger')
        else:
            flash("The email address you entered isn't connected to an account.", category='danger')
    if login_form.errors:
        for err in login_form.error.values():
            flash(err, category='danger')
    return render_template("login.html", form=login_form)


@app.route("/logout", strict_slashes=False)
def logout_page():
    logout_user()
    return redirect(url_for("home_page"))
