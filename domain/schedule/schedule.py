from dataclasses import dataclass
from abc import ABC
from datetime import date

@dataclass
class Schedule(ABC):
    def occurs_in_month(current_date: date):
        pass

    @staticmethod
    def month_index(date: date) -> int:
        return date.year * 12 + date.month
    
    def indexes_equal(self, current_date: date, date: date) -> bool:
        current_date_index = self.month_index(current_date)
        date_index = self.month_index(date)
        return current_date_index == date_index ## Occurs this month
    