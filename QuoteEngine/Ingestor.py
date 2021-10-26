"""Quote engine main class."""
from typing import List
from QuoteEngine import DocxIngestor, TextIngestor, PDFIngestor, QuoteModel, IngestorInterface, CSVIngestor


class Ingestor(IngestorInterface):
    """Ingestor class."""

    INGESTORS = [DocxIngestor, TextIngestor, PDFIngestor, CSVIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Try to parse a file and returns a list of quotes."""
        if not cls.can_ingest(path):
            raise Exception('Invalid extension')

        for ingestor in cls.INGESTORS:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
