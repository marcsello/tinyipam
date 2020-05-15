#!/usr/bin/env python3
from .db import db
from sqlalchemy.sql import func


class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    tld = db.Column(db.String(1024), unique=True, nullable=False)

    active = db.Column(db.Boolean, nullable=False, default=False)

    created = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())
