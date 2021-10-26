"""Ingestor Module."""
import os
from typing import List
from QuoteEngine import QuoteModel
from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """Abstract base class for Ingestors."""

    ALLOWED_TYPES = ['.csv', '.docx', '.pdf', '.txt']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if file matches extension."""
        return cls.get_file_extension(path) in cls.ALLOWED_TYPES

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return parsed file."""
        pass

    @classmethod
    def get_file_extension(self, path: str) -> str:
        """Return file extension."""
        filename, file_extension = os.path.splitext(path)
        return file_extension

    @classmethod
    def get_filename(self, path: str) -> str:
        """Return file name."""
        filename, file_extension = os.path.splitext(path)
        return filename
