class QuoteModel:
    """A  Quote object"""
    def __init__(self, text, author):
        self.text = text
        self.author = author

    def __repr__(self):
        return f'{self.text} - {self.author}'