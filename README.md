# MemeGenerator

Meme generator allows you to create images with a quote placed randomly on the image. Included there are some random images and quotes that you can play with.
# Quick Overview

This project contains a Flask app and a CLI interface.
To run Flask app:
- Make sure you install all requirements.txt
- In the terminal type `python app.py`
- It should start a local server where you can access from your browser

To run the CLI:
- Make sure you install all requirements.txt
- In the terminal type `python meme.py`
- You can pass optional arguments:
    - `--path` The local file path
    - `--body` Body text of the quote
    - `--author` The author

# Package Contents

## Quote Engine Module
Class `Ingestor` allows you to parse files with quotes and returns a list of them.
Allowed file extensions are: .csv, .docx, .pdf, .txt.

### Example Usage
```
Ingestor.parse('./lib/img.png')
```
## Meme Engine Module
Class `MemeEngine` allows you to create a meme into a directory.
This class needs to be instanciated with the directory to write into.
```
meme = MemeEngine('/tmp')
```
You can then call `make_meme` 
Function accepts 4 positional arguments
- img_path
- text
- author
- width ( Max. 500)


### Example Usage
```
meme = MemeEngine('/tmp')
meme.make_meme('image_path.png', 'body', 'author')
```