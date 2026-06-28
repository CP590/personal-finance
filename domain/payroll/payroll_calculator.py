from math import floor
from domain.cashflow.salary_income import SalaryIncome
from domain.payroll.payroll_result import PayrollResult
from domain.common.frequency import Frequency
from domain.tax.tax_type import TaxType
from domain.tax.income_tax_rules import INCOME_TAX_BANDS
from domain.tax.national_insurance_rules import NATIONAL_INSURANCE_BANDS
from domain.tax.student_loan_rules import PLAN_2_BAND

@staticmethod
def process(income: SalaryIncome) -> float:
    tax: float = 0

    for item in TaxType:
        tax += calculate_tax(income, item)

    return tax


@staticmethod
def calculate_tax(income: SalaryIncome, type: TaxType) -> float:
    tax: float = 0
    remaining: float = income.amount(Frequency.ANNUALLY)*0.95   #TODO: Salary sacrifice

    match type:
        case TaxType.INCOME_TAX:
            bands = INCOME_TAX_BANDS
        case TaxType.NATIONAL_INSURANCE:
            bands = NATIONAL_INSURANCE_BANDS
        case TaxType.STUDENT_LOAN:
            bands = [PLAN_2_BAND]
    
    for band in bands:
        if floor(income.amount(Frequency.ANNUALLY)*0.95) <= band.lower_threshold:
            break
        
        if type == TaxType.STUDENT_LOAN:
            taxable: float = income.amount(Frequency.ANNUALLY)*0.95 - band.lower_threshold
        else:
            taxable: float = min(remaining, band.upper_threshold - band.lower_threshold)
        
        if taxable > 0:
            tax += taxable * band.rate
            remaining -= taxable
        if remaining <= 0:
            break
        
    return tax

@staticmethod
def calculate_loan_repayment(income: SalaryIncome) -> float:
    tax: float = 0
    
    
    if taxable > 0:
        tax += taxable * PLAN_2_BAND.rate
    return tax