"""PDF ingestor Module."""

from QuoteEngine import IngestorInterface, QuoteModel
from docx import Document


class DocxIngestor(IngestorInterface):
    """Extends Ingestor interface."""
    
    ALLOWED_TYPES = ['.docx']

    @classmethod
    def parse(cls, path: str):
        """Parse .doc file."""
        quotes = []
        doc = Document(path)
        for i in doc.paragraphs:
            l = i.text.strip()
            if l:
                text, author = l.split(' - ')
                quotes.append(QuoteModel(text, author))
        return quotes
