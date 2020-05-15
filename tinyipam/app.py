#!/usr/bin/env python3
import os
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

# import stuff
from model import db, User

from utils import register_all_error_handlers, login_manager, hash_password

# import views
from views import OverviewView, SubnetView, DomainView, LoginView

# import API views
from api_views import SubnetAPIView

# create flask app
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1)
# configure flask app
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', "sqlite://")  # Default to memory db

app.config['LOCAL_API_KEY'] = os.environ['LOCAL_API_KEY']

# important stuff
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(12))
# disable this for better performance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize stuff
db.init_app(app)
login_manager.init_app(app)


@app.before_first_request
def initial_setup():
    db.create_all()

    default_username = os.environ.get('DEFAULT_USER')
    default_password = os.environ.get('DEFAULT_PASSWORD')

    if default_username and default_password:  # Create only if the default credentials are provided
        if User.query.count() == 0:  # Create default user, only if the user table is empty
            password_hashed, password_salt = hash_password(default_password)
            db.session.add(User(name=default_username, password=password_hashed, salt=password_salt))
            db.session.commit()
            app.logger.info("Users table is empty. Default user created!")


# register error handlers
register_all_error_handlers(app)

# register views
for view in [OverviewView, SubnetView, DomainView, LoginView]:
    view.register(app, trailing_slash=False)

# register API views
for view in [SubnetAPIView]:
    view.register(app, trailing_slash=False, route_prefix="/api/")

# start debuggig if needed
if __name__ == "__main__":
    app.run(debug=True)
