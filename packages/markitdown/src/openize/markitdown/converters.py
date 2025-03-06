import os
import re
import logging
from pathlib import Path
import aspose.words as aw
import aspose.cells as ac
import aspose.slides as asl
from config import Config


from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class DocumentConverter(ABC):
    @abstractmethod
    def convert_to_md(self, input_path, output_dir): pass

    @staticmethod
    def clean_text(text):
        return re.sub(r"<[^>]*>", "", text).replace("&nbsp;", " ").strip()

class WordConverter(DocumentConverter):
    def convert_to_md(self, input_path, output_dir):
        try:
            doc = aw.Document(str(input_path))
            output_file = output_dir / (input_path.stem + ".md")
            doc.save(str(output_file), aw.SaveFormat.MARKDOWN)
            return output_file
        except Exception as e:
            logging.error(f"Error converting {input_path}: {e}")

class PDFConverter(DocumentConverter):
    def convert_to_md(self, input_path, output_dir):
        try:
            doc = aw.Document(str(input_path))
            output_file = output_dir / (input_path.stem + ".md")
            doc.save(str(output_file), aw.SaveFormat.MARKDOWN)
            return output_file
        except Exception as e:
            logging.error(f"Error converting {input_path}: {e}")

class ExcelConverter(DocumentConverter):
    def convert_to_md(self, input_path, output_dir):
        try:
            workbook = ac.Workbook(str(input_path))
            output_file = output_dir / (input_path.stem + ".md")
            workbook.save(str(output_file), ac.SaveFormat.MARKDOWN)
            return output_file
        except Exception as e:
            logging.error(f"Error converting {input_path}: {e}")

class PowerPointConverter(DocumentConverter):
    def convert_to_md(self, input_path, output_dir):
        try:
            presentation = asl.Presentation(str(input_path))
            output_file = output_dir / (input_path.stem + ".md")
            presentation.save(str(output_file), asl.export.SaveFormat.MD)
            return output_file
        except Exception as e:
            logging.error(f"Error converting {input_path}: {e}")

