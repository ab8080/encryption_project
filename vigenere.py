from ceasar import Cezar


class Vigenere(Cezar):
    def __init__(self):
        super().__init__()

    def make_len_equal(self, str1, str2):

        """
        Делает длину двух строк одинаковой путем добавления в
        конец второй символов из ее начала

        :param str1: первая строка
        :param str2: вторая строка
        :возвращает: вторую строку, когда ее длина стала равной длине первой
        """
        i = 0
        str2_start_len = len(str2)
        non_letter_number = 0
        while len(str2) < len(str1):
            if str1[i + str2_start_len + non_letter_number] \
                    in self.non_letters:
                str2 += str1[i + str2_start_len + non_letter_number]
                non_letter_number += 1
            str2 += str2[i % str2_start_len]
            i += 1
        return str2

    def make_chars_equal(self, char1, char2):

        """
        Меняет второй символ на символ другого регистра если изначально
        регистры 1-го и 2-го символов не совпадают

        :param char1: первый символ
        :param char2: второй символ
        :возвращает: второй символ, когда того же регистра, что и первый
        """
        # making text and key both upper if they are not
        if char1.isupper() and char2.islower():
            char2 = chr(ord(char2) + ord("A") - ord("a"))
        # making text and key both lower if they are not
        if char1.islower() and char2.isupper():
            char2 = chr(ord(char2) - ord("A") + ord("a"))
        return char2

    def encrypt(self, text, keyword):

        """
        Зашифровывает текст с помощью ключевого слова.

        :param text: изначальный текст
        :param keyword: ключ (слово), с помощью
        которого будет зашифрован текст
        :возвращает: зашифрованный текст
        """
        # making chiper's length equal to message's length
        keyword = self.make_len_equal(text, keyword)
        result = ""  # encrypted message will be in result
        for i in range(len(text)):
            char1 = text[i]
            char2 = keyword[i]
            char2 = self.make_chars_equal(char1, char2)
            if char1 in self.non_letters:
                result += char1
            else:
                # Encrypt uppercase characters
                if char1.isupper():
                    result += chr((ord(char1) + ord(char2) - 2 * ord("A"))
                                  % self.length + ord("A"))
                # Encrypt lowercase characters
                else:
                    result += chr((ord(char1) + ord(char2) - 2 * ord("a"))
                                  % self.length + ord("a"))
        return result

    def decrypt(self, text, keyword):

        """
        Расшифровывает текст с помощью ключевого слова.

        :param text: зашифрованный текст
        :param keyword: ключ (слово), с помощью которого
        будет расшифрован текст
        :возвращает: расшифрованный текст
        """
        # making chiper's length equal to message's length
        keyword = self.make_len_equal(text, keyword)
        result = ""  # decrypted message will be in result
        for i in range(len(text)):
            char1 = text[i]
            char2 = keyword[i]
            char2 = self.make_chars_equal(char1, char2)
            if char1 in self.non_letters:
                result += char1
            else:
                # Decrypt uppercase characters
                if char1.isupper():
                    result += chr((ord(char1) - ord(char2))
                                  % self.length + ord("A"))
                # Decrypt lowercase characters
                else:
                    result += chr((ord(char1) - ord(char2))
                                  % self.length + ord("a"))
        return result
