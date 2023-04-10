import pytesseract
from PIL import Image
from translate import Translator

# Указываем путь к файлу с картинкой
image_path = "1635202484_1-pibig-info-p-manga-mem-anime-krasivo-1.png"

# Открываем картинку и преобразуем ее в черно-белый формат
image = Image.open(image_path)
image = image.convert('L')

# Распознаем текст на картинке с помощью Tesseract OCR
text = pytesseract.image_to_string(image, lang='eng')

# Переводим текст на английский язык с помощью библиотеки translate
translator = Translator(to_lang="ru")
translated_text = translator.translate(text)

# Выводим распознанный и переведенный текст
print("Распознанный текст:\n", text)
print("\nПереведенный текст:\n", translated_text)
