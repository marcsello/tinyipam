#!/usr/bin/env python3
from .db import db
from sqlalchemy.sql import func
from .custom_types.ip import DBIPv4AddressStr, DBIPv6AddressStr


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)

    subnet_id = db.Column(db.Integer, db.ForeignKey("subnet.id"), nullable=False)
    subnet = db.relationship("Subnet", backref=db.backref("addresses", lazy=True))

    name = db.Column(db.String(50), nullable=False)

    ipv4 = db.Column(DBIPv4AddressStr, nullable=True, default=None)
    ipv6 = db.Column(DBIPv6AddressStr, nullable=True, default=None)

    created = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())
