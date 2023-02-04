import numpy as np

from gmpy2 import invert
from numpy.linalg import det, inv


class Hill:
    def encrypt_decrypt(self, text, key, action):

        """
        Зашифровывает или расшифровывает текст (в зависимости от action)
        с помощью введенного ключа

        :param text: ткст который надо зашифровать или расшифровать
        :param key: ключевое слово (матрица), с помощью которого будет
        зашифрован или расшифрован текст
        :param action: действие - зашифровать или расшифровать
        :возвращает: зашифрованный или расшифрованный текст
        (в зависимости от action)
        """
        abc_len = 26

        encrypted_message = ""

        matr = [[0] * len(text) for i in range(len(text))]

        txt = [[ord(char) - ord("A")] for char in text]

        for i in range(int(len(key) / len(text))):
            for j in range(int(len(key) / len(text))):
                matr[i][j] = ord(key[i * len(text) + j]) - ord("A")
        NpKey = np.array(matr)
        if action == "decrypt":
            def get_inverse_key(key):

                """
                Находит обратную матрицу к матрице key по модулю равному
                длине алфавита

                :param key: ключевое слово(матрица)
                :возвращает: обратную матрицу к матрице key по модулю равному
                длине алфавита или выдает ошибку если не существует обратной
                матрицы к матрице key по модулю равному длине алфавита
                (с помощью таких матриц невозможно расшифровать текст)
                """
                determinant = int(det(key))
                return np.array(np.round(inv(key) * determinant)
                                * int(invert(determinant, abc_len)),
                                dtype=int) % abc_len
            NpKey = (get_inverse_key(NpKey))
        NpText = np.array(txt)
        NpMatr = (np.dot(NpKey, NpText)) % abc_len
        for i in range(len(text)):
            encrypted_message += chr(NpMatr[i][0] + ord("A"))
        return encrypted_message
