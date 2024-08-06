#!/usr/bin/python3
"""
Initialize the Blueprint for the API views.

This blueprint is prefixed with '/api/v1' and will include
all the routes defined in the 'index' module within 'api.v1.views'.
"""

from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


from api.v1.views.index import *