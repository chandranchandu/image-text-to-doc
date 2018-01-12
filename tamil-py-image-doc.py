from docx import Document
from docx.shared import Inches
document = Document()
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
result = pytesseract.image_to_string(Image.open("f3.jpg"), lang="tam")
document.add_paragraph(result)
document.add_page_break()
document.save('demo8.docx')



