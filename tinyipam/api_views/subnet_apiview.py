#!/usr/bin/env python3
from flask import request, abort, jsonify
from flask_classful import FlaskView
from utils import json_required, apikey_required

from model import db


class SubnetAPIView(FlaskView):

    route_base = 'subnet'

    decorators = [apikey_required]

    def index(self):
        return jsonify({"hello" : "world"})

    @json_required
    def post(self):
        return jsonify({"hello" : "world"})

