#!/usr/bin/env python3
from ipaddress import IPv4Network, IPv6Network, AddressValueError
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import validates_schema, fields
from marshmallow.exceptions import ValidationError
from model import Subnet


def validate_ipv4(test: str):
    if len(test) > 0:
        try:
            IPv4Network(test)
        except AddressValueError as e:
            raise ValidationError(str(e))


def validate_ipv6(test: str):
    if len(test) > 0:
        try:
            IPv6Network(test)
        except AddressValueError as e:
            raise ValidationError(str(e))


class SubnetSchema(SQLAlchemyAutoSchema):
    ipv4 = auto_field(validate=validate_ipv4, required=False)
    ipv6 = auto_field(validate=validate_ipv6, required=False)

    @validates_schema
    def validate_at_least_one_provided(self, data, **kwargs):
        if (not data['ipv4']) and (not data['ipv6']):
            raise ValidationError("At least one IP subnet version must be provided")

    class Meta:
        model = Subnet
        load_instance = True
