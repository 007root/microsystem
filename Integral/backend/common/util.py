import subprocess
from flask import session
from functools import wraps
import json
import datetime
from pangmeiren.models import Custom, Integral


def _json_default(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.strftime('%Y-%m-%d %H:%M:%S')


def required_login(fun):
    @wraps(fun)
    def wrap(*args, **kwargs):
        if session.get('is_login'):
            return fun(*args, **kwargs)
        else:
            return json.dumps({'code': 503, 'msg': '/'})
    return wrap


def send_result(fun):
    @wraps(fun)
    def wrap(*args, **kwargs):
        ret = fun(*args, **kwargs)
        if isinstance(ret, dict):
            return json.dumps(ret, default=_json_default)
        else:
            return ret
    return wrap


def update_integral(phone, integral, name=None):
    ret = {'code': 0, 'msg': 'succ'}
    try:
        if name:
            inte = Integral(name=name, phone=phone, integral=integral)
            inte.save()
        else:
            Integral.objects(phone=phone).update(integral=integral)
    except Exception as e:
        ret= {'code': 1, 'msg': str(e)}
    return ret


