#!/usr/bin/env python3
"""index.py"""

from flask import Blueprint, abort

app_views = Blueprint('app_views', __name__)

@app_views.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    """abort unauthorized"""
    abort(401)
