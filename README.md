# Multi-Agent LLM Project

This project implements a multi-agent system utilizing large language models (LLMs) to facilitate communication and collaboration among agents. The agents can operate in various modes, including message pooling, layered interaction, centralized communication, and decentralized approaches.

## Project Structure

```
multi-agent-llm-project
├── src
│   ├── agents
│   │   ├── agent_base.py          # Base class for agents
│   │   ├── specific_agent_1.py    # Implementation of the first specific agent
│   │   └── specific_agent_2.py    # Implementation of the second specific agent
│   ├── communication
│   │   ├── message_pool.py         # Manages a pool of messages shared among agents
│   │   ├── layered_mode.py         # Coordinates interaction in a layered approach
│   │   └── centralized_mode.py     # Manages centralized communication among agents
│   ├── core
│   │   └── orchestrator.py         # Manages the overall flow of the application
│   ├── llm_interface
│   │   └── chatgpt_api.py         # Handles interactions with the ChatGPT API
│   ├── main.py                     # Entry point of the application
│   └── config.py                   # Configuration settings for the project
├── tests
│   ├── test_agents.py              # Unit tests for agent classes
│   └── test_communication.py       # Unit tests for communication classes
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation
```

## Features

- **Multiple Agents**: The system supports multiple agents that can process and respond to messages.
- **Communication Modes**: Agents can operate in different modes:
  - **Message Pool**: Agents share a common pool of messages.
  - **Layered Mode**: Agents update their responses based on previous answers in a structured manner.
  - **Centralized Mode**: A unified communication approach where all agents can access and respond to messages.
  - **Decentralized Mode**: Agents operate independently, allowing for more flexible interactions.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd multi-agent-llm-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure your API keys and other settings in `src/config.py`.

4. Run the application:
   ```
   python src/main.py
   ```

## Usage Examples

- To interact with the agents, you can modify the `main.py` file to send specific queries and observe how the agents respond based on the configured communication mode.

## Contribution

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and suggestions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for more details.