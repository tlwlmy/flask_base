#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016.05.01 tlwlmy
#
from flask import session, render_template, redirect, flash, url_for
from app.auth import auth
from app.auth.models import User
from app import db, redis_store, cache
from flask import request
from app.common.functions import api_response
import time

@auth.route('/index', methods=['GET', 'POST'])
def index():
    return 'Hello world!'

@auth.route('/users', methods=['GET'])
def get_users():
    output = {
        'c': 0,
        'users': []
    }

    query_time = redis_store.get('query_time')
    if query_time is None:
        query_time = time.time()
        redis_store.set('query_time', query_time, 3600)

    output['query_time'] = query_time
    user = User.query.all()
    for u in user:
        output['users'].append({'uid': u.uid, 'name': u.name})

    session['time'] = time.time()

    return api_response(output)

@auth.route('/cache')
@cache.cached(timeout=5, key_prefix='cached_test')
def root():
    t = time.time()
    return str(t)

