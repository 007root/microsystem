# -*- coding: utf-8 -*-


import flask
import conf
from account.views import account
from pangmeiren.ops import pang
from flask import session
from datetime import timedelta


app = flask.Flask('pangmeiren')
app.secret_key = 'u3/d/*73ldjfosa21l*@j3d'
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)

app.register_blueprint(account)
app.register_blueprint(pang, url_prefix="/manage")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6666, debug=True)



