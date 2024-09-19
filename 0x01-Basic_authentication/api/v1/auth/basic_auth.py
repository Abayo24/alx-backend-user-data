#!/usr/bin/env python3
"""
Module for Basic Authorization handling.
This module provides methods to decode Base64 credentials
and extract user information for basic HTTP authentication.
"""
from auth import Auth
from typing import Optional, Tuple
from base64 import b64decode


class BasicAuth(Auth):
    """
    BasicAuth class that implements methods for handling
    Basic Authentication through Base64-encoded credentials.
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: Optional[str]
                                            ) -> Optional[str]:
        """
        Extracts the Base64 part of the Authorization header.

        Args:
            authorization_header (str): The full authorization header string.

        Returns:
            str: The Base64-encoded part of the Authorization header.
            None: If the authorization header is invalid or None.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> Optional[str]:
        """
        Decodes the Base64 part of the Authorization header.

        Args:
            base64_authorization_header (str): The Base64 string to decode.

        Returns:
            str: Decoded string if Base64 is valid.
            None: If the string is invalid or cannot be decoded.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            encoded_base64 = b64decode(base64_authorization_header)
            decoded_base64 = encoded_base64.decode('utf-8')
        except (Exception):
            return None
        return decoded_base64

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> Tuple[Optional[str], Optional[str]]:
        """
        Extracts the user email and password from the Base64 decoded value.

        Args:
            decoded_base64_authorization_header (str):
            The decoded Base64 string.

        Returns:
            tuple: A tuple containing the user email and password.
            None, None: If the decoded string is invalid or not in
            the expected format.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        user, pwd = decoded_base64_authorization_header.split(":")
        return user, pwd


if __name__ == "__main__":
    """main"""
    a = BasicAuth()

    print(a.extract_user_credentials(None))
    print(a.extract_user_credentials(89))
    print(a.extract_user_credentials("Holberton School"))
    print(a.extract_user_credentials("Holberton:School"))
    print(a.extract_user_credentials("bob@gmail.com:toto1234"))
