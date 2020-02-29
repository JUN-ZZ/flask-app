#!/usr/bin/env python
#-*- coding:utf-8 -*-
''' 
@author: zhengxianjun
@contact: 1596492090@qq.com
@datetime:2020/2/27 22:19
@software: PyCharm 
'''

from environs import Env

# 通过这个模块 可以读取.env环境变量文件 进行配置flask
env = Env()
env.read_env()

# 通过env 读取.env文件的配置信息
FLASK_ENV = env.str("FLASK_ENV")
DEBUG = "development"
SECRET_KEY = env.str("SECRET_KEY")
# 数据库地址
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}'.format(
        username=env.str("DB_USERNAME"),
        password=env.str("DB_PASSWORD"),
        host=env.str("HOST"),
        port=env.str("DB_PORT"),
        db=env.str("DB_NAME")
    )
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True


import  datetime
#jwt 配置 如果不配置则使用 JWTManager默认值
JWT_TOKEN_LOCATION = ['cookies'] # jwt 传输方式改为cookie
JWT_COOKIE_SAMESITE = 'Strict' # 严格禁止跨站传输，防止CSRF攻击（SPA前端用户体验还行，不影响，安全最重要！）
JWT_COOKIE_CSRF_PROTECT = env.bool("JWT_COOKIE_CSRF_PROTECT") # 双重验证
JWT_COOKIE_SECURE = env.bool("JWT_COOKIE_SECURE") # 只允许https传输cookie，生产环境最好设置为True（XSS攻击防护相关）！！！
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=env.int("JWT_ACCESS_TOKEN_EXPIRES_DAYS")) # 过期时间设置
JWT_BLACKLIST_ENABLED = env.bool("JWT_BLACKLIST_ENABLED")
JWT_BLACKLIST_TOKEN_CHECKS = env.list("JWT_BLACKLIST_TOKEN_CHECKS")



