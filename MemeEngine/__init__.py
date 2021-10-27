"""Meme enginer module."""

import os
import math
import random
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from string import ascii_letters


class MemeEngine:
    """Meme Engine generator."""

    def __init__(self, output_dir) -> None:
        """Save output dir."""
        self.output_dir = output_dir
        self.font = ImageFont.truetype(
            './OpenSans-Regular.ttf', size=16, encoding='utf-8')
        self.avg_char_width = sum(self.font.getsize(
            char)[0] for char in ascii_letters) / len(ascii_letters)
        self.avg_char_height = sum(self.font.getsize(
            char)[1] for char in ascii_letters) / len(ascii_letters)

    def get_resized_image(self, im, width):
        """Return resized image."""
        height = math.ceil((width * im.height) / im.width)
        return im.resize((width, height))

    def calculate_max_char_count(self, width):
        """Return max number of chars in a line."""
        return int((width * .90) / self.avg_char_width)

    def generate_quote(self, width, text='', author=''):
        """Return a quote object."""
        max_width = self.calculate_max_char_count(width)

        quote_lines = textwrap.wrap(
            text, max_width) + textwrap.wrap(author, max_width)
        quote_text = ''
        for line in quote_lines:
            quote_text = quote_text + line + '\n'

        return {
            'text': quote_text,
            'height': len(quote_lines) * self.avg_char_height,
            'width': len(quote_lines) * max_width
        }

    def make_meme(self, img_path, text='', author='', width=500) -> str:
        """Generate a meme."""
        if width > 500:
            raise Exception('Maximun width is 500')

        with Image.open(img_path) as im:
            im_resized = self.get_resized_image(im, width)

            draw = ImageDraw.Draw(im_resized)

            quote = self.generate_quote(im_resized.width, text, author)

            x = random.randint(int(im_resized.width * .10),
                               int((im_resized.width * .90) - quote['width']))
            y = random.randint(int(im_resized.width * .10),
                               int((im_resized.height * .90) - quote['height']))

            draw.text((x, y), quote['text'], font=self.font)

            file_name = os.path.split(img_path)[1]
            destination = os.path.join(self.output_dir, file_name)
            # Create dir if not exist
            Path(self.output_dir).mkdir(parents=True, exist_ok=True)
            im_resized.save(destination)
            return destination
