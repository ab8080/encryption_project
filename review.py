import sys
from ceasar import Cezar
from vigenere import Vigenere
from vernam import Vernam
from hill import Hill
from stegonography import Stegonography

if len(sys.argv) > 1:
    with open(sys.argv[1], "r") as f:
        text = f.read()
        chiper = sys.argv[2]
        action = sys.argv[3]
        if chiper == "ceasar":
            code = Cezar()
            if action == "encrypt":
                key = int(input())
                print(code.encrypt_decrypt(text, key, "e"))
            if action == "decrypt":
                key = int(input())
                print(code.encrypt_decrypt(text, key, "d"))
            if action == "hack":
                print(code.hack(text))
        if chiper == "vigenere":
            code = Vigenere()
            if action == "encrypt":
                key = input()
                print(code.encrypt(text, key))
            if action == "decrypt":
                key = input()
                print(code.decrypt(text, key))
        if chiper == "vernam":
            code = Vernam()
            key = input()
            print(code.encrypt_decrypt(text, key))
        if chiper == "hill":
            code = Hill()
            key = input()
            print(code.encrypt_decrypt(text, key, action))
        if chiper == "steg":
            code = Stegonography()
            if action == "encrypt":
                input_img = sys.argv[4]
                output_img = sys.argv[5]
                txt = sys.argv[1]
                code.encrypt(input_img, output_img, txt)
            if action == "decrypt":
                encrypted_img = sys.argv[4]
                output_txt = sys.argv[1]
                number_of_symbols = int(sys.argv[5])
                code.decrypt(encrypted_img, output_txt, number_of_symbols)
