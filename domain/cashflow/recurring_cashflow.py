from dataclasses import dataclass
from domain.cashflow.cashflow_item import CashFlowItem
from domain.common.frequency import Frequency

@dataclass
class RecurringCashFlow(CashFlowItem):
    frequency: Frequency

    def amount(self, schedule_frequency: Frequency) -> float:
        match schedule_frequency:
            case Frequency.MONTHLY:
                return self.monthly_amount()
            case Frequency.ANNUALLY:
                return self.annual_amount()
    