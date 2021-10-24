import subprocess
from QuoteEngine import IngestorInterface, QuoteModel, TextIngestor

class PDFIngestor(IngestorInterface):
    ALLOWED_EXTENSIONS = ['.pdf']

    def parse(cls, path: str):
        subprocess.run(["ls", "-l"])
        return TextIngestor().parse()
            