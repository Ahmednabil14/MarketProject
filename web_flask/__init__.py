#!/usr/bin/python3
"""hello world"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


#  name refer to the current python file
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# must define secret key for form
app.config['SECRET_KEY'] = '03cf6f03c39ec272567bb5eb'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# defining the login page for login_required attribute
login_manager.login_view = "login_page"
# for givving log in message prettier display
login_manager.login_message_category = 'info'
# for making our application recognise our routes
from web_flask import routes
