from dataclasses import dataclass
from domain.cashflow.recurring_expense import RecurringExpense
from domain.mortgage.mortgage import Mortgage
from domain.common.constants import MONTHS_IN_YEAR

@dataclass
class MortgageExpense(RecurringExpense):
    mortgage: Mortgage

    def annual_amount(self) -> float:
        return -self.mortgage.calculate_annual_payment()
    
    def monthly_amount(self) -> float:
        return self.annual_amount() / MONTHS_IN_YEAR
    