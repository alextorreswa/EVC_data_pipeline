from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/python/3.10.4/lib/python3.10/site-packages'

print(pytesseract.image_to_string(Image.open('test.png')))
