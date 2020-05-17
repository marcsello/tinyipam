#!/usr/bin/env python3
from marshmallow_sqlalchemy import ModelSchema
from model import Subnet


class SubnetSchema(ModelSchema):
    class Meta:
        model = Subnet
