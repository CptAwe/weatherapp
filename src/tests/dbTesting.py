import unittest

from modules import weatherDBSession
from sqlalchemy import inspect

class DBtesting(unittest.TestCase):
    
    def test_connection(self):
        """
        Check connection by checking if the essential tables (`users`, `users_metadata`, `weather_data`) exist
        """
        assert inspect(weatherDBSession._engine).has_table("users")
        assert inspect(weatherDBSession._engine).has_table("users_metadata")
        assert inspect(weatherDBSession._engine).has_table("weather_data")
