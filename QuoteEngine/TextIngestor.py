from QuoteEngine import IngestorInterface, QuoteModel

class TextIngestor(IngestorInterface):
    ALLOWED_EXTENSIONS = ['.txt']

    def parse(cls, path: str):
        quotes = []
        with open(path, encoding='utf8') as f:
            lines = f.readlines()
            for line in lines:
                l = line.strip()
                if l:
                    text, author = l.split(' - ')
                    quotes.append(QuoteModel(text, author))
        return quotes
            