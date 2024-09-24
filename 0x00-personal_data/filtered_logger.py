#!/usr/bin/env python3
"""Regex-ing"""
import re
from typing import List, Tuple
import logging


"""PIIs"""
PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:  # noqa
    """returns the log message obfuscated"""
    return re.sub(f'({"|".join(fields)})=[^{separator}]*', lambda m: f'{m.group(1)}={redaction}', message)  # noqa


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initializes fields to filter"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """formats logs, filtering sensitive info"""
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, message, self.SEPARATOR)  # noqa


def get_logger() -> logging.Logger:
    """returns a logger object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(stream_handler)
    return logger
