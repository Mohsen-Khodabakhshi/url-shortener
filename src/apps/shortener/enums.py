from enum import Enum


class ExpirationTimeMonthEnum(int, Enum):
    three_months: int = 3
    six_months: int = 6
    twelve_months: int = 12
