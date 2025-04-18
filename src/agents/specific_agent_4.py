from .agent_base import Agent

class SpecificAgent4(Agent):
    def __init__(self, message_pool, chatgpt_api):
        super().__init__("SpecificAgent4")
        self.message_pool = message_pool
        self.chatgpt_api = chatgpt_api

    def process_message(self, message):
        prompt = f"As Agent 4, you are creative and think outside the box. You received the message: '{message}'. Give an innovative perspective."
        print(f"Agent {self.name}: Sending prompt to LLM: '{prompt[:50]}...'")
        
        response = self.chatgpt_api.get_completion(prompt, agent_name="SpecificAgent4")
        print(f"Agent {self.name}: Received response from LLM.")
        
        return response
