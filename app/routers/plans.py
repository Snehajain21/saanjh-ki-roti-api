from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database import get_session
from app.dependencies import require_admin
from app.models.user import User
from app.schemas.plan import PlanCreate, PlanRead
from app.services.plan_service import (
    create_plan,
    get_all_plans
)

router = APIRouter(
    prefix="/plans",
    tags=["Plans"]
)


@router.get(
    "/",
    response_model=list[PlanRead]
)
def get_plans(
    session: Annotated[
        Session,
        Depends(get_session)
    ]
):
    return get_all_plans(session)


@router.post(
    "/",
    response_model=PlanRead,
    status_code=201
)
def create_new_plan(
    plan_data: PlanCreate,
    session: Annotated[
        Session,
        Depends(get_session)
    ],
    current_user: Annotated[
        User,
        Depends(require_admin)
    ]
):
    return create_plan(
        plan_data,
        session
    )