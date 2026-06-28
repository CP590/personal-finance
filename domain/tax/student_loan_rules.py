from domain.tax.student_loan_plan import StudentLoanPlan
from domain.tax.tax_band import TaxBand

PLAN_2_THRESHOLD: float = 29385
PLAN_2_RATE: float = 0.09

plan_2 = StudentLoanPlan(2, 29385, 0.09)

PLAN_2_BAND: TaxBand = TaxBand(plan_2.threshold, None, plan_2.rate)