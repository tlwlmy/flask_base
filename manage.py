#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 xym
#
from app import create_app
#from app.common.functions import api_response
from flask.ext.script import Manager

import json
from flask import request, jsonify

def api_response(contents, code=200):
    """返回API的响应
    :param contents: dict, JSON内容
    :param code: int, HTTP CODE
    :return: response
    """
    response = jsonify(contents)
    response.status_code = code
    return response
app = create_app()
manager = Manager(app)

@app.route('/')
def index():
    return api_response({
        'adapi-cn': 'https://git.umlife.net/adsys/adapi-cn',
    })

if __name__ == '__main__':
    # app.run()
    manager.run()
