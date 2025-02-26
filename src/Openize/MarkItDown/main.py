from Openize.MarkItDown.processor import DocumentProcessor

if __name__ == "__main__":
    processor = DocumentProcessor()

    # Process docx file and save locally
    processor.process_document("filename.docx", insert_into_llm=False)

    # Process xlsx file and save locally
    # processor.process_document("filename.xlsx", insert_into_llm=False)

    # Process pptx file and save locally
    # processor.process_document("filename.pptx", insert_into_llm=False)

    # Process pdf file and save locally
    # processor.process_document("filename.pdf", insert_into_llm=False)

    # Process documents and insert into LLM
    # processor.process_document("example.pdf", insert_into_llm=True)
