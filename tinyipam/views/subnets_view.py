#!/usr/bin/env python3
from flask import render_template
from flask_classful import FlaskView

class SubnetsView(FlaskView):

    def index(self):
            return render_template('subnets.html')
