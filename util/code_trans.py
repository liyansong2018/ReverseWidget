# MIT License
#
# Copyright (c) 2021 Yansong Li
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""The module of hash and crc.

This script contains hash functions and byte conversion.
"""
"""编解码类，一些常用的哈希算法和一些字节转换方法。
"""

#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import base64
import binascii
import hashlib
import zlib
from .ui_helper import *

class Code():
    def __init__(self):
        pass

    def bytes_to_hex(self, bytes):
        """
        bytes -> hexadecimal string, e.g, b'\x11\x12' -> "1112"
        :param bytes: bytes
        :return: hexadecimal string
        """
        data = binascii.hexlify(bytes)
        data = data.decode("utf-8")
        return data

    def bytes_to_hex_space(self, bytes):
        """
        bytes -> hexadecimal string, e.g, b'\x11\x12' -> "11 12"
        :param bytes: bytes
        :return: hexadecimal string
        """
        ret = ""
        hex_string = self.bytes_to_hex(bytes)
        for i in range(len(hex_string)):
            if i % 2 == 0:
                ret += hex_string[i]
            else:
                ret += hex_string[i] + " "
        return ret

    def hex_to_bytes(self, hex_string):
        """
        hexadecimal -> string bytes, e.g, 001122 -> b"001122"
        :param hex_string: hexadecimal string
        :return: bytes
        """
        data = binascii.unhexlify(hex_string)
        return data

    def bytes_to_base64(self, bytes):
        """
        bytes -> base64 string
        :param bytes: bytes
        :return: base64 string (76bit max!)
        """
        data = base64.encodebytes(bytes)
        data = data.decode("utf-8")
        return data

    def base64_to_bytes(self, base64_string):
        """
        base64 string -> bytes
        :param base64_string: base64 string
        :return: bytes
        """
        data = base64.decodebytes(base64_string.encode("utf-8"))
        return data

    def hex_to_base64(self, hex_string):
        """
        hex string -> base64 string
        :param hex_string: hex string
        :return: base64 string
        """
        bytes = self.hex_to_bytes(hex_string)
        base64_string = self.bytes_to_base64(bytes)
        return base64_string

    def base64_to_hex(self, base64_string):
        """
        base64 string -> hex string
        :param base64_string: base64 string
        :return: hex string
        """
        bytes = self.base64_to_bytes(base64_string)
        hex_string = self.bytes_to_hex(bytes)
        return hex_string

    def escaped_to_bytes(self, escaped_string):
        """
        escaped string -> bytes, e.g, \x11\x12 -> b'\x11\x12'
        :param escaped_string: escaped string
        :return: bytes
        """
        temp = self.escaped_to_hex(escaped_string)
        ret = self.hex_to_bytes(temp)
        return ret

    def escaped_to_hex(self, escaped_string):
        """
        escaped string -> hex, e.g, \x11\x12 -> 1112
        :param escaped_string: \x11
        :return: 11
        """
        ret = ""
        for i in escaped_string:
            if i in ("\\", "x"):
                i = ""
            ret += i
        return ret

    def list_to_hex_space(self, data):
        """
        list -> format hex, e.g, [65, 74] -> 41 4a
        :param data: list
        :return: string
        """
        ret = ""
        for i in data:
            ret += "%s " % (hex(i)[2:].zfill(2))
        return ret

    def list_to_escaped_space(self, data):
        """
        list -> format escaped string, e.g, [65, 74] -> \x41\x4a
        :param data: list
        :return: string
        """
        ret = ""
        for i in data:
            ret += "\\x%2s" % (hex(i)[2:].zfill(2))
        return ret

    def get_file_crc32(self, file):
        """
        compute crc of file in python
        :param file: file path
        :return: crc32
        """
        with open(file, 'rb') as fh:
            hash = 0
            while True:
                s = fh.read(65536)
                if not s:
                    break
                hash = zlib.crc32(s, hash)
            return "%08X" % (hash & 0xFFFFFFFF)

    def get_file_crc32_html(self, file):
        """
        wrapper for `get_file_crc`
        :return: crc32_html
        """
        return Helper.font_bold("CRC32") + ": " + self.get_file_crc32(file)

    def get_str_hash(self, data):
        """
        caculate hash: MD5, SHA1, SHA224, SHA256, SHA384, SHA512
        :param data: bytes array
        :return: "MD5: xxxx\nSHA224: xxxx\n..."
        """
        output_md5 = hashlib.md5(data).hexdigest()
        output_sha1 = hashlib.sha1(data).hexdigest()
        output_sha224 = hashlib.sha224(data).hexdigest()
        output_sha256 = hashlib.sha256(data).hexdigest()
        output_sha384 = hashlib.sha384(data).hexdigest()
        output_sha512 = hashlib.sha512(data).hexdigest()
        output = "MD5: " + output_md5 + "\n"
        output += "SHA1: " + output_sha1 + "\n"
        output += "SHA224: " + output_sha224 + "\n"
        output += "SHA256: " + output_sha256 + "\n"
        output += "SHA384: " + output_sha384 + "\n"
        output += "SHA512: " + output_sha512
        return output

    def get_file_hash(self, file_path):
        """
        caculate hash: MD5, SHA1, SHA224, SHA256, SHA384, SHA512
        :param file_path: file path
        :return: hash
        """
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha224 = hashlib.sha224()
        sha256 = hashlib.sha256()
        sha384 = hashlib.sha384()
        sha512 = hashlib.sha512()
        with open(file_path, "rb") as fp:
            while True:
                data = fp.read(4096)
                if not data:
                    break
                md5.update(data)
                sha1.update(data)
                sha224.update(data)
                sha256.update(data)
                sha384.update(data)
                sha512.update(data)

        output = "MD5: " + md5.hexdigest() + "\n"
        output += "SHA1: " + sha1.hexdigest() + "\n"
        output += "SHA224: " + sha224.hexdigest() + "\n"
        output += "SHA256: " + sha256.hexdigest() + "\n"
        output += "SHA384: " + sha384.hexdigest() + "\n"
        output += "SHA512: " + sha512.hexdigest()
        return output

    def get_file_hash_html(self, file_path):
        """
        wrapper for `get_file_hash`
        :param file_path: file path
        :return: html format
        """
        ret = self.get_file_hash(file_path)
        ret = ret.replace("MD5", Helper.font_bold("MD5"))
        ret = ret.replace("SHA1", Helper.font_bold("SHA1"))
        ret = ret.replace("SHA224", Helper.font_bold("SHA224"))
        ret = ret.replace("SHA256", Helper.font_bold("SHA256"))
        ret = ret.replace("SHA384", Helper.font_bold("SHA384"))
        ret = ret.replace("SHA512", Helper.font_bold("SHA512"))
        ret = ret.replace("\n", "<br />")
        return ret