from dataclasses import dataclass
from datetime import date
from domain.schedule.schedule import Schedule
from domain.common.frequency import Frequency

@dataclass
class RecurringSchedule(Schedule):
    source_id: str
    frequency: Frequency
    start_date: date
    end_date: date | None

    def occurs_in_month(self, current_date: date) -> bool:
        current_date_index = self.month_index(current_date)
        start_date_index = self.month_index(self.start_date)

        occurs: bool = False    #TODO cover null data for frequency
        match self.frequency:
            case Frequency.MONTHLY:
                occurs = current_date_index >= start_date_index   #Current month is or later than start month
            case Frequency.ANNUALLY:
                occurs = (current_date_index - start_date_index) % 12 == 0
        return occurs
