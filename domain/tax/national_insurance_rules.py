from domain.tax.tax_band import TaxBand
from domain.common.constants import MONTHS_IN_YEAR

PRIMARY_THRESHOLD: float = 1048 * MONTHS_IN_YEAR
UPPER_EARNINGS_LIMIT: float = 4189 * MONTHS_IN_YEAR

NATIONAL_INSURANCE_BANDS = [
    TaxBand(0, PRIMARY_THRESHOLD, 0),
    TaxBand(PRIMARY_THRESHOLD, UPPER_EARNINGS_LIMIT, 0.08),
    TaxBand(UPPER_EARNINGS_LIMIT, float("inf"), 0.02)
]