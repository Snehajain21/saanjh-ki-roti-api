from enum import Enum

from pydantic import EmailStr
from sqlmodel import SQLModel


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    CUSTOMER = "CUSTOMER"


class UserCreate(SQLModel):
    name: str
    email: EmailStr
    password: str


class UserRead(SQLModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole