#!/usr/bin/env python
#-*- coding:utf-8 -*-
''' 
@author: zhengxianjun
@contact: 1596492090@qq.com
@datetime:2020/2/29 17:15
@software: PyCharm 
'''

from marshmallow import fields
import typing


# 重写marshmallow里的字段 用来序列化
# 只需要重写下面两个方法即可
class StringField(fields.String):

    def _serialize(self, value, attr, obj, **kwargs) -> typing.Optional[str]:
        if value is None:
            return ''
        return str(value)

    def _deserialize(self, value, attr, data, **kwargs) -> typing.Any:
        if value is None:
            value = ''
        else:
            return str(value)


class IntField(fields.Field):

    def _serialize(self, value, attr, obj, **kwargs) -> typing.Optional[str]:
        if value is None:
            return ''
        return str(value).title()

    def _deserialize(self, value, attr, data, **kwargs) -> typing.Any:
        if value == '':
            return None
        try:
            value = int(value)
            return value
        except ValueError as e:
            raise e
