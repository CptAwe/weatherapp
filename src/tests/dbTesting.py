import unittest

from modules import weatherDBConn
from sqlalchemy import inspect

class DBtesting(unittest.TestCase):
    
    def test_connection(self):
        """
        Check connection by checking if the essential tables (`users`, `users_metadata`, `weather_data`) exist
        """
        assert inspect(weatherDBConn._engine).has_table("users")
        assert inspect(weatherDBConn._engine).has_table("users_metadata")
        assert inspect(weatherDBConn._engine).has_table("weather_data")
