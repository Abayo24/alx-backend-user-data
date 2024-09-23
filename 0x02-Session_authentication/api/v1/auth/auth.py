#!/usr/bin/env python3
"""
class to manage the API authentication.
"""
from os import getenv
from flask import request
from typing import List, TypeVar


class Auth:
    """
    class to manage the API authentication.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        checks if authentication is required
        """
        if path and not path.endswith('/'):
            path = path + '/'
        for excluded_path in excluded_paths:
            if path.startswith(excluded_path.split('*')[0]):
                return False
        if excluded_paths is None or excluded_paths == []:
            return True
        if path not in excluded_paths or path is None:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """
        validate all requests to secure the API
        """
        key = 'Authorization'

        if request is None or key not in request.headers:
            return None
        return request.headers.get(key)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        checks current user
        """
        return None

    def session_cookie(self, request=None):
        """ returns a cookie value from a request"""
        if not request:
            return None
        session_name = getenv('SESSION_NAME')
        cookie = request.cookies.get(session_name)
        return cookie
