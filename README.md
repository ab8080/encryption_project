# __Инструкция по запуску__

Если не установлен numpy:  
```bash
   pip install numpy
```

Если не установлен gmpy2:  
```bash
   sudo apt update
   sudo apt install python3-gmpy2
```

# __Сам запуск__
```bash
   git clone https://github.com/Sasha-nagibator/python -b dev

   cd python

   python3 review.py <путь к файлу с сообщением> <название шифра> <действие>
```
если действие encrypt или decrypt то в следующей строке нужно ввести ключ

Возможные названия шифра - "ceasar", "vigenere", "vernam"

Если шифр "ceasar", то возможные действия "encrypt", "decrypt", "hack"

Если шифр другой - только "encrypt", "decrypt"

Если шифр "hill", то длина ключа должена быть равной квадрату длины сообщения, которое хотите зашифровать

Если шифр - стегонография, то запуск происходит так:

Если зашифровываете - 
```bash
python3 review.py <путь к файлу с сообщением> steg encrypt <путь к изначальному файлу bmp> <путь к файлу bmp, который будет содержать зашифрованный текст>
```

Если расшифровываете - 
```bash
python3 review.py <путь к файлу в котором будет расшифрованное сообщение> steg decrypt <путь к зашифрованному файлу bmp> <количество символов в зашифрованном тексте>
```

# __Примеры__
Зашифровать шифром Цезаря текст из файла 1.txt:
```bash
   python3 review.py 1.txt ceasar encrypt
```
Зашифровать шифром Вернама текст из файла 1.txt:
```bash
   python3 review.py 1.txt vernam encrypt
```
Взломать текст из файла 1.txt зашифрованный шифром Цезаря:
```bash
   python3 review.py 1.txt ceasar hack
```
Расшифровать текст из файла 1.txt зашифрованный шифром Виженера:
```bash
   python3 review.py 1.txt vigenere decrypt
```
Зашифровать шифром Хилла текст из файла 1.txt:
```bash
   python3 review.py 1.txt hill encrypt
```
Зашифровать текст из файла 1.txt в картинку 1.bmp с помощью стеганографии, картинку с зашифрованным текстом назвать img.bmp:
```bash
   python3 review.py 1.txt steg encrypt 1.bmp img.bmp
```
Расшифровать текст из картинки img.bmp, длина текста - 22 символа, записать расшифрованный текст в файл 2.txt:
```bash
   python3 review.py 2.txt steg decrypt img.bmp 22
```
