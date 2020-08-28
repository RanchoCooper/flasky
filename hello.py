#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, request
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    user_agent = request.headers.get('User-agent')
    return '<h1>hello, world!</h1>\nyour browser is %s' % user_agent


@app.route('/user/<name>')
def user(name):
    return '<h1>hello, %s!</h1>' % name


if __name__ == '__main__':
    manager.run()
