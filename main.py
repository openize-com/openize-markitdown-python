import argparse
from pathlib import Path
from packages.markitdown.src.openize.markitdown.processor import DocumentProcessor

def run_conversion():
    processor = DocumentProcessor()


    processor.process_document("d://signform.pdf", insert_into_llm=False)

if __name__ == "__main__":
    run_conversion()
