from dataclasses import dataclass

@dataclass
class StudentLoanPlan:
    plan_number: int
    threshold: float
    rate: float