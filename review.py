import argparse

from ceasar import Cezar
from hill import Hill
from stegonography import Stegonography
from vigenere import Vigenere
from vernam import Vernam


parser = argparse.ArgumentParser()

parser.add_argument("txt_file")
parser.add_argument("chiper")
parser.add_argument("action")
parser.add_argument("input_img", nargs='?')
parser.add_argument("output_img_or_chars_num", nargs='?')

args = parser.parse_args()


with open(args.txt_file, "r+") as f:
    text = f.read()
    key = 0
    if args.action != "hack" and args.chiper != "steg":
        key = input()
    list_of_functions = {
        "ceasar_encrypt": Cezar().encrypt_decrypt,
        "ceasar_decrypt": Cezar().encrypt_decrypt,
        "ceasar_hack": Cezar().hack,

        "vigenere_encrypt": Vigenere().encrypt,
        "vigenere_decrypt": Vigenere().decrypt,

        "vernam_encrypt": Vernam().encrypt_decrypt,
        "vernam_decrypt": Vernam().encrypt_decrypt,

        "hill_encrypt": Hill().encrypt_decrypt,
        "hill_decrypt": Hill().encrypt_decrypt,

        "steg_encrypt": Stegonography().encrypt,
        "steg_decrypt": Stegonography().decrypt

    }
    params = (text, key, args.action)

    if args.action == "hack":
        params = (text, )
    if args.chiper == "vernam" or args.chiper == "vigenere":
        params = (text, key)
    if args.chiper == "steg" and args.action == "encrypt":
        params = (args.input_img, args.output_img_or_chars_num, args.txt_file)
    if args.chiper == "steg" and args.action == "decrypt":
        params = (args.input_img, args.txt_file,
                  int(args.output_img_or_chars_num))

    print(list_of_functions[f"{args.chiper}_{args.action}"](*params))
