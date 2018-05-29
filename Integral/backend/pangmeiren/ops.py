# -*- coding:utf8 -*-
from pangmeiren.models import Custom, Integral, CustomRecord
from flask import Blueprint, request, session
from common.util import *
from conf import RATE
from mongoengine.errors import NotUniqueError


pang = Blueprint('pang', __name__)


@pang.route('/integral/add', methods=['POST'])
@required_login
@send_result
def integral_add():
    ret = {'code': 0, 'msg': 'succ'}
    data = request.get_json(force=True)
    phone = data.get('phone', '')
    price = data.get('price', '')
    name = data.get('name', '')
    name = name.replace(' ', '')
    if phone and price:
        try:
            phone = int(phone)
            price = int(price)
        except Exception as e:
            ret = {'code': 1, 'msg': '检查输入的手机号或者金额是否为数字'}
            return ret
        custom = Custom.objects(phone=phone)
        if not custom and not name:
            ret = {'code': 404, 'msg': '该用户不存在请输入客户姓名'}
            return ret
        elif not custom and name:
            get_phone = Custom.objects(name=name).values_list('phone')
            if get_phone:
                ret = {'code': 1, 'msg': '该用户已经绑定手机号：%s' % get_phone[0]}
                return ret
            else:
                addUser = Custom(phone=phone, name=name)
                addUser.save()
        this_integral = price / RATE
        total_integral = Integral.objects(phone=phone).values_list('integral')
        if total_integral:
            result = update_integral(phone=phone, 
                                    integral=round(total_integral[0] + this_integral, 1))
        else:
            result = update_integral(phone=phone, 
                                    integral=this_integral, 
                                    name=name)
        if result['code'] != 0:
            ret = result
        customrecord = CustomRecord(name=name,
                                    phone=phone,
                                    integral=this_integral,
                                    price=price,
                                    remark='消费')
        customrecord.save()
        ret_integral = Integral.objects(phone=phone).values_list('integral')[0]
        ret['msg'] = ret_integral
    else:
        ret = {'code': 1, 'msg': '手机号和消费金额不能为空'}
    return ret


@pang.route('/integral/info', methods=['POST'])
@required_login
@send_result
def integral_info():
    ret = {'code': 0, 'msg': 'succ'}
    data = request.get_json(force=True)
    phone = data.get('phone', '')
    try:
        phone = int(phone)
    except:
        ret = {'code': 1, 'msg': '输入正确的手机号'}
        return ret
    if phone:
        result = Integral.objects(phone=phone)
        if result:
            result = result[0]
            ret['msg'] = {'name': result.name, 
                            'phone': result.phone, 
                            'integral': result.integral, 
                            'lut': result.lut}
            print(ret['msg'])
        else:
            ret = {'code': 2, 'msg': '用户不存在'}
    else:
        ret = {'code': 1, 'msg': '星号必填'}
    return ret


@pang.route('/integral/cost', methods=['POST'])
@required_login
@send_result
def integral_cost():
    ret = {'code': 0, 'msg': 'succ'}
    data = request.get_json(force=True)
    phone = data.get('phone', '')
    cost = data.get('cost', '')
    if phone and cost:
        try:
            phone = int(phone)
            cost = int(cost)
        except:
            ret = {'code': 1, 'msg': '检查输入的手机号或者积分是否为整数数字'}
            return ret
        inte_ret = Integral.objects(phone=phone)
        if inte_ret:
            if cost < inte_ret[0].integral:
                balance = round(inte_ret[0].integral - cost, 1)
                up_ret = update_integral(phone=phone, 
                                        integral=balance)
                if up_ret['code'] == 0:
                    customrecord = CustomRecord(phone=phone, 
                                                integral=-1*cost, 
                                                name=inte_ret[0].name)
                    customrecord.save()
                    ret['msg'] = balance 
                else:
                    ret = up_ret
            else:
                ret = {'code': 1, 
                       'msg': '现有积分:%s 不足本次兑换' % inte_ret[0].integral}
        else:
            ret = {'code': 1, 'msg': '用户不存在'}
    else:
        ret = {'code': 1, 'msg': '手机号和积分兑换必填'}
    return ret


@pang.route('/sale/back', methods=['POST'])
@required_login
@send_result
def sale_back():
    ret = {'code': 0, 'msg': 'succ'}
    data = request.get_json(force=True)
    phone = data.get('phone', '')
    price = data.get('price')
    if phone and price:
        try:
            phone = int(phone)
            price = int(price)
        except:
            ret = {'code': 1, 'msg': '检查输入的手机号或者积分是否为整数数字'}
            return ret
        this_integral = price / RATE
        integral = Integral.objects(phone=phone)
        if integral:
            balance = round(integral[0].integral - this_integral, 1)
            up_ret = update_integral(phone=phone, 
                    integral=balance)
            if up_ret['code'] == 0:
                customrecord = CustomRecord(phone=phone, 
                                name=integral[0].name, 
                                price=-1*price, 
                                remark='退货')
                customrecord.save()
                ret['msg'] = (this_integral, balance)
            else:
                ret = up_ret
        else:
            ret = {'code': 1, 'msg': '此用户无积分'}
    else:
        ret = {'code': 1, 'msg': '星号必填'}
    return ret


@pang.route('/sale/exchange', methods=['POST'])
@required_login
@send_result
def sale_exchange():
    ret = {'code': 0, 'msg': 'succ'}
    data = request.get_json(force=True)
    phone = data.get('phone', '')
    ori_price = data.get('ori_price', '')
    cur_price = data.get('cur_price', '')
    if phone and ori_price and cur_price:
        try:
            phone = int(phone)
            ori_price = int(ori_price)
            cur_price = int(cur_price)
        except:
            ret = {'code': 1, 'msg': '输入必须为整数'}
            return ret
        gap_price = cur_price - ori_price
        integral = gap_price / RATE
        cur_integral = Integral.objects(phone=phone).only('integral','name')
        if cur_integral:
            cur_integral = cur_integral[0]
            balance = round(cur_integral.integral + integral, 1)
            if balance < 0:
                balance = 0
            up_ret = update_integral(phone, balance)
            if up_ret['code'] == 0:
                customrecord = CustomRecord(phone=phone, 
                                name=cur_integral.name, 
                                integral = balance,
                                price=gap_price, 
                                remark='换货')
                customrecord.save()
                ret['msg'] = (integral, balance)
            else:
                ret = up_ret['msg']
        else:
            ret = {'code': 1, 'msg': '用户不存在'}
    else:
        ret = {'code': 1, 'msg': '星号必填'}
    return ret 


