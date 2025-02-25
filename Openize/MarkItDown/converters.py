import os
import re
import aspose.words as aw
import aspose.pdf as ap
import aspose.cells as ac
import aspose.slides as asl
from abc import ABC, abstractmethod

# Abstract class for document converters
class DocumentConverter(ABC):
    @abstractmethod
    def convert_to_md(self, input_path, output_dir): pass

    @staticmethod
    def clean_text(text):
        return re.sub(r"<[^>]*>", "", text).replace("&nbsp;", " ").strip()

# Concrete converters for each file type
class WordConverter(DocumentConverter):
    def convert_to_md(self, input_path, output_dir):
        doc = aw.Document(input_path)
        output_file = os.path.join(output_dir, os.path.basename(input_path).replace(".docx", ".md"))
        doc.save(output_file, aw.SaveFormat.MARKDOWN)
        return output_file

class PDFConverter(DocumentConverter):
    def convert_to_md(self, input_path, output_dir):
        doc = ap.Document(input_path)
        output_file = os.path.join(output_dir, os.path.basename(input_path).replace(".pdf", ".md"))
        doc.save(output_file, ap.SaveFormat.MARKDOWN)
        return output_file

class ExcelConverter(DocumentConverter):
    def convert_to_md(self, input_path, output_dir):
        workbook = ac.Workbook(input_path)
        output_file = os.path.join(output_dir, os.path.basename(input_path).replace(".xlsx", ".md"))
        workbook.save(output_file, ac.SaveFormat.MARKDOWN)
        return output_file

class PowerPointConverter(DocumentConverter):
    def convert_to_md(self, input_path, output_dir):
        presentation = asl.Presentation(input_path)
        output_file = os.path.join(output_dir, os.path.basename(input_path).replace(".pptx", ".md"))
        presentation.save(output_file, asl.export.SaveFormat.MD)
        return output_file
