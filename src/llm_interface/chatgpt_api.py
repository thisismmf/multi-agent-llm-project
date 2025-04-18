import config
from openai import OpenAI

client = OpenAI(api_key=config.OPENAI_API_KEY)

class ChatGPTAPI:
    def __init__(self):
        pass

    def get_completion(self, prompt, model="gpt-4o-mini", agent_name=None):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            error_message = f"Error: Could not get response from API. Details: {e}"
            print(error_message)
            return error_message