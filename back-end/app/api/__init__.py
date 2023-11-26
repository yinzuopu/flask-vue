from flask import Blueprint

bp = Blueprint('api', __name__)


# 写在最后是为了防止循环导入，ping.py文件也会导入 bp
from app.api import ping

bp_hulk = Blueprint('hulk', __name__)
from app.api import yin
