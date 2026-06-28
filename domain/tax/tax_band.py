from dataclasses import dataclass
from typing import Optional

@dataclass
class TaxBand:
    lower_threshold: float
    upper_threshold: float | None
    rate: float