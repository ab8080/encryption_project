from collections import Counter


class Cezar():
    def __init__(self):
        self.length = 26  # length of English alphabet
        # list of non letter symbols:
        self.non_letters = [
            ' ', '-', ',', '!', '?', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '0', ';', '/', '+', '(', ')', ':', chr(13), chr(10),
            chr(4), chr(3)]

    def encrypt_decrypt(self, text, key, action):

        """
        Зашифровывает или расшифровывает текст (в зависимости от action)
        с помощью введенного ключа

        :param text: ткст который надо зашифровать или расшифровать
        :param key: количество символов на которое надо сдвинуться,
        чтобы зашифровать или расшифровать
        :param action: действие - зашифровать или расшифровать
        :возвращает: зашифрованный или расшифрованный текст
        (в зависимости от action)
        """
        key = int(key)
        action_int = 1  # if action = encrypt
        if action == "decrypt":
            action_int = -1  # if action = decrypt
        result = ""
        for char in text:

            if char in self.non_letters:
                result += char
            else:
                # Encrypt uppercase characters
                if char.isupper():
                    result += chr((ord(char) + action_int * key - ord('A'))
                                  % self.length + ord('A'))
                # Encrypt lowercase characters
                else:
                    result += chr((ord(char) + action_int * key - ord('a'))
                                  % self.length + ord('a'))
        return result

    def hack(self, text):

        """
        Взламывает зашифрованный текст (подберает такой ключ, чтобы в
        расшифрованном тексте буква е встречалась чаще других букв,
        т.к. буква е самая часта в английском)

        :param text: зашифрованный текст
        :возвращает: расшифрованный текст
        """

        # list of number of each unique symbol
        count = Counter(list(text)).values()
        letters = Counter(list(text)).keys()  # list of unique symbols in text
        # dictionary with keys = count and values = letters
        stats = dict(zip(count, letters))
        max_count = max(count)  # number of the most common symbol in text
        # while the most common symbol is not letter I make its count = 0
        while stats[max_count] in self.non_letters:
            stats[0] = stats.pop(max_count)
            max_count = max(stats.keys())
        # 'e' is most frequent letter in English
        key_expected = ord(stats[max_count]) - ord("e")
        if ord(stats[max_count]) <= ord("Z"):
            key_expected = ord(stats[max_count]) - ord("E")
        return self.encrypt_decrypt(text, key_expected, "decrypt")
