import numpy as np
from numpy.linalg import det, inv
from gmpy2 import invert


class Hill:
    def encrypt_decrypt(self, text, key, action):
        abc_len = 26
        matr = []
        txt = []
        encrypted_message = ""
        for i in range(len(text)):
            matr.append([0] * len(text))
        for i in range(len(text)):
            txt.append([ord(text[i]) - ord('A')])
        for i in range(int(len(key) / len(text))):
            for j in range(int(len(key) / len(text))):
                matr[i][j] = ord(key[i * len(text) + j]) - ord('A')
        NpKey = np.array(matr)
        if action == "decrypt":
            def get_inverse_key(key):
                d = int(det(key))
                return np.array(np.round(inv(key) * d) * int(invert(d, abc_len)), dtype=int) % abc_len
            NpKey = (get_inverse_key(NpKey))
        NpText = np.array(txt)
        NpMatr = (np.dot(NpKey, NpText)) % abc_len
        for i in range(len(text)):
            encrypted_message += chr(NpMatr[i][0] + ord('A'))
        return encrypted_message
