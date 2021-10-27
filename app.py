"""Flask application to generate random memes."""
import random
import os
import requests
from pathlib import Path
from flask import Flask, render_template, abort, request

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quote_files = [Ingestor.parse(file) for file in quote_files]
    quotes = [quote for quotes_per_file in quote_files for quote in quotes_per_file]

    images_path = "./_data/photos/dog/"
    valid_images = [".jpg", ".png"]

    imgs = []
    for f in os.listdir(images_path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(os.path.join(images_path, f))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    tmp_img = None
    path = None
    output_dir = './tmp'

    try:
        if image_url:
            img_name = image_url.rsplit('/', 1)[1]
            img_extension = img_name.split('.')[-1]
            if img_extension.lower() in ['png', 'jpg', 'jpeg']:
                try:
                    r = requests.get(image_url, allow_redirects=True)
                    tmp_img = os.path.join(output_dir, img_name)
                    Path(output_dir).mkdir(parents=True, exist_ok=True)
                    open(tmp_img, 'wb').write(r.content)
                    path = meme.make_meme(tmp_img, body, author)
                    os.remove(tmp_img)
                except:
                    raise Exception('Error trying to generate image.')
            else:
                error_msj = f'Invalid image extension {img_extension}'
                raise Exception(error_msj)
        else:
            raise Exception('Missing image')
    except:
        path = meme.make_meme('./imgs/black-img.jpeg', 'Invalid image')

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
