from dataclasses import dataclass
from domain.people.person import Person
from factories.income_source_factory import IncomeSourceFactory
from factories.lookup import lookup

@dataclass
class PersonFactory:
    @staticmethod
    def create(data: dict) -> Person:
        ##incomes = [
         ##   IncomeSourceFactory.create(i) for i in data['income_sources']
        ##]

        incomes = []
        for i in data['income_sources']:
            income = IncomeSourceFactory.create(i)
            incomes.append(income)
            lookup[income.id] = income

        return Person(
            name=data['name'],
            income_sources=incomes
        )
    