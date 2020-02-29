#!/usr/bin/env python
#-*- coding:utf-8 -*-
''' 
@author: zhengxianjun
@contact: 1596492090@qq.com
@datetime:2020/2/27 22:50
@software: PyCharm 
'''

from flask import Blueprint
from models import User
from flask import request, jsonify
from flask_jwt_extended import (
    fresh_jwt_required,
    jwt_required,
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies
)
from extension import db
from werkzeug.security import check_password_hash , generate_password_hash
from schema import userField_Schema


# 初始化蓝图 ，相当于Java spring框架的controller
main_bp = Blueprint('main',__name__, url_prefix='/main')


@main_bp.route('/register',methods=(['POST']))
def register():
    json = request.json
    username = json.get('username')
    pwd = json.get('pwd')
    pwd = generate_password_hash(pwd)

    u = User.query.filter_by(username==username).first()
    if u is not None:
        return jsonify({'result':'该用户名已存在'}), 200
    uu = User(username=username,pwd=pwd)
    db.session.add(uu)
    db.session.commit()

    # 创建token
    token = create_access_token(identity=u.user_id)
    refresh_token = create_refresh_token(identity=u.user_id)

    data = {
        "access_token": token,
        "": refresh_token,
        'result': 'register success',
        'code': 200
    }
    resp = jsonify(data)

    # 设置cookie token会在cookie中
    set_access_cookies(response=resp, encoded_access_token=token)
    set_refresh_cookies(response=resp, encoded_refresh_token=refresh_token)

    return resp, 200


@main_bp.route('/login', methods=(['GET']))
@fresh_jwt_required
def login():
    # 这个是视图函数，就是相当于spring controller里面的方法
    # 不过这个要注册到app中
    #  to do
    json = request.json
    username = json.get('username')
    pwd = json.get('pwd')
    pwd = generate_password_hash(pwd)
    # 从数据库中验证
    u = User.query.filter(User.username ==username,User.pwd==pwd).first()
    if u is None:
        return jsonify({'result':'用户名 或密码不正确'}),401

    # 创建token
    token = create_access_token(identity=u.user_id)
    refresh_token = create_refresh_token(identity=u.user_id)

    data = {
        "access_token":token,
        "":refresh_token,
        "message":'welcome login ',
        'result':'success',
        'code':200
    }
    resp = jsonify(data)

    # 设置cookie token会在cookie中
    set_access_cookies(response=resp,encoded_access_token=token)
    set_refresh_cookies(response=resp,encoded_refresh_token=refresh_token)

    return resp, 200


@main_bp.route('/getUserByName', methods=(['POST']))
@fresh_jwt_required
def get_user():
    # 通过flask 的request 获取前端传过来的json数据
    json = request.json
    username = json.get('username')
    u = User.query.filter_by(username==username).all()
    # 进行序列化
    u = userField_Schema.dump(u)

    return jsonify(u),200


@main_bp.route('/add', methods=(['POST']))
@fresh_jwt_required
def add_user():
    # 通过flask 的request 获取前端传过来的json数据
    json = request.json
    # 进行数据反序列化 解析和校验数据对应schema的字段 带有required=True 是必要字段 没有的话会报错
    # schema 的字段可以自定义
    data = userField_Schema.load(json)
    u = User(**data)
    db.session.add(u)
    db.session.commit()
    # 进行序列化对象 对应schema的字段 返回json数据
    json_dump = userField_Schema.dump(u,many=True)

    return jsonify(json_dump),200




