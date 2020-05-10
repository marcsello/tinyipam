#!/usr/bin/env python3
from flask import render_template
from flask_classful import FlaskView


import requests.exceptions


class HomeView(FlaskView):

    route_base = '/'

    def index(self):
            return render_template('home.html')
