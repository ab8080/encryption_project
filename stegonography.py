import os
import sys


class Stegonography():

    BMP_HEADER_SIZE = 54

    def encrypt(self, input_img_name, output_img_name, txt_file):

        text_len = os.stat(txt_file).st_size
        img_len = os.stat(input_img_name).st_size

        if text_len >= img_len / 8 - self.BMP_HEADER_SIZE:
            print("Too long text")
            return False

        text = open(txt_file, 'r')
        input_image = open(input_img_name, 'rb')
        output_image = open(output_img_name, 'wb')
        bmp_header = input_image.read(self.BMP_HEADER_SIZE)
        output_image.write(bmp_header)
        text_mask, img_mask = self.create_masks()
        while True:
            symbol = text.read(1)
            if not symbol:
                break
            symbol = ord(symbol)

            for byte_amount in range(8):
                img_byte = int.from_bytes(input_image.read(1), sys.byteorder) & img_mask
                bits = symbol & text_mask
                bits >>= 7
                img_byte |= bits

                output_image.write(img_byte.to_bytes(1, sys.byteorder))
                symbol <<= 1
        output_image.write(input_image.read())
        text.close()
        input_image.close()
        output_image.close()
        return True

    def decrypt(self, encoded_img, output_txt, symbols_to_read):

        img_len = os.stat(encoded_img).st_size

        if symbols_to_read >= img_len / 8 - self.BMP_HEADER_SIZE:
            print("Too much symbols to read")
            return False

        text = open(output_txt, 'w', encoding='utf-8')
        encoded_bmp = open(encoded_img, 'rb')

        encoded_bmp.seek(self.BMP_HEADER_SIZE)

        _, img_mask = self.create_masks()
        img_mask = ~img_mask

        read = 0
        while read < symbols_to_read:
            symbol = 0

            for bits_read in range(8):
                img_byte = int.from_bytes(encoded_bmp.read(1), sys.byteorder) & img_mask
                symbol <<= 1
                symbol |= img_byte

            if chr(symbol) == '\n' and len(os.linesep) == 2:
                read += 1

            read += 1
            text.write(chr(symbol))

        text.close()
        encoded_bmp.close()
        return True

    def create_masks(self):
        text_mask = 0b11111111
        img_mask = 0b11111111
        text_mask <<= 7
        text_mask %= 256
        img_mask >>= 1
        img_mask <<= 1
        return text_mask, img_mask

