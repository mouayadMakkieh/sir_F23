import textract
import os
from docx import Document

def read_doc_file(doc_path):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    doc_path = os.path.join(BASE_DIR, 'SIR_app/Data/{0}'.format(doc_path))

    try:
        if doc_path.endswith('.docx'):
            # For.docx files, use the python-docx library
            doc = Document(doc_path)
            paragraphs = [paragraph.text for paragraph in doc.paragraphs]
            return '\n'.join(paragraphs)
        elif doc_path.endswith('.doc'):
            # For.doc files, use the textract library
            content = textract.process(doc_path).decode('utf-8')
            return content
        else:
            print(f"Unsupported file format: {doc_path}")
            return None
    except Exception as e:
        print(f"Error reading document: {e}")
        return None
