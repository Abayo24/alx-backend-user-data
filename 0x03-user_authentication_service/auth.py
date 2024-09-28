#!/usr/bin/env python3
"""
Auth module for password hashing
"""
import bcrypt
from user import User
from db import DB
from typing import Optional
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt and
    returns the hashed password as bytes
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with an email and password"""
        identical_user = self._db.find_user_by(email=email)
        if identical_user:
            raise ValueError(f'User {email} already exists')
        hashed_password = _hash_password(password)
        new_user = self.db.add_user(email, hashed_password.decode('utf-8'))
        return new_user
