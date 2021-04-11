from ceasar import Cezar
class Vigenere(Cezar):
    def __init__(self):
        super().__init__()

    def make_len_equal(self, str1, str2):  # making str2 length equal to str1 length
        i = 0
        str2_start_len = len(str2)
        non_letter_number = 0
        while len(str2) < len(str1):   # making keyword's length equal to text length
            if str1[i + str2_start_len + non_letter_number] in self.non_letters:
                str2 += str1[i + str2_start_len + non_letter_number]
                non_letter_number += 1
            str2 += str2[i % str2_start_len]
            i += 1
        return str2

    def make_chars_equal(self, char1, char2):  # making 2 chars both lowwer or upper
        if char1.isupper() and char2.islower():
            char2 = chr(ord(char2) + ord('A') - ord('a'))  # making text and key both upper if they are not

        if char1.islower() and char2.isupper():
            char2 = chr(ord(char2) - ord('A') + ord('a'))  # making text and key both lower if they are not
        return char2

    def encrypt(self, text, keyword):                      # text - message, keyword - chiper
        keyword = self.make_len_equal(text, keyword)       # making chiper's length equal to message's length
        result = ""                                        # encrypted message will be in result
        for i in range(len(text)):
            char1 = text[i]
            char2 = keyword[i]
            char2 = self.make_chars_equal(char1, char2)
            if char1 in self.non_letters:
                result += char1
            else:
                # Encrypt uppercase characters
                if char1.isupper():
                    result += chr((ord(char1) + ord(char2) - 2 * ord('A')) % self.length + ord('A'))
                # Encrypt lowercase characters
                else:
                    result += chr((ord(char1) + ord(char2) - 2 * ord('a')) % self.length + ord('a'))
        return result

    def decrypt(self, text, keyword):                   # text - message, keyword - chiper
        keyword = self.make_len_equal(text, keyword)    # making chiper's length equal to message's length
        result = ""                                     # decrypted message will be in result
        for i in range(len(text)):
            char1 = text[i]
            char2 = keyword[i]
            char2 = self.make_chars_equal(char1, char2)
            if char1 in self.non_letters:
                result += char1
            else:
                # Decrypt uppercase characters
                if char1.isupper():
                    result += chr((ord(char1) - ord(char2)) % self.length + ord('A'))
                # Decrypt lowercase characters
                else:
                    result += chr((ord(char1) - ord(char2)) % self.length + ord('a'))
        return result

