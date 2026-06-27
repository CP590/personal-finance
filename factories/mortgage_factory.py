from dataclasses import dataclass
from domain.mortgage.mortgage import Mortgage

@dataclass
class MortgageFactory:
    @staticmethod
    def create(data: dict) -> Mortgage:
        return Mortgage(
            principal=data['principal'],
            interest_rate=data['interest_rate'],
            term_years=data['term_years']
        )
    