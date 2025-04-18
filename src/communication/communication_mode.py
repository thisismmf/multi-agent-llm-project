from abc import ABC, abstractmethod
from typing import List, Dict
from ..agents.agent_base import Agent  # Changed to relative import

class CommunicationMode(ABC):
    def __init__(self, agents: List[Agent]):
        self.agents = agents

    @abstractmethod
    def process_query(self, query: str) -> Dict[str, str]:
        """Process a query and return responses from agents"""
        pass
