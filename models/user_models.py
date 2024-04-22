from datetime import datetime

import bcrypt
from flask_login import UserMixin
from route import db, login_manager
from sqlalchemy import Integer, String, TIMESTAMP, BLOB, func, Select
from sqlalchemy.orm import Mapped, mapped_column


# flask_manager.的一个标签，他会自动帮你查询用户会话连接，但是需要指定查询方法
@login_manager.user_loader
def get_user(user_id):
    query = Select(User).where(User.id==user_id)
    return db.session.scalar(query)


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(100), unique=False, nullable=False)
    fullname: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=True)

    def check_password(self, input_password):
        return bcrypt.checkpw(input_password.encode(), self.password.encode())
