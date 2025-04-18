import os
import sys
# Add the project root directory to PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from src.agents.agent_base import Agent
from src.communication.message_pool import SharedMessagePoolMode, MessagePool
from src.communication.layered_mode import LayeredMode
from src.communication.centralized_mode import CentralizedMode
from src.communication.decentralized_mode import DecentralizedMode
from src.core.orchestrator import Orchestrator
from src.llm_interface.chatgpt_api import ChatGPTAPI
from src.agents.specific_agent_1 import SpecificAgent1
from src.agents.specific_agent_2 import SpecificAgent2
from src.agents.specific_agent_3 import SpecificAgent3
from src.agents.specific_agent_4 import SpecificAgent4
from src.config import OPENAI_API_KEY

def main():
    # Initialize components
    chatgpt_api = ChatGPTAPI()
    
    # Initialize agents (passing required dependencies)
    # (Assuming agent __init__ methods require message_pool and chatgpt_api)
    # If message_pool is needed, create and pass it appropriately.
    message_pool = MessagePool()
    agents = [
        SpecificAgent1(message_pool, chatgpt_api),
        SpecificAgent2(message_pool, chatgpt_api),
        SpecificAgent3(message_pool, chatgpt_api),
        SpecificAgent4(message_pool, chatgpt_api)
    ]
    
    # Initialize all communication modes
    layered_mode = LayeredMode(agents)
    centralized_mode = CentralizedMode(agents)
    decentralized_mode = DecentralizedMode(agents)
    shared_pool_mode = SharedMessagePoolMode(agents)
    
    # Initialize orchestrator with all modes
    orchestrator = Orchestrator(
        layered_mode,
        centralized_mode,
        decentralized_mode,
        shared_pool_mode
    )
    
    # Define input questions
    questions = [
        "Which color do you prefer, blue or red?",
        "What is the best approach to solve complex problems?"
    ]
    
    # Process queries
    for question in questions:
        print(f"\nProcessing question: {question}")
        results = orchestrator.process_query(question)

        # Print results from each mode
        for mode_name, mode_results in results.items():
            print(f"\n{mode_name.upper()} MODE RESPONSES:")
            for agent_name, response in mode_results.items():
                print(f"{agent_name}: {response}")
            print("-" * 50)

if __name__ == "__main__":
    main()