from dataclasses import dataclass
from domain.cashflow.salary_income import SalaryIncome
from domain.common.frequency import Frequency

@dataclass
class IncomeSourceFactory:
    @staticmethod
    def create(data: dict) -> SalaryIncome:
        if data['name'] == 'Job':
            return SalaryIncome(
                id=data['id'],
                name=data['name'],
                amount_value=data['amount'],
                frequency=Frequency(data['frequency']),
                pension_percent=data['pension_percent']
            )
        