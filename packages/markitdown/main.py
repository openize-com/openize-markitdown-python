import argparse
from pathlib import Path
from openize.markitdown.processor import DocumentProcessor

def run_conversion():
    processor = DocumentProcessor()

    # Process PDF file
    # processor.process_document("file.pdf", insert_into_llm=False)

    # Process Word document (.docx)
    # processor.process_document("example.docx", insert_into_llm=False)

    # Process PowerPoint file (.pptx)
    # processor.process_document("presentation.pptx", insert_into_llm=False)

    # Process Excel file (.xlsx)
    # processor.process_document("data.xlsx", insert_into_llm=False)

if __name__ == "__main__":
    run_conversion()

