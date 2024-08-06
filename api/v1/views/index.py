#!/usr/bin/python3
"""api status
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', strict_slashes=False)
def api_status():
    """Returns the count of each object by type
    """

    response = {'status': 'OK'}
    return jsonify(response)


@app_views.route('/stats', strict_slashes=False)
def stuff():
    '''JSON Responses'''
    todos = {
        'states': 'State',
        'users': 'User',
        'amenities': 'Amenity',
        'cities': 'City',
        'places': 'Place',
        'reviews': 'Review'
    }
    for key in todos:
        todos[key] = storage.count(todos[key])
    return jsonify(todos)
