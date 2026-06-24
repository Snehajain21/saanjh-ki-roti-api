from sqlmodel import Session, select

from app.models.user import User, UserRole
from app.schemas.user import UserCreate
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from app.schemas.auth import Token
from app.core.security import create_access_token
from app.core.security import (
    hash_password,
    verify_password,
)


def register_user(
    user_data: UserCreate,
    session: Session
) -> User:

    hashed_password = hash_password(
        user_data.password
    )

    user = User(
        name=user_data.name,
        email=user_data.email,
        password_hash=hashed_password,
        role=UserRole.CUSTOMER
    )

    session.add(user)

    try:
        session.commit()
        session.refresh(user)

    except IntegrityError:
        session.rollback()

        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    return user


def authenticate_user(
    email: str,
    password: str,
    session: Session
):

    statement = select(User).where(
        User.email == email
    )

    user = session.exec(statement).first()

    if user is None:
        return None

    if not verify_password(
        password,
        user.password_hash
    ):
        return None

    return user

def login_user(
    username: str,
    password: str,
    session: Session
) -> Token:

    user = authenticate_user(
        username,
        password,
        session
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        user.id,
        user.role
    )

    return Token(
        access_token=access_token,
        token_type="bearer"
    )