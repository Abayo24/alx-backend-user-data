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
        return False

    def authorization_header(self, request=None) -> None:
        """
        authorize header
        """
        return None

    def current_user(self, request=None) -> None:
        """
        checks current user
        """
        return None


if __name__ == '__main__':
    """main"""
    a = Auth()

    print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
    print(a.authorization_header())
    print(a.current_user())
