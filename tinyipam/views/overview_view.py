#!/usr/bin/env python3
from flask import render_template
from flask_classful import FlaskView
from flask_login import login_required


class OverviewView(FlaskView):
    decorators = [login_required]

    route_base = '/'

    def index(self):
        return render_template('overview.html')
