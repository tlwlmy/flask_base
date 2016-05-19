#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016.05.01 tlwlmy
#
from app import create_app
from app.common.functions import api_response
from flask.ext.script import Manager
from flask import url_for

app = create_app()
manager = Manager(app)

@app.route('/')
def index():
    return api_response({
        'flask_base': 'https://github.com/tlwlmy/flask_base',
    })

if __name__ == '__main__':
    # app.run()
    manager.run()

@app.route('/page')
def indexPage():
    return 'Index Page'

with app.test_request_context():
    print url_for('indexPage')
