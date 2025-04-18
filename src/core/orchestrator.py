from typing import Dict, List
from ..communication.message_pool import MessagePool

class Orchestrator:
    def __init__(self, layered_mode, centralized_mode, decentralized_mode, shared_pool_mode):
        self.modes = {
            "layered": layered_mode,
            "centralized": centralized_mode,
            "decentralized": decentralized_mode,
            "shared_pool": shared_pool_mode
        }
        self.message_pool = MessagePool()  # Initialize message pool

    def process_query(self, query: str) -> Dict[str, Dict[str, str]]:
        results = {}
        
        # Process query through each communication mode
        for mode_name, mode in self.modes.items():
            print(f"\nProcessing with {mode_name} mode...")
            results[mode_name] = mode.process_query(query)
            
        return results

    def start(self, questions): # Accept questions list
        print("Orchestrator started.")
        all_results = {}

        # Example: Use layered_mode for processing
        # You might want to add logic here to choose the mode based on config or parameters
        print("Using Layered Mode for processing...")
        for question in questions:
            print(f"Processing question: {question}")
            # Use process_query instead of coordinate_interaction
            responses = self.process_query(question)
            all_results[question] = responses
            # Clear message pool for the next question if necessary
            self.message_pool.clear()  # Use clear instead of clear_messages

        print("Orchestration finished.")
        return all_results # Return collected results

    def run(self):
        # Initialize the communication mode
        self.communication_mode.initialize(self.agents)

        # Start the orchestration process
        self.orchestrate()

    def orchestrate(self):
        # Main orchestration logic
        while True:
            # Get messages from agents
            messages = self.communication_mode.get_messages()

            # Process messages with agents
            for agent in self.agents:
                responses = agent.process_messages(messages)
                self.communication_mode.update_responses(responses)

            # Check for termination condition
            if self.check_termination():
                break

    def check_termination(self):
        # Logic to determine if the orchestration should terminate
        return False  # Placeholder for actual termination logic