from enum import Enum

class userRoles(Enum):
    """The roles of each user"""
    viewer = 'viewer'
    weather_station = 'weather_station'
    admin = 'admin'
