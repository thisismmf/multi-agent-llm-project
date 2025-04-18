import unittest
from src.communication.message_pool import MessagePool
from src.communication.layered_mode import LayeredMode
from src.communication.centralized_mode import CentralizedMode
from src.agents.specific_agent_1 import SpecificAgent1
from src.agents.specific_agent_2 import SpecificAgent2

class TestCommunication(unittest.TestCase):

    def setUp(self):
        self.message_pool = MessagePool()
        self.agent1 = SpecificAgent1()
        self.agent2 = SpecificAgent2()
        self.layered_mode = LayeredMode([self.agent1, self.agent2])
        self.centralized_mode = CentralizedMode([self.agent1, self.agent2])

    def test_message_pool_add_and_retrieve(self):
        self.message_pool.add_message("Hello from agent 1")
        messages = self.message_pool.get_messages()
        self.assertIn("Hello from agent 1", messages)

    def test_layered_mode_response_update(self):
        self.layered_mode.process_initial_responses()
        self.layered_mode.update_responses()
        response1 = self.agent1.get_response()
        response2 = self.agent2.get_response()
        self.assertNotEqual(response1, response2)

    def test_centralized_mode_message_handling(self):
        self.centralized_mode.send_message("Hello from centralized mode")
        responses = self.centralized_mode.get_responses()
        self.assertEqual(len(responses), 2)

if __name__ == '__main__':
    unittest.main()