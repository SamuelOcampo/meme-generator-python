from QuoteEngine import IngestorInterface, QuoteModel
from docx import Document


class DocxIngestor(IngestorInterface):
    ALLOWED_TYPES = ['.docx']

    @classmethod
    def parse(cls, path: str):
        quotes = []
        doc = Document(path)
        for i in doc.paragraphs:
            l = i.text.strip()
            if l:
                text, author = l.split(' - ')
                quotes.append(QuoteModel(text, author))
        return quotes
