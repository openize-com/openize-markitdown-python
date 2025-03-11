import argparse
from pathlib import Path
from openize.markitdown.processor import DocumentProcessor
from openize.markitdown.license_manager import LicenseManager


def run_conversion(input_file):
    processor = DocumentProcessor()
    processor.process_document(input_file, insert_into_llm=False)
    print(f"Conversion completed: {input_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert documents to Markdown.")
    parser.add_argument("input_file", type=str, help="Path to the input file")
    args = parser.parse_args()

    license_manager = LicenseManager()
    license_manager.apply_license()

    run_conversion(args.input_file)

