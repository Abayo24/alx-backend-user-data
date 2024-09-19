#!/usr/bin/env python3
"""
class to manage the API authentication.
"""
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

    def current_user(self, request=None) -> None:
        """
        checks current user
        """
        return None


if __name__ == '__main__':
    """main"""
    a = Auth()

    print(a.require_auth(None, None))
    print(a.require_auth(None, []))
    print(a.require_auth("/api/v1/status/", []))
    print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
    print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))
    print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))
    print(a.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))
