from typing import Any
from sqlalchemy import select

from modules import weatherDBSession
from tables import users

from .userRoles import userRoles
from .DBObjectBase import DbObjBase

class User(DbObjBase):
    
    def __init__(self, username: str) -> None:
        """Initialize the user object"""
        self.username: str = username
        
        # Some attributes are populated by the DB
        self.id: str = None
        self.uuid: str = None
        
        # Some attributes have to be fetched by the DB
        self.role: userRoles = None
        super().__init__()
    
    def fetch(self):
        """In place fetching of the user attributes"""
        
        user = super().fetch(
            users,
            users.username,
            self.username
        )
        
        self.username = user.username
        self.uuid = user.uuid
        self.id = user.id
        self.role = userRoles[user.access]
    
    def create(self):
        """In place creation of user"""
        pass
        