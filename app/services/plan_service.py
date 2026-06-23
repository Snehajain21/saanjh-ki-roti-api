from sqlmodel import Session, select

from app.models.plan import Plan
from app.schemas.plan import PlanCreate


def create_plan(
    plan_data: PlanCreate,
    session: Session
) -> Plan:

    plan = Plan(
        name=plan_data.name,
        price=plan_data.price,
        meal_type=plan_data.meal_type,
        diet_type=plan_data.diet_type,
        billing_cycle=plan_data.billing_cycle
    )

    session.add(plan)
    session.commit()
    session.refresh(plan)

    return plan


def get_all_plans(
    session: Session
) -> list[Plan]:

    statement = select(Plan)

    plans = session.exec(
        statement
    ).all()

    return plans