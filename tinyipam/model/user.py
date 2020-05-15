#!/usr/bin/env python3
from .db import db
from sqlalchemy.sql import func
from flask_login import UserMixin


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String(16), unique=True, nullable=True)

    password = db.Column(db.String(255), unique=False, nullable=True)
    salt = db.Column(db.String(50), unique=False, nullable=True)

    created = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())
