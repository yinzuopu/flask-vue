from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 注册 blueprint
    from app.api import bp as api_bp
    from app.api import bp_hulk as hulk_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(hulk_bp, url_prefix='/hulk')
    return app