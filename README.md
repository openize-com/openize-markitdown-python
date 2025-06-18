# Openize.MarkItDown for Python

![Python Version](https://img.shields.io/badge/python-3.12+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-alpha-orange)

Openize.MarkItDown for Python is a package that converts documents into Markdown format. It supports multiple file formats, provides flexible output handling, and integrates with LLMs for extended processing including OpenAI, Claude, Gemini, and Mistral.

## Features

- Convert `.docx`, `.pdf`, `.xlsx`, and `.pptx` to Markdown.
- Save Markdown files locally or send them to an LLM for processing (OpenAI, Claude, Gemini, Mistral).
- Structured with the **Factory & Strategy Pattern** for scalability.
- Works with Windows and Linux-compatible paths.
- Command-line interface for easy use.

## Requirements

This package depends on the Aspose libraries, which are commercial products:

- [Aspose.Words](https://purchase.aspose.com/buy/words/python)
- [Aspose.Cells](https://purchase.aspose.com/buy/cells/python)
- [Aspose.Slides](https://purchase.aspose.com/buy/slides/python)

You'll need to obtain valid licenses for these libraries separately. The package will install these dependencies, but you're responsible for complying with Aspose's licensing terms.

LLM support requires valid API keys and potentially the following dependencies:

- `openai` for OpenAI
- `anthropic` for Claude
- `requests` for Gemini and Mistral REST APIs

## Installation

### From TestPyPI

```bash
pip install openize-markitdown-python
```

### From Source

```bash
git clone https://github.com/openize-com/openize-markitdown-python.git
cd openize-markitdown-python\packages\markitdown
pip install -e . --verbose
```

## Usage

### Command Line Interface

```bash
# Convert a file and save locally
markitdown document.docx -o output_folder

# Process with an LLM (requires corresponding API key)
markitdown document.docx -o output_folder --llm openai
markitdown document.docx -o output_folder --llm claude
markitdown document.docx -o output_folder --llm gemini
markitdown document.docx -o output_folder --llm mistral
```

### Python API

```python
from openize.markitdown.core import MarkItDown

# Define input file and output directory
input_file = "report.pdf"
output_dir = "output_markdown"

# Create MarkItDown instance with desired LLM
converter = MarkItDown(output_dir, llm_client_name="mistral")

# Convert document and send output to LLM
converter.convert_document(input_file)

print("Conversion completed and data sent to LLM.")
```

## Environment Variables

| Variable              | Description                                                        |
|-----------------------|--------------------------------------------------------------------|
| `ASPOSE_LICENSE_PATH` | Path to Aspose license file (required if using paid features)      |
| `OPENAI_API_KEY`      | API key for OpenAI integration                                     |
| `OPENAI_MODEL`        | (Optional) Model name for OpenAI (default: `gpt-4`)                |
| `CLAUDE_API_KEY`      | API key for Claude integration                                     |
| `CLAUDE_MODEL`        | (Optional) Model name for Claude (default: `claude-v1`)            |
| `GEMINI_API_KEY`      | API key for Gemini integration                                     |
| `GEMINI_MODEL`        | (Optional) Model name for Gemini (default: `gemini-pro`)           |
| `MISTRAL_API_KEY`     | API key for Mistral integration                                    |
| `MISTRAL_MODEL`       | (Optional) Model name for Mistral (default: `mistral-medium`)      |

### Setting Environment Variables

**Unix-based systems:**

```bash
export ASPOSE_LICENSE_PATH="/path/to/license"
export OPENAI_API_KEY="your-openai-key"
export CLAUDE_API_KEY="your-claude-key"
export GEMINI_API_KEY="your-gemini-key"
export MISTRAL_API_KEY="your-mistral-key"
```

**Windows (PowerShell):**

```powershell
$env:ASPOSE_LICENSE_PATH = "C:\path\to\license"
$env:OPENAI_API_KEY = "your-openai-key"
$env:CLAUDE_API_KEY = "your-claude-key"
$env:GEMINI_API_KEY = "your-gemini-key"
$env:MISTRAL_API_KEY = "your-mistral-key"
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
