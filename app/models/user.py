from enum import Enum
from typing import Optional

from sqlmodel import SQLModel, Field


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    CUSTOMER = "CUSTOMER"


class User(SQLModel, table=True):
    id: int | None = Field(
        default=None,
        primary_key=True
    )

    name: str

    email: str = Field(
        unique=True,
        index=True
    )

    password_hash: str

    role: UserRole