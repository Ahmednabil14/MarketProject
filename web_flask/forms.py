#!/usr/bin/python3
"""register form"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError
from web_flask.models import User

class Register(FlaskForm):

    # function must call validate_(the field_name)
    def validate_user_name(self, user_to_create):
        user = User.query.filter_by(user_name=user_to_create.data).first()
        if user:
            raise ValidationError("This user already exists!")

    def validate_email(self, email_to_create):
        email = User.query.filter_by(email=email_to_create.data).first()
        if email:
            raise ValidationError('This email already exists!')

    user_name = StringField(label='User Name', validators=[Length(min=4, max=30), DataRequired()])
    email = StringField(label='Email', validators=[Length(max=60), Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=6, max=60), DataRequired()])
    password_confirm = PasswordField(label='Confirm Password', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Sign Up')


class Login(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log in')

class PurchaseItems(FlaskForm):
    submit = SubmitField(label='Purchase')
