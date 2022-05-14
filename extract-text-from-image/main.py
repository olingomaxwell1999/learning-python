import pytesseract
import pillow

image = Image.open('./assets/image.jpg')

image

text = pytesseract.image_to_string(image)

print(text)