#!/usr/bin/env python3
from flask import render_template
from flask_classful import FlaskView


class OverviewView(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('overview.html')
