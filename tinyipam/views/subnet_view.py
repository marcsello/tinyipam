#!/usr/bin/env python3
from flask import render_template, url_for, redirect, request, flash, jsonify
from flask_classful import FlaskView
from flask_login import login_required

from marshmallow.exceptions import ValidationError

from model import db, Subnet
from schemas import SubnetSchema


class SubnetView(FlaskView):
    decorators = [login_required]
    subnet_schema = SubnetSchema(many=False, session=db.session)

    def index(self):
        subnets = Subnet.query.all()
        return render_template('subnets.html', subnets=subnets)

    def post(self):
        form_data = dict(request.form)

        try:
            s = self.subnet_schema.load(form_data, partial=True)
        except (ValidationError, ValueError) as e:
            flash(f"Validation error\n{str(e)}", "danger")
            return redirect(url_for("SubnetView:index"))

        db.session.add(s)
        db.session.commit()

        flash("Subnet successfully created!", "success")

        return redirect(url_for("SubnetView:index"))

    def get(self, id: int):
        subnet = Subnet.query.get(id)
        return render_template('subnet.html', subnet=subnet)

    def post(self, id: int):
        data = dict(request.values)
        return jsonify(data)