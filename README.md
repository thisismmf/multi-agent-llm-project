# Multi-Agent LLM Project

This project implements a multi-agent system utilizing large language models (LLMs) to facilitate communication and collaboration among agents. The agents can operate in various modes, including message pooling, layered interaction, centralized communication, and decentralized approaches.

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