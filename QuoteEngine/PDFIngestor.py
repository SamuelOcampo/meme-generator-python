import subprocess
import os
from QuoteEngine import IngestorInterface, QuoteModel, TextIngestor


class PDFIngestor(IngestorInterface):
    ALLOWED_TYPES = ['.pdf']

    def parse(cls, path: str):
        filename = cls.get_filename(path)
        tmp_file = f'{filename}_tmp.txt'
        subprocess.run(["pdftotext", "-raw", path, tmp_file])
        quotes = TextIngestor().parse(tmp_file)
        os.remove(tmp_file)
        return quotes
