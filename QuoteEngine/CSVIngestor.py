"""CSV ingestor Module."""
import pandas as pd
from QuoteEngine import IngestorInterface, QuoteModel


class CSVIngestor(IngestorInterface):
    """Extends Ingestor interface."""

    ALLOWED_TYPES = ['.csv']

    @classmethod
    def parse(cls, path: str):
        """Parse .csv file."""
        quotes = []
        df = pd.read_csv(path)
        for index, row in df.iterrows():
            text = row['body']
            quotes.append(QuoteModel(f'"{text}"',  row['author']))

        return quotes
