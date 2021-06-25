#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   crypt.py    
@Contact :   https://github.com/liyansong2018/ReverseWidget
@License :   (C)Copyright 2021, liyansong

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/25 21:59   liyansong     1.0         None
'''


from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import DES3
from Crypto.Cipher import ARC2

from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import base64

MODE_ECB = 1
MODE_CBC = 2
MODE_CFB = 3
MODE_OFB = 5
MODE_CTR = 6
MODE_OPENPGP = 7
MODE_CCM = 8
MODE_EAX = 9
MODE_SIV = 10
MODE_GCM = 11
MODE_OCB = 12

KEY_64 = 1
KEY_128 = 2
KEY_192 = 3
KEY_256 = 4

class Cipher():
    def __init__(self, model, padding, key_length, key, iv):
        """
        Encryption Class
        :param model: int type
        :param padding: str type
        :param key_length: int type, 16,24,32
        :param key: bytes type
        :param iv:  bytes type
        """
        self.model = model
        self.padding = padding
        self.key_length = key_length
        self.key = key
        self.iv = iv

    def get_cipher_object(self, algorithm):
        """
        Get cipher object
        :param algorithm: Crypto.Cipher.AES/DES...
        :return: AES/DEX... object
        """
        if self.model in (MODE_ECB, MODE_CTR, MODE_CCM, MODE_EAX, MODE_SIV, MODE_GCM, MODE_OCB):
            cipher = algorithm.new(key=self.key, mode=self.model)
        else:
            cipher = algorithm.new(key=self.key, mode=self.model, iv=self.iv)

        return cipher

    def get_ciphertext(self, data, algorithm):
        """
        AES/DES/3DES/... Encryption function
        :param data: Data to be encrypted (bytes)
        :return: Encrypted data
        """
        padding_text = pad(data, self.key_length, self.padding)

        if algorithm == "AES":
            cipher = self.get_cipher_object(AES)

        elif algorithm == "DES":
            cipher = self.get_cipher_object(DES)

        elif algorithm == "3DES":
            cipher = self.get_cipher_object(DES3)

        elif algorithm == "RC2":
            cipher = self.get_cipher_object(ARC2)

        return cipher.encrypt(padding_text)


    def get_plaintext(self, data, algorithm):
        """
        AES/DES/3DES/... Decryption function
        :param data: Data to be decrypted (bytes)
        :return: Decrypted data
        """
        if algorithm == "AES":
            cipher = self.get_cipher_object(AES)

        elif algorithm == "DES":
            cipher = self.get_cipher_object(DES)

        elif algorithm == "3DES":
            cipher = self.get_cipher_object(DES3)

        elif algorithm == "RC2":
            cipher = self.get_cipher_object(ARC2)

        # Not all data is AES/DES/3DES/... encrypted
        # try:
        plain_text = cipher.decrypt(data)
        unpadding_text = unpad(plain_text, self.key_length, self.padding)
        # except ValueError:
        #     raise
        # else:
        return unpadding_text


if __name__ == "__main__":
    # Testcases
    s = "xiaoming".encode("utf-8")
    des3 = Cipher(1, 'pkcs7', 16, b'1234567812345678', b'')
    d = des3.get_ciphertext(s, "3DES")
    print(base64.encodebytes(d))