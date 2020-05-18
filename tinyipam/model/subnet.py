#!/usr/bin/env python3
from .db import db
from sqlalchemy.sql import func
from .custom_types.ip import DBIPv4SubnetStr, DBIPv6SubnetStr


class Subnet(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)

    name = db.Column(db.String(50), nullable=False)

    ipv4 = db.Column(DBIPv4SubnetStr, nullable=True, default=None)
    ipv6 = db.Column(DBIPv6SubnetStr, nullable=True, default=None)

    active = db.Column(db.Boolean, nullable=False, default=False)

    created = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())
