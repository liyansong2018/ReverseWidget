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
"""The module of log .

This script contains log helper which will be used for print all kinds of log.
"""
"""日志打印模块

打印提示、错误以及调试日志。
"""

#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class Log():
    def __init__(self):
        pass

    @classmethod
    def info(cls, *args):
        """
        Print info information
        :param args: Multiple strings or tuples or bytes
        :return: null
        """
        data = ""
        for i in range(len(args)):
            if isinstance(args[i], tuple):
                data += str(args[i])
            elif isinstance(args[i], str):
                data += args[i]
            elif isinstance(args[i], bytes):
                data += str(args[i])
            data += " "

        # "\e[1;32m" Green
        print('\033[0;32m[+] %s\033[0m' % data)

    @classmethod
    def error(cls, *args):
        data = ""
        for i in range(len(args)):
            if isinstance(args[i], tuple):
                data += str(args[i])
            elif isinstance(args[i], str):
                data += args[i]
            elif isinstance(args[i], bytes):
                data += str(args[i])
            data += " "

        # "\e[1;31m" Red
        print('\033[0;31m[-] %s\033[0m' % data)

    @classmethod
    def debug(cls, *args):
        """
        Print debug information
        :param args: Multiple strings or tuples
        :return: null
        """
        data = ""
        for i in range(len(args)):
            if isinstance(args[i], tuple):
                data += str(args[i])
            elif isinstance(args[i], str):
                data += args[i]
            elif isinstance(args[i], bytes):
                data += str(args[i])
            data += " "

        # "\e[1;33m" Yellow
        print('\033[0;33m[*] %s\033[0m' % data)
