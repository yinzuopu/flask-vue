from app import db
import base64
from datetime import datetime, timedelta
import os
from flask import url_for
from werkzeug.security import generate_password_hash, check_password_hash


# API 中有 POST /users 需要返回用户集合，所以还需要添加 to_collection_dict 方法。考虑到后续会创建 Post 等数据模型，
# 所以在 app/models.py 中设计一个通用类 PaginatedAPIMixin
class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        # query：查询结果
        # page：当前页数
        # per_page：每页显示的记录数
        # endpoint：生成的URL链接
        # **kwargs：其他参数
        resources = query.paginate(page, per_page, False)   # 分页查询
        data = {
            'items': [item.to_dict() for item in resources.items],   # 查询结果转换成字典
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,   # 总页数
                'total_items': resources.total   # 总记录数
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page, **kwargs),   # 生成一个URL链接
                'next': url_for(endpoint, page=page + 1, per_page=per_page, **kwargs) if resources.has_next else None,   # 下一页
                'prev': url_for(endpoint, page=page - 1, per_page=per_page, **kwargs) if resources.has_prev else None   # 上一页
            }
        }
        return data


class User(PaginatedAPIMixin, db.Model):
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))   # 不保存原始密码

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, passworld):
        self.password_hash = generate_password_hash(passworld)

    def check_password(self, passworld):
        return check_password_hash(self.password_hash, passworld)

    # 定义一个to_dict方法，用于将User对象转换成字典形式，如果include_email为True，那么会包含email字段
    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'username': self.username,
            '_links':{
                'self': url_for('api.get_user', id=self.id)   # 生成一个URL链接
            }
        }
        if include_email:
            data['email'] = self.email   # 如果include_email为True，那么会包含email字段
        return data

    def from_dict(self, data, new_user=False):
        # new_user：是否为新用户
        for field in ['username', 'email']:
            if field in data:
                setattr(self, field, data[field])   # 设置属性
        if new_user and 'password' in data:
            self.set_password(data['password'])   # 设置密码

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user
