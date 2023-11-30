from flask import Blueprint
bp = Blueprint('api', __name__)

# 写在最后防止循环导入，ping.py文件也会导入bp
from app.api import ping, users, tokens