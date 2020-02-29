#!/usr/bin/env python
#-*- coding:utf-8 -*-
''' 
@author: zhengxianjun
@contact: 1596492090@qq.com
@datetime:2020/2/27 22:21
@software: PyCharm 
'''

from extension import ma
from marshmallow import fields
from schema_field_rewrite import StringField, IntField


class UserSchema(ma.Schema):

    user_id = fields.Integer()
    username = fields.String()
    pwd = fields.String()


user_schema = UserSchema()


# 用自定义的字段重新定义schema
# 可以起到数据校验的作用
class UserFieldSchema(ma.Schema):
    user_id = IntField()
    username = StringField(required=True)
    pwd = StringField()


userField_Schema = UserFieldSchema()

