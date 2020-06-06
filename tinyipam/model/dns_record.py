#!/usr/bin/env python3
from .db import db
from sqlalchemy.sql import func
import enum


@enum.unique
class RecordType(enum.Enum):
    A = 0
    NS = 2
    CNAME = 5
    SOA = 6  # Autogenerated, kept here for consistency
    PTR = 12  # Probably Autogenerated, kept here for consistency
    TXT = 16
    MX = 15
    AAAA = 28


class DNSRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String(1024), unique=True, nullable=False)

    type = db.Column(db.Enum(RecordType), unique=False, nullable=False)

    # For A, AAAA and PTR records, it's supposedly automatically generated
    value = db.Column(db.String(1024), unique=False, nullable=True)

    address_id = db.Column(db.Integer, db.ForeignKey("address.id"), nullable=True)
    address = db.relationship("Address", backref=db.backref("records", lazy=True))

    zone_id = db.Column(db.Integer, db.ForeignKey("dns_zone.id"), nullable=False)
    zone = db.relationship("DNSZone", backref=db.backref("records", lazy=True))

    created = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())
