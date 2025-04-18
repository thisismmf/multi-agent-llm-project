from .communication_mode import CommunicationMode  # Ensure relative import
from typing import List, Dict

class DecentralizedMode(CommunicationMode):
    def process_query(self, query: str) -> Dict[str, str]:
        responses = {}
        all_responses = []
        
        # First round: each agent processes independently
        for agent in self.agents:
            response = agent.process_message(query)
            responses[agent.name] = response
            all_responses.append(response)
            
        # Second round: each agent can see others' responses
        for agent in self.agents:
            updated_response = agent.process_message(
                f"Others said: {all_responses}. Original query: {query}"
            )
            responses[f"{agent.name}_updated"] = updated_response
            
        return responses
