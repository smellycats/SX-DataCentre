# -*- coding: utf-8 -*-
import time

from peewee import *

from app import db, db2


class BaseModel(Model):
    @classmethod
    def get_one(cls, *query, **kwargs):
        # 为了方便使用，新增此接口，查询不到返回None，而不抛出异常
        try:
            return cls.get(*query, **kwargs)
        except DoesNotExist:
            return None


class Users(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    banned = BooleanField(default=False)

    class Meta:
        database = db


class Carinfo(BaseModel):
    passtime = IntegerField(index=True)
    ip = CharField()
    place = IntegerField()
    content = TextField()

    class Meta:
        database = db
