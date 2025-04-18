from .agent_base import Agent

class SpecificAgent1(Agent):
    def __init__(self, message_pool, chatgpt_api):  # Add chatgpt_api parameter
        super().__init__("SpecificAgent1")  # Pass a default name or modify Agent base
        self.message_pool = message_pool
        self.chatgpt_api = chatgpt_api  # Store the API instance

    def process_message(self, message):
        # Formulate a prompt for the LLM based on the agent's role/persona
        # Example: Define a simple persona
        prompt = f"As Agent 1, you prefer simple and direct answers. You received the message: '{message}'. How do you respond?"
        print(f"Agent {self.name}: Sending prompt to LLM: '{prompt[:50]}...'")  # Log prompt start

        # Call the ChatGPT API
        response = self.chatgpt_api.get_completion(prompt)
        print(f"Agent {self.name}: Received response from LLM.")

        # Optionally add the response to the message pool if needed by the communication mode
        # self.message_pool.add_message(self.name, response)

        return response

    def update_response(self, previous_responses):
        # Implement logic to update response based on previous responses
        updated_response = f"SpecificAgent1 updated response based on: {previous_responses}"
        return updated_response