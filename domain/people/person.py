from dataclasses import dataclass
from domain.cashflow.cashflow_item import CashFlowItem

@dataclass
class Person:
    name: str
    income_sources: list[CashFlowItem]
    