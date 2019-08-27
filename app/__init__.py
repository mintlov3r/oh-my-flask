from flask import Flask


def register_blueprint(app):
    from app.api.views import api
    app.register_blueprint(api, url_prefix='/api')
    from app.movie.views import movie
    app.register_blueprint(movie, url_prefix='/movie')
    from app.main.views import main
    app.register_blueprint(main)
    

def register_plugins(app):
    pass

def create_app():
    # 初始化
    app = Flask(__name__)

    # 注册路由和蓝图
    register_blueprint(app)
    
    # 注册插件
    register_plugins(app)

    return app