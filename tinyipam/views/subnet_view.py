#!/usr/bin/env python3
from flask import render_template, url_for, redirect
from flask_classful import FlaskView
from flask_login import login_required

from model import db, Subnet


class SubnetView(FlaskView):
    decorators = [login_required]

    def index(self):
        subnets = Subnet.query.all()
        return render_template('subnets.html', subnets=subnets)

    def post(self):
        form_data = dict(request.form)
        return redirect(url_for("SubnetView:index"))

    def get(self, id: int):
        return render_template('subnet.html')
