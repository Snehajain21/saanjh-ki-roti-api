from sqlmodel import Session, select

from app.models.user import User
from app.schemas.user import UserCreate
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
        role=user_data.role
    )

    session.add(user)
    session.commit()
    session.refresh(user)

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