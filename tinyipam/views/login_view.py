#!/usr/bin/env python3
from flask import render_template
from flask_classful import FlaskView


class LoginView(FlaskView):

    def index(self):
        return render_template('login.html')

    def post(self):
        return render_template('login.html')
