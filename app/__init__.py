#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 xym
#
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config, run_env
db = SQLAlchemy()

def create_app(config_name=None):
    app = Flask(__name__)
    if not config_name:
        config_name = run_env
    app.config.from_object(config[config_name])
    print config[config_name]
    config[config_name].init_app(app)
    db.init_app(app)

    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler(app.config['LOG_PATH'],
                                       maxBytes=1024*1024, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
