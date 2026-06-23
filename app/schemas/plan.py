from enum import Enum

from sqlmodel import SQLModel


class MealType(str, Enum):
    LUNCH = "LUNCH"
    LUNCH_AND_DINNER = "LUNCH_AND_DINNER"


class DietType(str, Enum):
    VEG = "VEG"
    NON_VEG = "NON_VEG"


class BillingCycle(str, Enum):
    MONTHLY = "MONTHLY"


class PlanCreate(SQLModel):
    name: str
    price: float
    meal_type: MealType
    diet_type: DietType
    billing_cycle: BillingCycle


class PlanRead(SQLModel):
    id: int
    name: str
    price: float
    meal_type: MealType
    diet_type: DietType
    billing_cycle: BillingCycle
    is_active: bool