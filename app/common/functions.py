#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
