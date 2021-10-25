import os
import math
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    def __init__(self, output_dir) -> None:
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        if width > 500:
            raise Exception('Maximun width is 500')

        with Image.open(img_path) as im:
            height = math.ceil((width * im.height) / im.width)
            im_resized = im.resize((width, height))

            draw = ImageDraw.Draw(im_resized)
            font = ImageFont.truetype(
                './OpenSans-Regular.ttf', size=10, encoding='utf-8')
            font_width, font_height = font.getsize(text)

            x = random.randint(0, im_resized.width - font_width - 10)
            y = random.randint(0, im_resized.height - font_height * 2 - 10)

            draw.text((x, y), text, font=font)
            draw.text((x, y + 10), author, font=font)

            file_name = os.path.split(img_path)[1]
            destination = os.path.join(self.output_dir, file_name)
            # Create dir if not exist
            Path(self.output_dir).mkdir(parents=True, exist_ok=True)
            im_resized.save(destination)
            return destination
