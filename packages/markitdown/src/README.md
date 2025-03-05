# Openize.MarkItDown

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-alpha-orange)

Openize.MarkItDown is a Python package that converts documents into Markdown format. It supports multiple file formats, provides flexible output handling, and integrates with LLMs for extended processing.

## Features

- Convert `.docx`, `.pdf`, `.xlsx`, and `.pptx` to Markdown.
- Save Markdown files locally or send them to an LLM for processing.
- Structured with the **Factory & Strategy Pattern** for scalability.
- Works with Windows and Linux-compatible paths.
- Command-line interface for easy use.

## Requirements

This package depends on the Aspose libraries, which are commercial products:

- [Aspose.Words](https://purchase.aspose.com/buy/words/python)
- [Aspose.Cells](https://purchase.aspose.com/buy/cells/python)
- [Aspose.Slides](https://purchase.aspose.com/buy/slides/python)

You'll need to obtain valid licenses for these libraries separately. The package will install these dependencies, but you're responsible for complying with Aspose's licensing terms.

## Installation

### From TestPyPI

```sh
pip install -i https://test.pypi.org/simple/ openize-markitdown
```

### From Source

```sh
git clone https://github.com/openize-com/Openize.MarkItDown.git
cd Openize.MarkItDown
pip install -e .
```

## Usage

### Command Line Interface

```sh
# Convert a file and save locally
markitdown document.docx

# Specify output directory
markitdown document.docx -o output_folder

# Process with an LLM (requires OPENAI_API_KEY environment variable)
markitdown document.docx --llm
```

### Python API

```python
from openize.markitdown import DocumentProcessor

# Initialize with custom output directory
processor = DocumentProcessor(output_dir="my_markdown_files")

# Convert files and save locally
processor.process_document("document.docx")
processor.process_document("presentation.pptx")
processor.process_document("spreadsheet.xlsx")
processor.process_document("sample.pdf")

# Send to LLM for processing (requires OPENAI_API_KEY environment variable)
processor.process_document("document.docx", insert_into_llm=True)
```

## Environment Variables

- `OPENAI_API_KEY`: Required when using the `insert_into_llm=True` option or the `--llm` flag.

## Running Tests

```sh
# Install test dependencies
pip install pytest pytest-mock

# Run the tests
pytest
```

## Contributing  

We appreciate your interest in contributing to this project! To ensure a smooth collaboration, please follow these steps when submitting a pull request:  

1. **Fork & Clone** – Fork the repository and clone it to your local machine.  
2. **Create a Branch** – Use a new branch for your contribution.  
3. **Sign the Contributor License Agreement (CLA)** – Before your first contribution can be accepted, you must sign our CLA via [CLA Assistant](https://cla-assistant.io). You will be prompted to sign it when submitting your first pull request. You can also review the CLA here: [https://cla.openize.com/agreement](https://cla.openize.com/agreement).  
4. **Submit a Pull Request (PR)** – Once your changes are ready, open a PR with a clear description.  
5. **Review & Feedback** – Our maintainers will review your PR and provide feedback if needed.  

By contributing, you agree to the terms of the CLA and confirm that your changes comply with the project's licensing policies.  

## License

This package is licensed under the MIT License. However, it depends on Aspose libraries, which are proprietary, closed-source libraries.

⚠️ Users must obtain a valid license for Aspose libraries separately. This repository does not include or distribute any proprietary components.
