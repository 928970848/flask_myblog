import os

import bcrypt
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from sqlalchemy import inspect

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../assets',
            static_url_path='/assets')

host = os.getenv('MYSQL_HOST', '127.0.0.1')
port = os.getenv('MYSQL_PORT', '3306')
mysql_db = os.getenv('MYSQL_DB', 'flask')
user = os.getenv('MYSQL_USER', 'root')
pwd = os.getenv('MYSQL_PWD', 'root')

# flask-sqlalchemy准备工作
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{user}:{pwd}@{host}:{port}/{mysql_db}'
db = SQLAlchemy(app)

# flask_login的准备工作
app.config['SECRET_KEY'] = 'J221jkl3432hJ3N23HK'
csrf = CSRFProtect(app)  # 创建csrf_token令牌
login_manager = LoginManager(app)

from route import user_routes
from route import admin_routes

# 创建应用上下文，db.create_all只可在应用上下文中执行
with app.app_context():
    inspector =  inspect(db.engine)
    if not inspector.has_table('user'):  # 判断是否存在user表
        db.create_all()  # 创建表，表模型由user_routes、admin_routes文件内导入模型文件
        password = bcrypt.hashpw('123456'.encode(),bcrypt.gensalt())
        from models.user_models import User
        user = User(username='root', password=password.decode('utf-8'), fullname='管理员')  # 创建
        db.session.add(user)
        db.session.commit()