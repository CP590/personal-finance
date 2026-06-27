from dataclasses import dataclass
from domain.cashflow.recurring_cashflow import RecurringCashFlow
from domain.cashflow.expense_allocation import ExpenseAllocation
from domain.common.constants import MONTHS_IN_YEAR

@dataclass
class RecurringExpense(RecurringCashFlow):
    amount_value: float
    allocations: list[ExpenseAllocation]

    def annual_amount(self) -> float:
        return -self.amount_value * self.frequency.annual_factor()

    def monthly_amount(self) -> float:
        return self.annual_amount() / MONTHS_IN_YEAR
    