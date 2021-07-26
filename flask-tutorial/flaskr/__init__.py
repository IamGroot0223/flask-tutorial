import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app=Flask(__name__,instance_relative_config=True)
    #默认False，配置对象提供从相对文件名来载入配置的方式，
    # 也使得它从相对实例路径的文件名加载成为可能，配置文件中的相对路径的行为可
    # 以在“相对应用的根目录”（默认）和 “相对实例文件夹”中切换
    # 创建实例，并同时启用实例文件夹（instance_relative_config：告诉应用——配置文件是相对于instance folder的相对路径）
    app.config.from_mapping(       #通过mapping获取配置信息
        SECRET_KEY='dev',# 这里为了方便，使用了简单的密钥
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite'),
    # 指定正式环境和测试环境的配置文件
    )
    if test_config is None: #配置存在，没有测试
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello,World!"
    return app
