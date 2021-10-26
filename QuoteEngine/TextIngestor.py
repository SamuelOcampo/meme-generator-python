from QuoteEngine import IngestorInterface, QuoteModel


class TextIngestor(IngestorInterface):
    ALLOWED_TYPES = ['.txt']

    @classmethod
    def parse(cls, path: str):
        quotes = []
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                l = line.strip()
                if l:
                    text, author = l.split(' - ')
                    quotes.append(QuoteModel(text, author))
        return quotes
