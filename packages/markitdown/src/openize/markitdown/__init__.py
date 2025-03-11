import sys
import os

sys.path.append(os.path.dirname(__file__))

__version__ = "25.3.9"

from .processor import DocumentProcessor
from .converters import WordConverter, PDFConverter, ExcelConverter, PowerPointConverter
from .factory import ConverterFactory
from .llm_strategy import SaveLocally, InsertIntoLLM
from .license_manager import LicenseManager

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
