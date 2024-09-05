from typing import List, Literal, get_args
from sqlalchemy.orm import (
    Mapped, mapped_column, relationship
)
from sqlalchemy import (
    String, Enum
)

from modules import weatherDBTableBase

userRoles = Literal[
    "viewer", "weather_station", "admin"
]

class users(weatherDBTableBase):
    
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key = True)
    uuid: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column("passwrd",String(255), nullable = True)
    access: Mapped[Enum] = mapped_column(
        Enum(
            *get_args(userRoles),
            name = "access",
            create_constraint = True,
            validate_strings = True
        ),
        )

    # users_metadata: Mapped[List["users_metadata"]] = relationship(back_populates="metadata")
    # weather_data: Mapped[List["weather_data"]] = relationship(back_populates="weather_data")
    
    def __str__(self) -> str:
        return f"users(id={self.id}, uuid={self.uuid}, username={self.username}, access={self.access})"
    
    def __repr__(self) -> str:
        return super().__repr__()