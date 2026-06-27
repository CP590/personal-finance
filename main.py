import json
from datetime import date
from factories.scenario_factory import ScenarioFactory
from factories.lookup import lookup
from simulation.engine import SimulationEngine


with open('scenario.json') as f:
    data = json.load(f)

scenario = ScenarioFactory.create(data)
print(scenario.net_monthly_cash_flow())
print(lookup[scenario.schedules[0].source_id])
SimulationEngine.run(scenario, date(2026, 3, 1), 3)
