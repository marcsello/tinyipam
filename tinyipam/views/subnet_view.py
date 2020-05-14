#!/usr/bin/env python3
from flask import render_template
from flask_classful import FlaskView
from flask_login import login_required


class SubnetView(FlaskView):
    decorators = [login_required]

    def index(self):
        return render_template('subnets.html')

    def get(self, id: int):
        return render_template('subnet.html')
