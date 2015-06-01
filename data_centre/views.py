# -*- coding: utf-8 -*-
import os
import json
import time
import datetime
import threading
import Queue
import logging

from flask import g, request
from flask_restful import reqparse, abort, Resource
from passlib.hash import sha256_crypt

from app import app, db, api, auth
from models import Users, Carinfo
import gl


logger = logging.getLogger('root')


@app.before_request
def before_request():
    g.db = db
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


class Index(Resource):

    def get(self):
        return {'msg': "Welcome to use SX-DataCentre %s" % app.config['VERSION']}


class DataListApiV1(Resource):

    def post():
        parser = reqparse.RequestParser()

        parser.add_argument('passtime', type=unicode, required=True,
                            help='A passtime is require', location='json')
        args = parser.parse_args()

        folder = request.json['passtime'].strftime("%Y%m/%d/%H")
        filepath = os.path.join(app.config['BASEPATH'], folder)
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        f = request.files['file']
        f.save(os.path.join(filepath, '%s.jpg' % datetime.datetime.now().strftime( "%Y-%m-%d%H%M%S")))

        return {'code':100,'msg':'Created'}, 201


api.add_resource(Index, '/')
api.add_resource(DataListApiV1, '/api/v1/data')


