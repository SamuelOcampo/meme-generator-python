from typing import List
from QuoteEngine import QuoteModel
from abc import ABC


class IngestorInterface(ABC):
    ALLOWED_TYPES = ['csv', 'docx', 'pdf', 'txt']

    def can_ingest(cls, path: str) -> bool:
        return cls.get_extension(path) in cls.ALLOWED_TYPES

    def parse(cls, path: str) -> List[QuoteModel]:
        pass

    def get_extension(self, path: str) -> bool:
        return path.split(".")[-1]
