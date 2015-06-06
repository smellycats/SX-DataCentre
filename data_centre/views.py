# -*- coding: utf-8 -*-
import os
import json
import time
import datetime

from flask import g, request
from flask_restful import reqparse, abort, Resource
from passlib.hash import sha256_crypt

from app import app, db, db2, api, auth, logger
from models import Users, Carinfo


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
        return {'data_url': 'http://localhost/v1/data'}


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
        f.save(os.path.join(filepath, '%s.jpg' % datetime.datetime.now().strftime("%Y-%m-%d%H%M%S")))

        return {'code': 100, 'msg': 'Created'}, 201


class TestList(Resource):

    def get(self):
        try:
            c = Carinfo.get(Carinfo.id == 1)
            print c
        except Exception as e:
            print e
        return {'code': 100}

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('passtime', type=unicode, required=True,
                            help='A passtime is require', location='json')
        args = parser.parse_args()

        Carinfo.create(passtime=int(time.time()),
                       ip='127.0.0.1', place=2,
                       content='{"passtime":45}')

        return {'code': 100, 'msg': 'Created'}, 201


class Test(Resource):

    def get(self, test_id):
        c = Carinfo.get(Carinfo.id == test_id)
        return {'content': c.content}


api.add_resource(Index, '/')
api.add_resource(TestList, '/test')
api.add_resource(Test, '/test/<test_id>')
api.add_resource(DataListApiV1, '/v1/data')
