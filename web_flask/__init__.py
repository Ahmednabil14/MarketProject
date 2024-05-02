#!/usr/bin/python3
"""hello world"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#  name refer to the current python file
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '03cf6f03c39ec272567bb5eb'
db = SQLAlchemy(app)
# for making our application recognise our routes
from web_flask import routes