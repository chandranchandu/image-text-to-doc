from docx import Document
from docx.shared import Inches

document = Document()
import pytesseract
from PIL import Image
img = Image.open('f6.jpg')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
img.load()
result = pytesseract.image_to_string(img)



document.add_paragraph(result)


document.add_page_break()

document.save('demo6.docx')
