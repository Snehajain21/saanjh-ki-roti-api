from decimal import Decimal
from enum import Enum

from sqlmodel import SQLModel, Field


from app.models.enums import (
    MealType,
    DietType,
    BillingCycle
)


class Plan(SQLModel, table=True):
    id: int | None = Field(
        default=None,
        primary_key=True
    )

    name: str = Field(
        index=True
    )

    price: Decimal

    meal_type: MealType

    diet_types: list[DietType]

    billing_cycle: BillingCycle

    is_active: bool = True