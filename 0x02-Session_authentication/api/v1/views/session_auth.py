#!/usr/bin/env python3
"""
Session Authentication views
"""
from os import getenv
from flask import abort, jsonify, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """returns loggedin user"""
    from api.v1.app import auth
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({"email": email})
    except Exception:
        return jsonify({'error': 'no user found for this email'}), 404
    if not users:
        return jsonify({'error': 'no user found for this email'}), 404

    for user in users:
        found_user_bool = user.is_valid_password(password)
        if user.is_valid_password(password):
            found_user = user
        if not found_user_bool:
            return jsonify({'error': 'wrong password'}), 401

        session_id = auth.create_session(found_user.id)
        session_name = getenv('SESSION_NAME')

        response = jsonify(found_user.to_json())

        response.set_cookie(session_name, session_id)

        return response
