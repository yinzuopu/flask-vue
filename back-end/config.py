import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'), encoding='utf-8')


# 定义一个名为Config的类，它继承自object，这是一个基础的Python类
class Config(object):
    # 从环境变量中获取'DATABASE_URL'的值，并将其设置为SQLALCHEMY_DATABASE_URI的值  
    # 如果环境变量中没有'DATABASE_URL'，则使用SQLite数据库，它的地址是相对路径（basedir）下的'app.db'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')

    # 关闭SQLAlchemy的修改跟踪。当SQLAlchemy跟踪模型修改时，这可以防止程序在没有明确调用commit()的情况下自动提交事务
    SQLALCHEMY_TRACK_MODIFICATIONS = False