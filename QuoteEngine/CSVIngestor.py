import pandas as pd
from QuoteEngine import IngestorInterface, QuoteModel


class CSVIngestor(IngestorInterface):
    ALLOWED_TYPES = ['.csv']

    def parse(cls, path: str):
        quotes = []
        df = pd.read_csv(path)
        for index, row in df.iterrows():
            text = row['body']
            quotes.append(QuoteModel(f'"{text}"',  row['author']))

        return quotes
            