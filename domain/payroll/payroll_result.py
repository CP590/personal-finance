from dataclasses import dataclass

@dataclass
class PayrollResult():
    gross_pay: float
    net_pay: float

    income_tax: float
    national_insurance: float
    employee_pension: float
    employer_pension: float
    