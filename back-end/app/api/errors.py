# 错误处理
from flask import jsonify
from app import db
from app.api import bp
from werkzeug.http import HTTP_STATUS_CODES


def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    # 如果message不为空，就把message加入到payload中
    if message:
        payload['message'] = message
    # 返回json格式的错误信息
    response = jsonify(payload)
    # 设置状态码
    response.status_code = status_code
    return response


def bad_request(message):
    ''' 最常用的错误400：错误的请求 '''
    return error_response(400, message)


@bp.app_errorhandler(404)
def not_found_error(error):
    return error_response(404)


@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return error_response(500)