import argparse
import os
import sys
import logging
from processor import DocumentProcessor
from license_manager import LicenseManager
from llm_strategy import InsertIntoLLM


def ask_user_boolean(question):
    """Ask the user a yes/no question and return True/False."""
    while True:
        response = input(f"{question} (yes/no): ").strip().lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def ensure_env_variable(var_name, prompt_message):
    """Ensure an environment variable is set, otherwise ask the user and persist it."""
    value = os.getenv(var_name)

    if not value:
        value = input(prompt_message).strip()
        if value:
            set_env_variable(var_name, value)
        else:
            print(f"Warning: {var_name} is not set. This may cause issues.")

    return value


def set_env_variable(var_name, value):
    """Set an environment variable persistently on Windows and Linux/macOS."""
    os.environ[var_name] = value  # Set for the current session

    if os.name == "nt":  # Windows
        os.system(f'setx {var_name} "{value}"')
    else:  # Linux/macOS
        os.system(f'echo "export {var_name}={value}" >> ~/.bashrc')
        os.system(f'echo "export {var_name}={value}" >> ~/.profile')


def run_conversion(input_file, output_dir, insert_into_llm=False):
    """Handle license setup, document processing, and optional LLM integration."""

    # Ask user if they want to use Aspose Paid APIs
    use_aspose = ask_user_boolean("Do you want to use the Aspose Paid APIs?")

    if use_aspose:
        ensure_env_variable("ASPOSE_LICENSE_PATH", "Enter the full path of your Aspose license file: ")
        license_manager = LicenseManager()
        license_manager.apply_license()
        # Only ask for OpenAI credentials if --insert-into-llm was specified

    if insert_into_llm:
        ensure_env_variable("OPENAI_API_KEY", "Enter your OpenAI API key: ")
        ensure_env_variable("OPENAI_MODEL", "Enter OpenAI model name (default: gpt-4): ")



    processor = DocumentProcessor(output_dir)
    processor.process_document(input_file, insert_into_llm)




def main():
    """Entry point for the CLI tool."""
    parser = argparse.ArgumentParser(description="Convert documents to Markdown.")
    parser.add_argument("input_file", help="Path to the input document (PDF, Word, etc.)")
    parser.add_argument("output_dir", help="Directory to save the converted Markdown file")
    parser.add_argument("--insert-into-llm", action="store_true", help="Insert output into LLM")

    args = parser.parse_args()

    try:
        run_conversion(args.input_file, args.output_dir, args.insert_into_llm)
    except Exception as e:
        print(f"Error: {e}")
        logging.error(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
