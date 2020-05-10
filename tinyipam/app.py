#!/usr/bin/env python3
import os
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

# import stuff
from model import db

from utils import register_all_error_handlers

# import views
from views import HomeView

# import API views
from api_views import HelloView


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

with app.app_context():
	db.create_all()

# register error handlers
register_all_error_handlers(app)

# register views
for view in [HomeView]:
	view.register(app, trailing_slash=False)


# register API views
for view in [HelloView]:
	view.register(app, trailing_slash=False, route_prefix="/api/")

# start debuggig if needed
if __name__ == "__main__":
	app.run(debug=True)
