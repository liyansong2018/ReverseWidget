#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   log.py    
@Contact :   https://github.com/liyansong2018/ReverseWidget
@License :   (C)Copyright 2021, liyansong

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/25 21:59   liyansong     1.0         None
'''


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

        print("[i] " + data)

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

        print("[-] " + data)

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

        print("[d] " + data)