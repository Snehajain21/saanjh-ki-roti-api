from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from app.database import get_session
from app.schemas.user import UserCreate, UserRead
from app.schemas.auth import Token
from app.services.auth_service import (
    register_user,
    authenticate_user
)
from app.services.auth_service import (
    register_user,
    login_user
)
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)
@router.post(
    "/register",
    response_model=UserRead,
    status_code=201
)
def register(
    user_data: UserCreate,
    session: Annotated[Session, Depends(get_session)]
):
    return register_user(
        user_data,
        session
    )
@router.post(
    "/login",
    response_model=Token
)
def login(
    form_data: Annotated[
        OAuth2PasswordRequestForm,
        Depends()
    ],
    session: Annotated[
        Session,
        Depends(get_session)
    ]
):

    return login_user(
    form_data.username,
    form_data.password,
    session
)