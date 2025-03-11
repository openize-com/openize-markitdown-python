import argparse
import logging
from pathlib import Path
from processor import DocumentProcessor
from license_manager import LicenseManager

def run_conversion(input_file, output_dir, insert_into_llm=False):
    # Apply license
    license_manager = LicenseManager()
    license_manager.apply_license()

    # Process document
    processor = DocumentProcessor(output_dir)
    processor.process_document(input_file, insert_into_llm=insert_into_llm)

    print(f"Conversion completed: {input_file} → {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert documents to Markdown.")
    parser.add_argument("input_file", type=str, help="Path to the input file")
    parser.add_argument("output_dir", type=str, help="Path to the output directory")
    parser.add_argument(
        "--insert-into-llm",
        action="store_true",
        help="Insert output into LLM instead of saving locally"
    )
    args = parser.parse_args()

    run_conversion(args.input_file, args.output_dir, args.insert_into_llm)


