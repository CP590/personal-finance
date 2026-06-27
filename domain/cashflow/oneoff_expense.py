from dataclasses import dataclass
from domain.cashflow.cashflow_item import CashFlowItem
from domain.cashflow.expense_allocation import ExpenseAllocation

@dataclass
class OneOffExpense(CashFlowItem):
    amount_value: float
    allocations: list[ExpenseAllocation]

    def amount(self) -> float:
        return -self.amount_value
    