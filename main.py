from cv2 import cv2
import pytesseract
from googletrans import Translator

translator = Translator()  # Обозначаем переводчик
config = r'--oem 3 --psm 6 -l jpn'  # Задаём параметры перевода
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  # Указываеи путь к tesseract


def translate(image_path, pronun=False, lang='en'):
    """Функция перевода текста"""
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = translator.translate(text=pytesseract.image_to_string(img,
                                                                   config=config).
                                  replace('\n', '').replace('.', '. ').replace(' ', '').replace('', ''),
                                  src='ja',
                                  dest='en')
    print(result)

    original_text = result.origin
    pronunciation_text = str(
        translator.translate(text=pytesseract.image_to_string(img,
                                                              config=config).
                             replace('\n', '').replace('.', '. ').replace(' ', '').replace('', ''),
                             src='ja',
                             dest='ja').pronunciation)

    if lang != 'en':
        result = translator.translate(result.text, src='en', dest=lang)

    if pronun:
        print(f'{original_text}  "{pronunciation_text}"  --> {result.text}')
    else:

        print(f'{original_text} --> {result.text}')

    return result.text


translate(image_path='C:\\Users\\Mikhail\\Desktop\\test.png')
