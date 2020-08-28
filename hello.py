#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, render_template, request
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    user_agent = request.headers.get('User-agent')
    return render_template('index.html', user_agent=user_agent)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    manager.run()
