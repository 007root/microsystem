# -*- coding: utf-8 -*-
import datetime
from mongoengine import *


class User(DynamicDocument):
    """
    User model.
    """
    meta = {
        "db_alias": "pang_db",
        "indexes": ["user_id"]
    }
    name = StringField(unique=True)
    user_id = IntField(unique=True)
    password = StringField()
    phone = StringField()
    email = StringField()
    create_time = DateTimeField(default=datetime.datetime.now)
    lut = DateTimeField(default=datetime.datetime.now)

