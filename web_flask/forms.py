#!/usr/bin/python3
"""register form"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired


class Register(FlaskForm):
    user_name = StringField(label='User Name:', validators=[Length(min=4, max=30), DataRequired()])
    email = StringField(label='Email:', validators=[Length(max=60), Email(), DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=6, max=60), DataRequired()])
    password_confirm = PasswordField(label='Confirm Password:', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Sign Up')
