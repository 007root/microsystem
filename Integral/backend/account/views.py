from flask import Blueprint, render_template, request, jsonify, redirect, session
from account.models import User
from common.util import required_login, send_result
import json


account = Blueprint('account', __name__)


@account.route('/', methods=['GET'])
def root():
    return redirect('/index/login.html')


@account.route('/logout', methods=['GET'])
@send_result
def logout():
    del session['is_login']
    ret = {'code': 0, 'msg': ''}
    return ret


@account.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        ret = {'code': 1, 'msg': 'Invalid username or password'}
        result = None
        data = request.get_json(force=True)
        name = data.get('username')
        password = data.get('password')
        if name and password:
            result = User.objects(name=name,password=password)
        if result:
            session['is_login']= {'name':name}
            ret = {'code': 0}
        return json.dumps(ret)
    else:
        return redirect('/index/login.html')
    

#@account.route('/register', methods=['POST'])
#def register():
#    ret = {'code': 0, 'msg': ''}
#    data = request.get_json(force=True)
#    name = data.get('name')
#    password = data.get('password')
#    if name and password:
#        user = User()
#        user.name=name
#        user.password=password
#        try:
#            user.save()
#        except Exception as e:
#            ret['code'] = 1
#            ret['msg'] = ' Name exist'
#            return jsonify(ret)
#    return render_template('login.html')



