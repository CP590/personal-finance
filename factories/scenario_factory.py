from dataclasses import dataclass
from domain.scenario.scenario import Scenario
from factories.person_factory import PersonFactory
from factories.mortgage_factory import MortgageFactory
from factories.expense_factory import ExpenseFactory
from factories.schedule_factory import ScheduleFactory
from factories.lookup import lookup


@dataclass
class ScenarioFactory:
    @staticmethod
    def create(data:dict) -> Scenario:
        persons = [
            PersonFactory.create(p) for p in data['persons']
        ]

        mortgage = MortgageFactory.create(data['mortgage'])

        expenses = []
        for e in data['expenses']:
            expense = ExpenseFactory.create(e, mortgage=mortgage)
            expenses.append(expense)
            lookup[expense.id] = expense

        schedules = [
            ScheduleFactory.create(s) for s in data['schedules']
        ]

        return Scenario(
            name=data['name'],
            persons=persons,
            expenses=expenses,
            mortgage=mortgage,
            schedules=schedules
        )
    