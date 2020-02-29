from flask import Flask

# app = Flask(__name__)

# IDE自带创建的 example
# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# 使用工厂函数创建app实例，这时候使用flask run 内置命令
# if __name__ == '__main__':
#     app.run()


def create_app():
    '''
    工厂函数，创建flask app实例  通过flask run 内置命令启动 并加载各个模块
    :return:
    '''
    from flask import Flask
    # 1.实例化 app 实例
    app = Flask(__name__)
    #  2.加载配置文件 从 根目录下找
    app.config.from_object('setting')
    # 3.注册扩展模块
    register_extension(app)
    # 4.注册蓝图，视图函数
    register_blueprint(app)

    return app


def register_extension(app):
    '''
    加载扩展模块，并且配置各个模块
    :param app:
    :return:
    '''
    # 加载扩展模块
    from extension import jwt
    from extension import db
    from extension import ma
    from extension import migrate
    #  将扩展模块注册到app 中
    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    migrate.init_app(app,db=db)

    # 配置jwt
    config_jwt(jwt=jwt)

    return None


def register_blueprint(app):
    '''
        注册蓝图
    :param app:
    :return:
    '''
    from view.main import main_bp
    app.register_blueprint(main_bp)
    return None


def config_jwt(jwt):
    '''
        配置jwt
    :param jwt:
    :return:
    '''
    @jwt.token_in_blacklist_loader
    def token_in_blacklist_loader(decoded_jwt):
        # identity =
        #
        pass
    pass


