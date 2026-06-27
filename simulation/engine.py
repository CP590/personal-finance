from dataclasses import dataclass
from datetime import date
from dateutil.relativedelta import relativedelta
from domain.scenario.scenario import Scenario
from simulation.state import FinancialState
from simulation.results import SimulationResults
from factories.lookup import lookup

@dataclass
class SimulationEngine:
    @staticmethod
    def run(scenario: Scenario, start_date: date, months: int):
        results: SimulationEngine = SimulationResults()
        for i in range(months):
            current_date = start_date + relativedelta(months=i)
            print(f"MONTH: {current_date.strftime('%B')}")
            month_state: FinancialState = FinancialState()
            for schedule in scenario.schedules:
                if schedule.occurs_in_month(current_date):
                    source = lookup[schedule.source_id]
                    cashflow = source.amount(schedule.frequency)
                    month_state.cash_balance += cashflow
            print(f"cashflow for month: {month_state.cash_balance}")
            results.monthly_states.append(month_state)
        print(results.monthly_states)
        