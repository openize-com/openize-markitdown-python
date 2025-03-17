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
markitdown document.docx -o output_folder --insert-into-llm
```

### Python API

```python
from _markitdown import MarkItDown

# Define input file and output directory
input_file = "report.pdf"
output_dir = "output_markdown"

# Create MarkItDown instance
converter = MarkItDown(output_dir)

# Convert document and send output to LLM
converter.convert_document(input_file, insert_into_llm=True)

print("Conversion completed and data sent to LLM.")

```

## Environment Variables

- `ASPOSE_LICENSE_PATH`: Required when using the Aspose Paid APIs. This should be set to the full path of your Aspose license file.
- `OPENAI_API_KEY`: Required when using the `insert_into_llm=True` option or the `--llm` flag.
- `OPENAI_MODEL`: Specifies the OpenAI model name (default: `gpt-4`).

To set these variables:

For Unix-based systems:

```bash
export ASPOSE_LICENSE_PATH="/path/to/license"
export OPENAI_API_KEY="your-api-key"
export OPENAI_MODEL="gpt-4"
```

For Windows (PowerShell):

```powershell
$env:ASPOSE_LICENSE_PATH = "C:\path\to\license"
$env:OPENAI_API_KEY = "your-api-key"
$env:OPENAI_MODEL = "gpt-4"
```



