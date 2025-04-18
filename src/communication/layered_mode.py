from .communication_mode import CommunicationMode  # Ensure relative import
from typing import List, Dict

class LayeredMode(CommunicationMode):
    def process_query(self, query: str) -> Dict[str, str]:
        responses = {}
        previous_layer_response = query
        
        # Process through layers (agents are assumed to be ordered by layer)
        for agent in self.agents:
            # Each agent receives combined knowledge from previous layer
            response = agent.process_message(f"Previous layer said: {previous_layer_response}. {query}")
            responses[agent.name] = response
            previous_layer_response = response
            
        return responses