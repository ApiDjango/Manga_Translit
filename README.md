# Manga_Translit
Шаги для установки и добавления Tesseract OCR в PATH зависят от вашей операционной системы. Ниже приведены инструкции для некоторых из них:

# Windows
    Скачайте установщик Tesseract OCR с официального сайта: https://github.com/UB-Mannheim/tesseract/wiki. 
    Рекомендуется выбрать версию 4.1 или выше.
    Запустите установщик и следуйте инструкциям на экране.
    Добавьте путь к папке с исполняемым файлом Tesseract OCR в переменную окружения PATH. Например, если Tesseract OCR был установлен в папку "C:\Program Files\Tesseract-OCR", то необходимо добавить этот путь в переменную PATH.
    
# macOS
    Установите Tesseract OCR с помощью Homebrew, выполнив следующую команду в терминале:
    brew install tesseract
    Добавьте путь к папке с исполняемым файлом Tesseract OCR в переменную окружения PATH. 
    Например, если Tesseract OCR был установлен в папку "/usr/local/Cellar/tesseract/4.1.1/bin", 
      то необходимо добавить этот путь в переменную PATH.
      
# Linux (Ubuntu)
    Установите Tesseract OCR, выполнив следующую команду в терминале:
      sudo apt-get update
      sudo apt-get install tesseract-ocr
    Добавьте путь к папке с исполняемым файлом Tesseract OCR в переменную окружения PATH. 
    Например, если Tesseract OCR был установлен в папку "/usr/bin", то необходимо добавить этот путь в переменную PATH.
# Пример ответа
    Распознанный текст:
      THIS WORLD
      IS FULL OF
      IDIOTS.
    Переведенный текст:
      ЭТОТ МИР
      ПОЛОН
      ИДИОТОВ.
