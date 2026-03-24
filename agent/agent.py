
'''from agent.perception import perceive_data
from agent.reasoning import reason_patterns

class AirQualityAgent:
    def run(self, path):
        data = perceive_data(path)
        return reason_patterns(data)
'''

from agent.perception import perceive_data
from agent.reasoning import reason_patterns

class AirQualityAgent:

    def run(self, path="data/AirQualityUCI.xlsx"):
        data = perceive_data(path)
        processed = reason_patterns(data)
        return processed