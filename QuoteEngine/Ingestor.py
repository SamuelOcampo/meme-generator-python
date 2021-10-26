from typing import List
from QuoteEngine import DocxIngestor, TextIngestor, PDFIngestor, QuoteModel, IngestorInterface, CSVIngestor


class Ingestor(IngestorInterface):
    INGESTORS = [DocxIngestor, TextIngestor, PDFIngestor, CSVIngestor]

    def __init__(self):
        pass

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Invalid extension')

        for ingestor in cls.INGESTORS:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
