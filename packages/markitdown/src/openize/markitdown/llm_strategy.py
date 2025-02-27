import logging
from abc import abstractmethod, ABC

import openai
class LLMStrategy(ABC):
    @abstractmethod
    def process(self, md_file): pass

class SaveLocally(LLMStrategy):
    def process(self, md_file):
        logging.info(f"File saved locally: {md_file}")

class InsertIntoLLM(LLMStrategy):
    def process(self, md_file):
        try:
            with open(md_file, "r", encoding="utf-8") as file:
                content = file.read()

            client = openai.OpenAI()  # Ensure you are using the new API client
            response = client.chat.completions.create(
                model="gpt-4",  # Change this to your required model
                messages=[{"role": "system", "content": "Process this Markdown content."},
                          {"role": "user", "content": content}]
            )

            logging.info("LLM Response: %s", response.choices[0].message.content)
        except Exception as e:
            logging.error(f"Error inserting into LLM: {e}")