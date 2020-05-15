#!/usr/bin/env python3
from flask import render_template, redirect, url_for, request
from flask_classful import FlaskView
from flask_login import login_required

from model import Domain


class DomainView(FlaskView):
    decorators = [login_required]

    def index(self):
        domains = Domain.query.all()
        return render_template('domains.html', domains=domains)

    def post(self):
        form_data = dict(request.form)
        return redirect(url_for("DomainView:index"))

    def get(self, id: int):
        return render_template('domain.html')
