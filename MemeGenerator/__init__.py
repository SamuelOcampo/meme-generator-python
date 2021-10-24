import math
from PIL import Image, ImageDraw

class MemeGenerator:
    def __init__(self, output_dir) -> None:
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        if width > 500:
            raise  Exception('Maximun width is 500')

        with Image.open(img_path) as im:
            height = math.ceil((width * im.height) / im.width)
            im_resized = im.resize((width, height))
            ImageDraw.Draw(im_resized).text((0,0),text)
            ImageDraw.Draw(im_resized).text((0,0),author)
            im_resized.save('./hello-sam.png', "PNG")