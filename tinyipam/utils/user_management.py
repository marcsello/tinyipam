#!/usr/bin/env python3
from flask_login import LoginManager


class User:

    def __init__(self, id: str):
        self._id = id

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def is_active(self):
        return True

    def get_id(self):
        return self._id


login_manager = LoginManager()
login_manager.login_view = "LoginView:index"
login_manager.login_message = None


@login_manager.user_loader
def load_user(user_id: str) -> User:
    return User(user_id)
