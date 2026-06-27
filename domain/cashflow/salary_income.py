from dataclasses import dataclass
from domain.cashflow.recurring_cashflow import RecurringCashFlow
from domain.common.constants import MONTHS_IN_YEAR

@dataclass
class SalaryIncome(RecurringCashFlow):
    amount_value: float
    pension_percent: float

    def annual_amount(self) -> float:
        return self.amount_value * self.frequency.annual_factor()

    def monthly_amount(self) -> float:
        return self.annual_amount() / MONTHS_IN_YEAR
    