#!/usr/bin/env python
#-*- coding:utf-8 -*-
''' 
@author: zhengxianjun
@contact: 1596492090@qq.com
@datetime:2020/2/27 22:31
@software: PyCharm 
'''

from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# 用来jwt token 认证登录
jwt = JWTManager()

# 因为flask没有自带json解析对象的功能 而Java spring boot等框架有
# 所以 这个用来解析前端 和返回给前端的json 功能
ma = Marshmallow()

# 由于flask 对表结构改变 如添加字段 和删除字段 没有自动修改的功能 而spring data jpa 是有的
# 所有用这个来改变表结构和对数据进行迁移
# 主要命令是 1.flask db init 初始化
# 2.flask db migrate -m " message" 生成迁移文件
# 3.flask db upgrade 用来更新数据库 即运行2产生的迁移文件 如果一开始就有迁移文件 可以直接运行这步
# 以后有修改表model结构 就直接运行2和3
migrate = Migrate()

# orm
db = SQLAlchemy()
