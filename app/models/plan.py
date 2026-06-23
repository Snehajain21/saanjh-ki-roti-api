from enum import Enum

from sqlmodel import SQLModel, Field


class MealType(str, Enum):
    LUNCH = "LUNCH"
    LUNCH_AND_DINNER = "LUNCH_AND_DINNER"


class DietType(str, Enum):
    VEG = "VEG"
    NON_VEG = "NON_VEG"


class BillingCycle(str, Enum):
    MONTHLY = "MONTHLY"


class Plan(SQLModel, table=True):
    id: int | None = Field(
        default=None,
        primary_key=True
    )

    name: str = Field(
        index=True
    )

    price: float

    meal_type: MealType

    diet_type: DietType

    billing_cycle: BillingCycle

    is_active: bool = True