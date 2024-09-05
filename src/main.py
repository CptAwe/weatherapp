from modules import weatherDBConn
from tables import users

from sqlalchemy import select

with weatherDBConn() as conn:
    weather_users = conn.scalar(select(users))
    
    print(weather_users)
    
