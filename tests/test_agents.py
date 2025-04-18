import unittest
from src.agents.agent_base import Agent
from src.agents.specific_agent_1 import SpecificAgent1
from src.agents.specific_agent_2 import SpecificAgent2
from src.communication.message_pool import MessagePool

class TestAgents(unittest.TestCase):

    def setUp(self):
        self.agent1 = SpecificAgent1()
        self.agent2 = SpecificAgent2()
        self.message_pool = MessagePool()

    def test_agent_initialization(self):
        self.assertIsInstance(self.agent1, SpecificAgent1)
        self.assertIsInstance(self.agent2, SpecificAgent2)

    def test_agent_send_receive_message(self):
        message = "Hello from Agent 1"
        self.agent1.send_message(message)
        self.assertIn(message, self.message_pool.messages)

        received_message = self.agent2.receive_message()
        self.assertEqual(received_message, message)

    def test_agent_response_processing(self):
        message = "What is the weather today?"
        self.agent1.send_message(message)
        response = self.agent1.process_response("It's sunny.")
        self.assertEqual(response, "It's sunny.")

    def test_multiple_agents_interaction(self):
        message1 = "Agent 1: How are you?"
        message2 = "Agent 2: I'm fine, thank you!"
        
        self.agent1.send_message(message1)
        self.agent2.send_message(message2)

        self.assertIn(message1, self.message_pool.messages)
        self.assertIn(message2, self.message_pool.messages)

if __name__ == '__main__':
    unittest.main()