## 代码结构

- migrations 迁移文件 
git之后 直接 在根目录运行flask db upgrade 升级数据库会自动创建表

- utils 工具模块

- views 该包下编写视图函数，也就是controller 编写接口

- .env 环境变量文件 flask 会自动扫描该文件

- app.py 启动模块 用flask run 内置命令 自动扫描create_app工厂函数创建实例app

- extension.py 扩展模块

- models.py SQLAlchemy 定义的模型 orm 对应数据库表模型，改变字段等操作时要运用flask db migrate -m " message" 生成迁移文件 进行数据库更新

- requeriment.txt 该程序所需依赖

- schema.py 序列化所需的对应校验等 

- schema_field_rewrite.py schema的自定义字段对Marshmallow的内置字段进行重写

- setting.py app配置文件

持续更新中...
