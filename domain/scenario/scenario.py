from dataclasses import dataclass
from domain.people.person import Person
from domain.mortgage.mortgage import Mortgage
from domain.common.constants import MONTHS_IN_YEAR, PERCENTAGE

@dataclass
class Scenario:
    name: str
    persons: list[Person]
    expenses: list
    mortgage: Mortgage
    schedules: list

    def total_monthly_income(self) -> float:
        return sum(p.monthly_amount() for person in self.persons for p in person.income_sources)

    def total_annual_income(self) -> float:
        return self.total_monthly_income() * MONTHS_IN_YEAR

    def total_monthly_expenses(self) -> float:
        return sum(e.monthly_amount() for e in self.expenses)

    def total_annual_expenses(self) -> float:
        return self.total_monthly_expenses() * MONTHS_IN_YEAR

    def net_monthly_cash_flow(self) -> float:
        return self.total_monthly_income() - self.total_monthly_expenses()

    def net_annual_cash_flow(self) -> float:
        return self.net_monthly_cash_flow() * MONTHS_IN_YEAR

    def annual_income_of_person(self, person_name: str) -> float:
        for person in self.persons:
            if person.name == person_name:
                return sum(i.annual_amount() for i in person.income_sources)
        return 0.0
    
    def monthly_income_of_person(self, person_name: str) -> float:
        return self.annual_income_of_person(person_name) / MONTHS_IN_YEAR
    
    def annual_expenses_of_person(self, person_name: str) -> float:
        amount = 0.0
        for expense in self.expenses:
            for allocation in expense.allocations:
                if allocation.name == person_name:
                    amount += expense.annual_amount() * (allocation.percent / PERCENTAGE)
        return amount
    
    def monthly_expenses_of_person(self, person_name: str) -> float:
        return self.annual_expenses_of_person(person_name) / MONTHS_IN_YEAR
