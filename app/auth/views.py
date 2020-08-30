#!/usr/bin/env python
# encoding: utf-8
from flask import render_template

from app.auth import auth


@auth.route('/login')
def login():
    return render_template('auth/login.html')
