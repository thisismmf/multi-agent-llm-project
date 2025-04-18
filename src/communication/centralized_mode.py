from .communication_mode import CommunicationMode  # Ensure relative import
from typing import List, Dict

class CentralizedMode(CommunicationMode):
    def __init__(self, agents):
        self.agents = agents
        self.message_pool = []

    def send_message(self, message):
        self.message_pool.append(message)
        for agent in self.agents:
            agent.receive_message(message)

    def receive_responses(self):
        responses = {}
        for agent in self.agents:
            response = agent.process_response()
            responses[agent.__class__.__name__] = response
        return responses

    def run(self):
        while self.message_pool:
            current_message = self.message_pool.pop(0)
            self.send_message(current_message)
            responses = self.receive_responses()
            self.handle_responses(responses)

    def handle_responses(self, responses):
        for agent_name, response in responses.items():
            print(f"{agent_name} responded: {response}")

    def process_query(self, query: str) -> Dict[str, str]:
        responses = {}
        coordinator = self.agents[0]  # First agent acts as coordinator
        
        # Coordinator processes query first
        coordinator_response = coordinator.process_message(query)
        responses[coordinator.name] = coordinator_response
        
        # Other agents receive coordinator's processed query
        for agent in self.agents[1:]:
            response = agent.process_message(f"Coordinator said: {coordinator_response}. Original query: {query}")
            responses[agent.name] = response
            
        return responses