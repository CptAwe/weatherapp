from typing import Any
from sqlalchemy import select

from modules import weatherDBSession

class DbObjBase():
    
    # initialize the db session
    __sess = weatherDBSession
    
    def __init__(self) -> None:
        pass
    
    def fetch(self, db_obj, db_obj_attr, unique_identifier: Any):
        with self.__sess() as sess:
            tmp = sess.scalar(
                select(db_obj).where(
                    db_obj_attr == unique_identifier
                )
            )
            return tmp

    def __str__(self) -> str:
        """String representation of object"""
        attrs = {i:j for i,j in self.__dict__.items()}
        return f"{attrs}"