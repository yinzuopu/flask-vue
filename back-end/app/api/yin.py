
from flask import jsonify
from app.api import bp_hulk


@bp_hulk.route('/yin', methods=['GET'])
def yin():
    '''前端Vue.js用来测试与后端Flask API的连通性'''
    return jsonify('hello yin!')