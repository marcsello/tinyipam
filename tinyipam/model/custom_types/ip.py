#!/usr/bin/env python3
from sqlalchemy import types
from sqlalchemy.types import TypeDecorator
from ipaddress import IPv4Network, IPv6Network

# TODO: Use postgres native types if available

class DBIPv4SubnetStr(TypeDecorator):
    impl = types.Unicode(18)

    def __init__(self, *args, **kwargs):
        super(DBIPv4SubnetStr, self).__init__(*args, **kwargs)
        self.impl = types.Unicode(18)

    def process_literal_param(self, value, dialect):
        return str(value) if value else None

    def process_bind_param(self, value, dialect):
        return str(value) if value else None

    def process_result_value(self, value, dialect):
        return IPv4Network(value) if value else None

    @property
    def python_type(self):
        return self.impl.type.python_type


class DBIPv6SubnetStr(TypeDecorator):
    impl = types.Unicode(18)

    def __init__(self, *args, **kwargs):
        super(DBIPv6SubnetStr, self).__init__(*args, **kwargs)
        self.impl = types.Unicode(18)

    def process_literal_param(self, value, dialect):
        return str(value) if value else None

    def process_bind_param(self, value, dialect):
        return str(value) if value else None

    def process_result_value(self, value, dialect):
        return IPv6Network(value) if value else None

    @property
    def python_type(self):
        return self.impl.type.python_type