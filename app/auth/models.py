#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016.05.01 tlwlmy
#
from app import db

class User(db.Model):
    # __bind_key__ = 'test2'   # 数据库路由
    __tablename__= 'user'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    date = db.Column(db.DateTime)
