from enum import Enum


class MealType(str, Enum):
    LUNCH = "LUNCH"
    LUNCH_AND_DINNER = "LUNCH_AND_DINNER"


class DietType(str, Enum):
    VEG = "VEG"
    NON_VEG = "NON_VEG"
    JAIN = "JAIN"
    DIABETIC = "DIABETIC"


class BillingCycle(str, Enum):
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"