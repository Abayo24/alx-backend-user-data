#!/usr/bin/env python3
"""
Module for SSession Authorization handling.
This module provides methods to decode Base64 credentials
and extract user information for basic HTTP authentication.
"""
from api.v1.auth.auth import Auth
from models.user import User
from base64 import b64decode
from typing import TypeVar


class SessionAuth(Auth):
    """
    BasicAuth class that implements methods for handling
    Basic Authentication through Base64-encoded credentials.
    """
    pass
