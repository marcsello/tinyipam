#!/usr/bin/env python3
from flask import render_template
from flask_classful import FlaskView


class SubnetView(FlaskView):

    def index(self):
        return render_template('subnets.html')

    def get(self, id: int):
        return render_template('subnets.html')
