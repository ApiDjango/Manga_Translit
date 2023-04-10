import easyocr
from PIL import Image
from translate import Translator

# Открываем изображение
image = Image.open('home_reader-light.png')

# Создаем экземпляр класса EasyOCR и выбираем язык распознавания
reader = easyocr.Reader(['en'])

# Применяем распознавание текста на изображении
result = reader.readtext(image)

# Объединяем результаты распознавания в одну строку
text = '\n'.join([res[1] for res in result])

# Переводим текст с помощью библиотеки translate
translator = Translator(to_lang="ru")
translated_text = translator.translate(text)

# Выводим распознанный и переведенный текст
print("Распознанный текст:\n", text)
print("\nПереведенный текст:\n", translated_text)
