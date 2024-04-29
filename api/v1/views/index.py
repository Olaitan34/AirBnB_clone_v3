#!/usr/bin/python3
""" Module containing views """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status", methods=["GET"],  strict_slashes=False)
def status():
    """ returns a JSON """
    data = {"status": "OK"}
    
    resp = jsonify(data)
    resp.status_code = 200

    return resp


@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def stats():
    """ retrieves the number of each objects by type """
    data = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }

    resp = jsonify(data)
    resp.status_code = 200

    return resp