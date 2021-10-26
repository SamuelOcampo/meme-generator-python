"""Quote Model Module."""
class QuoteModel:
    """A Quote object."""

    def __init__(self, body, author):
        """Store body and author."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return body - author."""
        return f'{self.body} - {self.author}'
