import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os

def extract_text_from_file(filepath):
    text = ""
    if filepath.endswith(".pdf"):
        images = convert_from_path(filepath)
        text = " ".join([pytesseract.image_to_string(img) for img in images])
    else:
        img = Image.open(filepath)
        text = pytesseract.image_to_string(img)
    return text
