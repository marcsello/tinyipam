#!/usr/bin/env python3
from flask import render_template, redirect, url_for, request, flash
from flask_classful import FlaskView
from flask_login import login_required

from marshmallow.validate import ValidationError

from model import db, Domain
from schemas import DomainSchema


class DomainView(FlaskView):
    decorators = [login_required]
    domain_schema = DomainSchema(many=False, session=db.session)

    def index(self):
        domains = Domain.query.all()
        return render_template('domains.html', domains=domains)

    def post(self):
        form_data = dict(request.form)

        try:
            s = self.domain_schema.load(form_data, partial=True)
        except (ValidationError, ValueError) as e:
            flash(f"Validation error\n{str(e)}", "danger")
            return redirect(url_for("SubnetView:index"))

        db.session.add(s)
        db.session.commit()

        flash("Domain successfully created!", "success")

        return redirect(url_for("DomainView:index"))

    def get(self, id: int):
        return render_template('domain.html')
