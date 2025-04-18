from typing import List, Dict
from .communication_mode import CommunicationMode
from ..agents.agent_base import Agent

class MessagePool:
    def __init__(self):
        self.messages = []
        
    def add_message(self, sender: str, content: str):
        self.messages.append({"sender": sender, "content": content})
        
    def get_messages(self):
        return self.messages
        
    def clear(self):
        self.messages = []

class SharedMessagePoolMode(CommunicationMode):
    def __init__(self, agents: List[Agent]):
        super().__init__(agents)
        self.message_pool = MessagePool()
        
    def process_query(self, query: str) -> Dict[str, str]:
        responses = {}
        self.message_pool.clear()
        
        # Initial query added to pool
        self.message_pool.add_message("user", query)
        
        # Each agent processes all messages in pool
        for agent in self.agents:
            pool_content = self.message_pool.get_messages()
            response = agent.process_message(
                f"Message pool contains: {pool_content}. Original query: {query}"
            )
            self.message_pool.add_message(agent.name, response)
            responses[agent.name] = response
            
        return responses