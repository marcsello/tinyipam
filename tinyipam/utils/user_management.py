#!/usr/bin/env python3
from model import User
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = "LoginView:index"
login_manager.login_message = None


@login_manager.user_loader
def load_user(user_id: str) -> User:
    return User.query.get(int(user_id))



