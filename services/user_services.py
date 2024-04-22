import bcrypt
from sqlalchemy import Select
from models.user_models import User
from route import db
from flask_login import login_user


class UserServers():

    def do_login(self, username: str, password: str) -> bool:
        query = Select(User).where(User.username == username)


        attempted_user = db.session.scalar(query)
        if attempted_user and attempted_user.check_password(input_password=password):
            login_user(attempted_user)
            return True
        return False
