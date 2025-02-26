from setuptools import setup, find_packages

setup(
    name="Openize.MarkItDown",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A document converter for Word, PDF, Excel, and PowerPoint to Markdown.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/openize-com/openize-markitdown",
    packages=find_packages(),
    install_requires=[
        "aspose-words",
        "aspose-pdf",
        "aspose-cells",
        "aspose-slides",
        "openai"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
