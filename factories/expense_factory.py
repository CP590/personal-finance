from dataclasses import dataclass
from domain.mortgage.mortgage import Mortgage
from domain.cashflow.recurring_expense import RecurringExpense
from domain.cashflow.expense_allocation import ExpenseAllocation
from domain.cashflow.mortgage_expense import MortgageExpense
from domain.common.frequency import Frequency

@dataclass
class ExpenseFactory:
    @staticmethod
    def create(data: dict, mortgage: Mortgage = None) -> RecurringExpense:
        allocations = [
            ExpenseAllocation(
                name=a['name'],
                percent=a['percent']
            ) for a in data['allocations']
        ]

        match data.get('name'):
            case 'Mortgage':
                mortgage_expense: MortgageExpense = MortgageExpense(
                    id=data['id'],
                    name=data['name'],
                    amount_value=None,
                    frequency=Frequency(data['frequency']),
                    allocations=allocations,
                    mortgage=mortgage
                )
                mortgage_expense.amount_value = mortgage_expense.monthly_amount()
                return mortgage_expense
            case _:
                return RecurringExpense(
                    id=data['id'],
                    name=data['name'],
                    amount_value=data['amount'],
                    frequency=Frequency(data['frequency']),
                    allocations=allocations
        )
            