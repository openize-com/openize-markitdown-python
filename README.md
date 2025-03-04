# Openize.MarkItDown

Openize.MarkItDown is a Python package that converts documents into Markdown format. It supports multiple file formats, provides flexible output handling, and integrates with LLMs for extended processing.

## Features

- Convert `.docx`, `.pdf`, `.xlsx`, and `.pptx` to Markdown.
- Save Markdown files locally or insert them into an LLM.
- Structured with the **Factory & Strategy Pattern** for scalability.
- Works on Windows and Linux-compatible paths.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/openize-com/Openize.MarkItDown.git
   cd Openize.MarkItDown
   ```

3. (Optional) Install the package:

   ```sh
   pip install -i https://test.pypi.org/simple/ Openize.MarkItDown
   ```

## Usage

### Convert Documents to Markdown

```python
from packages.markitdown.src.openize.markitdown.processor import DocumentProcessor

processor = DocumentProcessor()

# Convert files and save locally
processor.process_document("document.docx", insert_into_llm=False)
processor.process_document("presentation.pptx", insert_into_llm=False)
processor.process_document("spreadsheet.xlsx", insert_into_llm=False)
processor.process_document("sample.pdf", insert_into_llm=False)
```

### Insert Markdown into LLM

```python
processor.process_document("filename.docx", insert_into_llm=True)
```

## Running Tests

Run `pytest` to validate all use cases:

```sh
pytest
```
## Contributing  

We appreciate your interest in contributing to this project! To ensure a smooth collaboration, please follow these steps when submitting a pull request:  

1. **Fork & Clone** – Fork the repository and clone it to your local machine.  
2. **Create a Branch** – Use a new branch for your contribution.  
3. **Sign the Contributor License Agreement (CLA)** – Before your first contribution can be accepted, you must sign our CLA via [CLA Assistant](https://cla-assistant.io). You will be prompted to sign it when submitting your first pull request. You can also review the CLA here: [https://cla.openize.com/agreement](https://cla.openize.com/agreement).  
4. **Submit a Pull Request (PR)** – Once your changes are ready, open a PR with a clear description.  
5. **Review & Feedback** – Our maintainers will review your PR and provide feedback if needed.  

By contributing, you agree to the terms of the CLA and confirm that your changes comply with the project’s licensing policies.  

We appreciate your contributions and look forward to working with you!

## License

This wrapper is licensed under the MIT License. However, it depends on [CommercialLibrary](https://purchase.aspose.com/pricing/), which is a proprietary, closed-source library.

⚠️ Users must obtain a valid license for [CommercialLibrary](https://purchase.aspose.com/pricing/) separately. This repository does not include or distribute any proprietary components.
