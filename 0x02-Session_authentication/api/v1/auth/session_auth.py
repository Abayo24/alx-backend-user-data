#!/usr/bin/env python3
"""
Module for SSession Authorization handling.
This module provides methods to decode Base64 credentials
and extract user information for basic HTTP authentication.
"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User
from base64 import b64decode
from typing import TypeVar


class SessionAuth(Auth):
    """
    BasicAuth class that implements methods for handling
    Basic Authentication through Base64-encoded credentials.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if not session_id or not isinstance(session_id, str):
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id
