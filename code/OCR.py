import pytesseract
from PIL import Image
import fitz

# doc = fitz.open('.pdf')
# page = doc.load_page(3)
# mat = fitz.Matrix(2, 2)
# output = '.png'
# pix.save(output)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'
 
image = Image.open('Receipt.jpg')
result = pytesseract.image_to_string(image, lang = 'kor')
print(result)

# result.spilt()
