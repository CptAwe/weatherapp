"""Custom Database Exceptions"""
from loguru import logger

class NoObjectinDbException(Exception):
    """Object not in database"""
    def __init__(self, *args: object) -> None:
        logger.error(f"Couldn't fetch object of type {args[0]} from database")
        logger.debug(f"Condition: {args[1]} == {args[2]}")
        super().__init__(f"Couldn't fetch object of type {args[0]} from database")
