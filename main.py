import json
from datetime import date
from factories.scenario_factory import ScenarioFactory
from factories.lookup import lookup
from simulation.engine import SimulationEngine
from domain.payroll.payroll_calculator import process
from domain.tax.tax_type import TaxType

with open('scenario.json') as f:
    data = json.load(f)

scenario = ScenarioFactory.create(data)
print(scenario.net_monthly_cash_flow()) #outdated, assumed all incomes and expenses are monthly
print(lookup[scenario.schedules[0].source_id])
SimulationEngine.run(scenario, date(2026, 3, 1), 8)
tax = process(scenario.persons[0].income_sources[0])
print(tax)