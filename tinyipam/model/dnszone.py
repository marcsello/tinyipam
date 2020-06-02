#!/usr/bin/env python3
from .db import db
from sqlalchemy.sql import func


class DNSZone(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    tld = db.Column(db.String(1024), unique=True, nullable=False)

    active = db.Column(db.Boolean, nullable=False, default=False)

    rname = db.Column(db.String(1024), default="hostmaster.local.")

    default_ttl = db.Column(db.Integer, default=86400)
    serial = db.Column(db.Integer, default=1)
    refresh = db.Column(db.Integer, default=28800)
    retry = db.Column(db.Integer, default=7200)
    expire = db.Column(db.Integer, default=2419200)
    min_ttl = db.Column(db.Integer, default=86400)

    created = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())
