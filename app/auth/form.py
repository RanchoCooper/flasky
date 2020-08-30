#!/usr/bin/env python
# encoding: utf-8
from flask_wtf import Form
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import Email, Length, Required


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log In')
