# -*- coding: utf-8 -*-
import logging

from flask import Flask
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth
from flask.ext.sqlalchemy import SQLAlchemy
from peewee import SqliteDatabase


# create a flask application - this ``app`` object will be used to handle
app = Flask(__name__)
app.config.from_pyfile('config.py')
api = Api(app)

db = SqliteDatabase(app.config['DATABASE'], journal_mode='WAL')
db2 = SQLAlchemy(app)

auth = HTTPBasicAuth()

logger = logging.getLogger('root')
