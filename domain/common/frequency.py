from enum import Enum

class Frequency(Enum):
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    QUARTERLY = 'quarterly'
    ANNUALLY = 'annually'

    def annual_factor(self) -> float:
        if self == Frequency.WEEKLY:
            return 52
        elif self == Frequency.MONTHLY:
            return 12
        elif self == Frequency.QUARTERLY:
            return 4
        elif self == Frequency.ANNUALLY:
            return 1
        