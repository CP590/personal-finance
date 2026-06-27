from dataclasses import dataclass
from datetime import date
from domain.schedule.schedule import Schedule

@dataclass
class OneOffSchedule(Schedule):
    source_id: str
    execution_date: date

    def occurs_in_month(self, current_date: date) -> bool:
        return self.indexes_equal(current_date, self.execution_date)
    