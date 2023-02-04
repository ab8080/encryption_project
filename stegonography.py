import os
import sys


class Stegonography():

    BMP_HEADER_SIZE = 54
    BITS_IN_BYTE = 8
    DEGREE = 1

    def encrypt(self, input_img_name, output_img_name, txt_file):

        """
        Зашифровывает текст из файла txt_file в картинку input_img_name
        и сохраняет картинку с зашифрованным текстом в файл output_img_name.

        :param input_img_name: название изначальной BMP картинки
        :param output_img_name: название зашифрованной BMP картинки
        (создаст или перепишет)
        :param txt_file: название файла с текстом, который будет зашифрован
        :возвращает: TRUE если функция зашифровала, FALSE если не можт
        зашифровать из-за слишком длинного текста
        """

        text_len = os.stat(txt_file).st_size
        img_len = os.stat(input_img_name).st_size

        if text_len >= img_len / self.BITS_IN_BYTE - self.BMP_HEADER_SIZE:
            print("Too long text")
            return False

        with open(txt_file, "r") as text:
            with open(input_img_name, "rb") as input_image:
                with open(output_img_name, "wb") as output_image:
                    bmp_header = input_image.read(self.BMP_HEADER_SIZE)
                    output_image.write(bmp_header)
                    text_mask, img_mask = self.create_masks()
                    while True:
                        symbol = text.read(1)
                        if not symbol:
                            break
                        symbol = ord(symbol)

                        for byte_amount in range(self.BITS_IN_BYTE):
                            img_byte = int.from_bytes(input_image.read(1),
                                                      sys.byteorder)\
                                       & img_mask
                            bits = symbol & text_mask
                            bits >>= self.BITS_IN_BYTE - self.DEGREE
                            img_byte |= bits

                            output_image.write(img_byte.to_bytes
                                               (1, sys.byteorder))
                            symbol <<= self.DEGREE
                    output_image.write(input_image.read())

        return True

    def decrypt(self, encoded_img, output_txt, symbols_to_read):

        """
        Читает символы из зашифрованной картинки encoded_img,
        расшифровывает и записывает их в текстовый файл output_txt.

        :param encoded_img: название зашифрованной BMP картинки
        :param output_txt: название текстового айла, куда будет
        записан результат
        :param symbols_to_read: количество символов в зашифрованной картинке

        :возвращает: TRUE если функция расифровала, FALSE если не может
        расифровать из-за слишком длинного текста
        """

        img_len = os.stat(encoded_img).st_size

        if symbols_to_read >= img_len / self.BITS_IN_BYTE -\
                self.BMP_HEADER_SIZE:
            print("Too much symbols to read")
            return False

        with open(output_txt, "w", encoding="utf-8") as text:
            with open(encoded_img, "rb") as encoded_bmp:

                encoded_bmp.seek(self.BMP_HEADER_SIZE)

                _, img_mask = self.create_masks()
                img_mask = ~img_mask

                read = 0
                while read < symbols_to_read:
                    symbol = 0

                    for bits_read in range(self.BITS_IN_BYTE):
                        img_byte = int.from_bytes(encoded_bmp.read(1),
                                                  sys.byteorder)\
                                   & img_mask
                        symbol <<= self.DEGREE
                        symbol |= img_byte

                    if chr(symbol) == "\n" and os.linesep == "\r\n":
                        read += 1

                    read += 1
                    text.write(chr(symbol))

        return True

    def create_masks(self):

        """
        Создает текстовую маску и маску изображения

        :возвращает: маски для текста и картинки
        """
        start_mask = 0b11111111
        values_in_byte = 256

        text_mask = start_mask
        img_mask = start_mask
        text_mask <<= self.BITS_IN_BYTE - self.DEGREE
        text_mask %= values_in_byte
        img_mask >>= self.DEGREE
        img_mask <<= self.DEGREE
        return text_mask, img_mask
