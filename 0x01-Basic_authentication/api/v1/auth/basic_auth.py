#!/usr/bin/env python3
"""
Module for Basic authorization
"""
from auth import Auth
from typing import Optional
from base64 import b64decode


class BasicAuth(Auth):
    """
    class for Baic Authorization
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """
         returns the Base64 part of
         the Authorization header for a Basic Authentication
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
                                           ) -> str:
        """
        returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            encoded_base64 = b64decode(base64_authorization_header)
            decoded_base64 = encoded_base64.decode('utf-8')
        except (Exception):
            return
        return decoded_base64


if __name__ == "__main__":
    a = BasicAuth()

    print(a.decode_base64_authorization_header(None))
    print(a.decode_base64_authorization_header(89))
    print(a.decode_base64_authorization_header("Holberton School"))
    print(a.decode_base64_authorization_header("SG9sYmVydG9u"))
    print(a.decode_base64_authorization_header
          ("SG9sYmVydG9uIFNjaG9vbA==")
          )
    print(a.decode_base64_authorization_header
          (a.extract_base64_authorization_header
           ("Basic SG9sYmVydG9uIFNjaG9vbA==")
           )
          )
