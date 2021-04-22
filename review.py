import argparse
from ceasar import Cezar
from vigenere import Vigenere
from vernam import Vernam
from hill import Hill
from stegonography import Stegonography

parser = argparse.ArgumentParser()

parser.add_argument("txt_file")
parser.add_argument("chiper")
parser.add_argument("action")
parser.add_argument("input_img", nargs='?')
parser.add_argument("output_img_or_chars_num", nargs='?')

args = parser.parse_args()

with open(args.txt_file, "r+") as f:
    text = f.read()
    if args.chiper == "ceasar":
        code = Cezar()
        if args.action == "encrypt":
            key = int(input())
            print(code.encrypt_decrypt(text, key, "e"))
        if args.action == "decrypt":
            key = int(input())
            print(code.encrypt_decrypt(text, key, "d"))
        if args.action == "hack":
            print(code.hack(text))
    if args.chiper == "vigenere":
        code = Vigenere()
        if args.action == "encrypt":
            key = input()
            print(code.encrypt(text, key))
        if args.action == "decrypt":
            key = input()
            print(code.decrypt(text, key))
    if args.chiper == "vernam":
        code = Vernam()
        key = input()
        print(code.encrypt_decrypt(text, key))
    if args.chiper == "hill":
        code = Hill()
        key = input()
        print(code.encrypt_decrypt(text, key, args.action))
    if args.chiper == "steg":
        code = Stegonography()
        if args.action == "encrypt":
            code.encrypt(args.input_img, args.output_img_or_chars_num, args.txt_file)
        if args.action == "decrypt":
            code.decrypt(args.input_img, args.txt_file, int(args.output_img_or_chars_num))
