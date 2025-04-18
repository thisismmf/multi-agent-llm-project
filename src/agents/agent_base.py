class Agent:
    def __init__(self, name: str):
        self.name = name

    def process_message(self, message: str) -> str:
        raise NotImplementedError("Subclasses must implement process_message")