#!/usr/bin/env python3
from flask import render_template, redirect, request, flash, url_for, current_app
from flask_classful import FlaskView
from flask_login import login_user, logout_user, login_required, current_user
from model import User
from utils import hash_password_with_salt


class LoginView(FlaskView):

    def index(self):
        if current_user.is_authenticated:
            return redirect(url_for("OverviewView:index"))

        return render_template('login.html')

    def post(self):
        if current_user.is_authenticated:
            return redirect(url_for("OverviewView:index"))

        provided_credentials = dict(request.form)

        # TODO: Check if the dbms supports hashing, and use it for credential retrival

        u = User.query.filter_by(name=provided_credentials['username']).first()

        if not u:
            flash("Username or password incorrect.", "danger")
            return redirect(url_for("LoginView:index"))

        # Check password

        if hash_password_with_salt(provided_credentials['password'], u.salt) == u.password:
            login_user(u)
            flash("Welcome back!", "success")
            current_app.logger.info(f"New login by {u.name}")
            return redirect(url_for("OverviewView:index"))  # TODO: use next parameter to determine the next view

        else:
            flash("Username or password incorrect.", "danger")
            return redirect(url_for("LoginView:index"))

    @login_required
    def logout(self):
        logout_user()
        flash("Successful logout!", "success")
        return redirect(url_for("LoginView:index"))
