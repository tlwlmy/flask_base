#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 xym
#
from flask import session, render_template, redirect, flash, url_for
from app.auth import auth
from app.auth.models import User
from app import db
from flask import request
from app.common.functions import api_response

@auth.route('/index', methods=['GET', 'POST'])
def index():
    return 'Hello world!'

@auth.route('/users', methods=['GET'])
def get_users():
    output = {
        'c': 0,
        'users': []
    }

    user = User.query.all()
    for u in user:
        output['users'].append({'uid': u.uid, 'name': u.name})

    return api_response(output)


