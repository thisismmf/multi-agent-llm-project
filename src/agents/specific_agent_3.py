from .agent_base import Agent

class SpecificAgent3(Agent):
    def __init__(self, message_pool, chatgpt_api):
        super().__init__("SpecificAgent3")
        self.message_pool = message_pool
        self.chatgpt_api = chatgpt_api

    def process_message(self, message):
        prompt = f"As Agent 3, you are analytical and focus on pros and cons. You received the message: '{message}'. Evaluate the options and respond."
        print(f"Agent {self.name}: Sending prompt to LLM: '{prompt[:50]}...'")
        
        response = self.chatgpt_api.get_completion(prompt, agent_name="SpecificAgent3")
        print(f"Agent {self.name}: Received response from LLM.")
        
        return response
