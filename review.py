import sys
from ceasar import Cezar
from vigenere import Vigenere
from vernam import Vernam
from hill import Hill
from stegonography import Stegonography


if len(sys.argv) > 1:
    f = open(sys.argv[1], "r")
    text = f.read()
    chiper = sys.argv[2]
    action = sys.argv[3]
    if chiper == "ceasar":
        a = Cezar()
        if action == "encrypt":
            key = int(input())
            print(a.encrypt_decrypt(text, key, "e"))
        if action == "decrypt":
            key = int(input())
            print(a.encrypt_decrypt(text, key, "d"))
        if action == "hack":
            print(a.hack(text))
    if chiper == "vigenere":
        a = Vigenere()
        if action == "encrypt":
            key = input()
            print(a.encrypt(text, key))
        if action == "decrypt":
            key = input()
            print(a.decrypt(text, key))
    if chiper == "vernam":
        a = Vernam()
        key = input()
        print(a.encrypt_decrypt(text, key))
    if chiper == "hill":
        a = Hill()
        key = input()
        print(a.encrypt_decrypt(text, key, action))
    if chiper == "steg":
        a = Stegonography()
        if action == "encrypt":
            input_img = sys.argv[4]
            output_img = sys.argv[5]
            txt = sys.argv[1]
            a.encrypt(input_img, output_img, txt)
        if action == "decrypt":
            encrypted_img = sys.argv[4]
            output_txt = sys.argv[1]
            number_of_symbols = int(sys.argv[5])
            a.decrypt(encrypted_img, output_txt, number_of_symbols)
        
    f.close()

