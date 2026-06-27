from dataclasses import dataclass
from domain.common.constants import MONTHS_IN_YEAR

@dataclass
class Mortgage:
    principal: float
    interest_rate: float
    term_years: int

    def calculate_annual_payment(self)-> float:
        r = self.interest_rate / MONTHS_IN_YEAR
        n = self.term_years * MONTHS_IN_YEAR
        return MONTHS_IN_YEAR * self.principal * r * (1 + r) ** n / ((1 + r) ** n - 1)
    