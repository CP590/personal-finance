from dataclasses import dataclass
from datetime import date
from domain.schedule.recurring_schedule import RecurringSchedule
from domain.schedule.oneoff_schedule import OneOffSchedule
from domain.schedule.schedule_type import ScheduleType
from domain.cashflow.oneoff_expense import OneOffExpense
from domain.common.frequency import Frequency

@dataclass
class ScheduleFactory:
    @staticmethod
    def create(data: dict) -> RecurringSchedule | OneOffExpense:
        match ScheduleType(data.get('type')):
            case ScheduleType.RECURRING:
                start_date = date.fromisoformat(data["start_date"])
                end_date = (
                    date.fromisoformat(data["end_date"])
                    if data.get("end_date")
                    else None
                )
                return RecurringSchedule(
                    source_id=data['source_id'],
                    frequency=Frequency(data['frequency']),
                    start_date=start_date,
                    end_date=end_date
                )
            case ScheduleType.ONE_OFF:
                execution_date = date.fromisoformat(data["date"])
                return OneOffSchedule(
                    source_id=data['source_id'],
                    execution_date=execution_date,
                )
            