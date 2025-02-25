import openai
from abc import ABC, abstractmethod

class LLMStrategy(ABC):
    @abstractmethod
    def process(self, md_file): pass

class SaveLocally(LLMStrategy):
    def process(self, md_file):
        print(f"File saved locally: {md_file}")

class InsertIntoLLM(LLMStrategy):
    def process(self, md_file):
        with open(md_file, "r", encoding="utf-8") as file:
            content = file.read()

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": content}]
        )

        print(f"Inserted into LLM: {response['choices'][0]['message']['content']}")
