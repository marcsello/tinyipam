#!/usr/bin/env python3
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow.validate import Regexp
from model import Domain


class DomainSchema(SQLAlchemyAutoSchema):
    tld = auto_field(validate=Regexp("^[a-z0-9.]*$"))

    class Meta:
        model = Domain
        load_instance = True
        dump_only = ["id", "created"]
