from Openize.MarkItDown.processor import DocumentProcessor

if __name__ == "__main__":
    processor = DocumentProcessor()

    # Process documents and save locally
    processor.process_document("D://AsposeSampleData//draw.pptx", insert_into_llm=False)

    # Process documents and insert into LLM
    #processor.process_document("example.pdf", insert_into_llm=True)