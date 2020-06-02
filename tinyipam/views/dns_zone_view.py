#!/usr/bin/env python3
from flask import render_template, redirect, url_for, request, flash
from flask_classful import FlaskView
from flask_login import login_required

from marshmallow.validate import ValidationError

from model import db, DNSZone
from schemas import DNSZoneSchema


class DNSZoneView(FlaskView):
    decorators = [login_required]
    dns_zone_schema = DNSZoneSchema(many=False, session=db.session)

    def index(self):
        zones = DNSZone.query.all()
        return render_template('dns_zones.html', zones=zones)

    def post(self):
        form_data = dict(request.form)

        try:
            s = self.dns_zone_schema.load(form_data, partial=True)
        except (ValidationError, ValueError) as e:
            flash(f"Validation error\n{str(e)}", "danger")
            return redirect(url_for("DNSZoneView:index"))

        db.session.add(s)
        db.session.commit()

        flash("Zone successfully created!", "success")

        return redirect(url_for("DNSZoneView:index"))

    def get(self, id: int):
        return render_template('dns_zone.html')
