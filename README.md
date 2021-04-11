__Инструкция по запуску__

Если не установлен numpy:  pip install numpy

Если не установлен gmpy2:  

sudo apt update

sudo apt install python3-gmpy2

__Сам запуск__

git clone https://github.com/Sasha-nagibator/review1

python3 review.py <путь к файлу с сообщением> <название шифра> <действие>

если действие encrypt или decrypt то в следующей строке нужно ввести ключ

Возможные названия шифра - "ceasar", "vigenere", "vernam"

Если шифр "ceasar", то возможные действия "encrypt", "decrypt", "hack"

Если шифр другой - только "encrypt", "decrypt"

Если шифр "hill", то длина ключа должена быть равной квадрату длины сообщения, которое хотите зашифровать

Если шифр - __стегонография__, то запуск происходит так:

Если зашифровываете - python3 review.py <путь к файлу с сообщением> steg encrypt <путь к изначальному файлу bmp> <путь к файлу bmp, который будет содержать зашифрованный текст>

Если расшифровываете - python3 review.py <путь к файлу в котором будет расшифрованное сообщение> steg decrypt <путь к зашифрованному файлу bmp> <количество символов в зашифрованном тексте>

__Примеры__

python3 review.py /home/aleksandr/Review/python/1.txt ceasar encrypt

python3 review.py /home/aleksandr/Review/python/1.txt vernam encrypt

python3 review.py /home/aleksandr/Review/python/1.txt ceasar hack

python3 review.py /home/aleksandr/Review/python/1.txt vigenere decrypt

python3 review.py /home/aleksandr/Review/python/1.txt hill encrypt

python3 review.py /home/aleksandr/Review/python/text1.txt steg encrypt 1.bmp img.bmp

python3 review.py /home/aleksandr/Review/python/2.txt steg decrypt img.bmp 22
