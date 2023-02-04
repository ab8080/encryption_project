class Vernam():

    def encrypt_decrypt(self, text, key):

        """
        Зашифровывает и одновременно расшифровывает зашифрованный текст
        с помощью введенного ключа

        :param text: ткст который надо зашифровать или расшифровать
        :param key: ключ, с помощью которого будет зашифрован или
        расшифрован текст
        :возвращает: зашифрованный или расшифрованный текст
        """
        alphabet_len = 26
        result = ""
        overflow = 0
        if ord(text[len(text) - 1]) < ord("A"):
            overflow = 1
        for i in range(len(text) - overflow):
            if ord(text[i]) <= ord("Z"):
                # "A" = 0, "B" = 1, ... , "Z" = 25, "a" = 26, ... "f" = 31
                code_char = ord(text[i]) - ord("A")
            else:
                code_char = ord(text[i]) - ord("a") + alphabet_len
            key_char = ord(key[i]) - ord("A")
            res = code_char ^ key_char          # "^" is XOR
            if res < alphabet_len:
                res += ord("A")
            else:
                res += ord("a") - alphabet_len
            result += chr(res)
        return result
