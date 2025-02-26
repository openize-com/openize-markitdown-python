import argparse
from pathlib import Path
from packages.markitdown.src.openize.markitdown.processor import DocumentProcessor

def run_conversion():
    processor = DocumentProcessor()

    # Process PDF file
    # processor.process_document("d://signform.pdf", insert_into_llm=False)

    # Process Word document (.docx)
    # processor.process_document("d://example.docx", insert_into_llm=False)

    # Process PowerPoint file (.pptx)
    # processor.process_document("d://presentation.pptx", insert_into_llm=False)

    # Process Excel file (.xlsx)
    # processor.process_document("d://data.xlsx", insert_into_llm=False)

if __name__ == "__main__":
    run_conversion()

