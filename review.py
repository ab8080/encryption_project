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
        "hill_decrypt": Hill().encrypt_decrypt

    } 
    if args.chiper != "steg":  
        print(list_of_functions[f"{args.chiper}_{args.action}"](text, key, args.action))
    
    elif args.chiper == "steg":
        code = Stegonography()
        if args.action == "encrypt":
            code.encrypt(args.input_img, args.output_img_or_chars_num, args.txt_file)
        if args.action == "decrypt":
            code.decrypt(args.input_img, args.txt_file, int(args.output_img_or_chars_num))
