import os
from typing import List
from QuoteEngine import QuoteModel
from abc import ABC


class IngestorInterface(ABC):
    ALLOWED_TYPES = ['.csv', '.docx', '.pdf', '.txt']

    def can_ingest(cls, path: str) -> bool:
        return cls.get_file_extension(path) in cls.ALLOWED_TYPES

    def parse(cls, path: str) -> List[QuoteModel]:
        pass

    def get_file_extension(self, path: str) -> str:
        filename, file_extension = os.path.splitext(path)
        return file_extension

    def get_filename(self, path: str) -> str:
        filename,file_extension = os.path.splitext(path)
        return filename
