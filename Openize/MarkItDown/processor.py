import os
from .factory import ConverterFactory
from .llm_strategy import SaveLocally, InsertIntoLLM

class DocumentProcessor:
    def __init__(self, output_dir="d://converted_md"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def process_document(self, file_path, insert_into_llm=False):
        file_extension = os.path.splitext(file_path)[1]
        converter = ConverterFactory.get_converter(file_extension)

        if not converter:
            print(f"No converter available for {file_extension}")
            return

        md_file = converter.convert_to_md(file_path, self.output_dir)
        strategy = InsertIntoLLM() if insert_into_llm else SaveLocally()
        strategy.process(md_file)
