# packages/markitdown/src/openize/markitdown/__init__.py
"""
Openize.MarkItDown - Convert documents to Markdown format

This package provides utilities to convert various document formats
(.docx, .pdf, .xlsx, .pptx) to Markdown format.
"""

__version__ = "25.3.8"

from processor import DocumentProcessor
from converters import WordConverter, PDFConverter, ExcelConverter, PowerPointConverter
from factory import ConverterFactory
from llm_strategy import SaveLocally, InsertIntoLLM
from license_manager import LicenseManager

__all__ = [
    'DocumentProcessor',
    'WordConverter',
    'PDFConverter',
    'ExcelConverter',
    'PowerPointConverter',
    'ConverterFactory',
    'SaveLocally',
    'InsertIntoLLM',
    'LicenseManager',
]
