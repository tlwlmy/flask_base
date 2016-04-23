#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 xym
#
from app import create_app
from app.common.functions import api_response
from flask.ext.script import Manager

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
