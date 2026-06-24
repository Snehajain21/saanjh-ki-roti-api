from decimal import Decimal
from enum import Enum

from sqlmodel import SQLModel

from app.models.enums import (
    MealType,
    DietType,
    BillingCycle
)


class PlanCreate(SQLModel):
    name: str
    price: Decimal
    meal_type: MealType
    diet_types: list[DietType]
    billing_cycle: BillingCycle


class PlanRead(SQLModel):
    id: int
    name: str
    price: Decimal
    meal_type: MealType
    diet_types: list[DietType]
    billing_cycle: BillingCycle
    is_active: bool