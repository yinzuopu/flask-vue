from flask import Flask
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# flask_sqlalchemy插件
db = SQLAlchemy()

# flask_migrate插件
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # enable CORS
    CORS(app)

    # 初始化flask_sqlalchemy
    db.init_app(app)

    # 初始化flask_migrat
    migrate.init_app(app, db)

    # 注册蓝图
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

from app import models
