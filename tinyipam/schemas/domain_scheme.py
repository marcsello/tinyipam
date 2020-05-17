#!/usr/bin/env python3
from marshmallow_sqlalchemy import ModelSchema
from model import Domain


class DomainSchema(ModelSchema):
    class Meta:
        model = Domain
