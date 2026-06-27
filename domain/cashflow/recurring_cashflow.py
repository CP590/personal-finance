from dataclasses import dataclass
from domain.cashflow.cashflow_item import CashFlowItem
from domain.common.frequency import Frequency

@dataclass
class RecurringCashFlow(CashFlowItem):
    frequency: Frequency
    