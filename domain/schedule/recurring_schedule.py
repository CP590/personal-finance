from dataclasses import dataclass
from datetime import date
from domain.schedule.schedule import Schedule

@dataclass
class RecurringSchedule(Schedule):
    source_id: str
    start_date: date
    end_date: date | None

    def occurs_in_month(self, current_date: date) -> bool:
        current_date_index = self.month_index(current_date)
        start_date_index = self.month_index(self.start_date)
        return current_date_index >= start_date_index   #Current month is or later than start month
#TODO: Figure out how to deal with yearly payments (modulo)
