# -*- coding: utf-8 -*-
import datetime
from mongoengine import *


class Custom(DynamicDocument):
    """
    Custom model.
    """
    meta = {
        "db_alias": "pang_db",
        "indexes": ["phone"]
    }
    name = StringField(unique=True)
    phone = IntField(unique=True)
    createtime = DateTimeField(default=datetime.datetime.now)


class CustomRecord(DynamicDocument):
    """
    CustomRecord model.
    """
    meta = {
        "db_alias": "pang_db",
        "indexes": ["phone"]
    }
    name = StringField()
    phone = IntField()
    integral = FloatField()
    price = IntField()
    remark = StringField()
    lut = DateTimeField(default=datetime.datetime.now)


class Integral(DynamicDocument):
    """
    Integral model.
    """
    meta = {
        "db_alias": "pang_db",
        "indexs": ["phone"]
    }
    name = StringField()
    phone = IntField(unique=True)
    integral = FloatField()
    lut = DateTimeField(default=datetime.datetime.now)


