from dataclasses import dataclass

@dataclass
class ExpenseAllocation:
    name: str
    percent: float
    