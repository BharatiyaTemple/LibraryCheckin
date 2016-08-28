import validators as validators
from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, RadioField
from wtforms.validators import DataRequired, Regexp, ValidationError, Email, Length, EqualTo, Optional

from models import User, Taco, Check


def email_exists(Form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that email already exists.')


class RegisterForm(Form):
    email = StringField(
        'Email',
        validators=[DataRequired(),
                    Email(),
                    email_exists
                    ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=2),
            EqualTo('password2', message='Passwords must match')
        ])
    password2 = PasswordField(
        'Confirm Password',
        validators=[DataRequired()]
    )


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class SigninForm(Form):
    phoneNumber = StringField('Enter Your 10 Digit Phone Number', [DataRequired(), Length(min=10)])

class TacoForm(Form):
    fullName = StringField('Full Name', validators=[DataRequired()])
    phoneNumber = StringField('10 Digit Phone Number', validators=[DataRequired()])
    member = RadioField(
        'Are you a Temple Member?',
        choices=[('yes', 'Yes'), ('no', 'No')], default='no'
    )
