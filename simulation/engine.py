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
            print(f"MONTH: {i}")
            month_state: FinancialState = FinancialState()
            current_date = start_date + relativedelta(months=i)
            for schedule in scenario.schedules:
                if schedule.occurs_in_month(current_date):
                    print(f"schedule {schedule.source_id} occurs in current month")
                    source = lookup[schedule.source_id]
                    cashflow = source.monthly_amount()
                    print(f"cashflow for schedule: {cashflow}")
                    month_state.cash_balance += cashflow
            results.monthly_states.append(month_state)
        print(results.monthly_states)
        