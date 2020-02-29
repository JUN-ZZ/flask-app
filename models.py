#!/usr/bin/env python
#-*- coding:utf-8 -*-
''' 
@author: zhengxianjun
@contact: 1596492090@qq.com
@datetime:2020/2/27 22:20
@software: PyCharm 
'''

from extension import db


# 定义表 model 对应数据库表
class User(db.Model):
    # 表名 __tablename__
    __tablename__ = 'user'
    user_id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(30))
    pwd = db.Column(db.String())


class Token(db.Model):

    __tablenmae__ = 'token'
    t_id = db.Column(db.INTEGER,primary_key=True)
    jti = db.Column(db.String(100))


