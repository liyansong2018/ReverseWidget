#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   asm.py    
@Contact :   https://github.com/liyansong2018/ReverseWidget
@License :   (C)Copyright 2021, liyansong

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/25 21:57   liyansong     1.0         None
2021/9/25 17:42   liyansong     1.1         None
'''

from keystone import *
from capstone import *
from .code_trans import *

class Asm():
    def __init__(self, arch, mode, data, endian):
        """
        Assemble or Disassemble
        :param arch: architecture
        :param mode: 16bit/32bit/64bit -> 2B/4B/8B
        :param data: input data
        :param endian: little/big endian
        """
        self.arch = arch
        self.mode = mode
        self.data = data
        self.endian = endian

    def assemble(self):
        # ARM
        if self.arch == KS_ARCH_ARM:
            if self.mode == 2 or self.mode == 4:
                if self.endian == KS_MODE_BIG_ENDIAN:
                    self.mode = KS_MODE_ARM + self.endian
                else:
                    self.mode = KS_MODE_ARM

            elif self.mode == 8:
                # ARM64 only supports little endian
                self.arch = KS_ARCH_ARM64
                self.mode = KS_MODE_LITTLE_ENDIAN

        # PowerPC
        elif self.arch == KS_ARCH_PPC:
            if self.mode == 4:
                # 32 bit PowerPC architecture only supports big endian
                self.mode = KS_MODE_PPC32 + KS_MODE_BIG_ENDIAN
            elif self.mode == 8:
                self.mode = KS_MODE_PPC64
                if self.endian == KS_MODE_BIG_ENDIAN:
                    self.mode = KS_MODE_PPC64 + self.endian
        # Mips
        elif self.arch == KS_ARCH_MIPS:
            if self.endian == KS_MODE_BIG_ENDIAN:
                self.mode = self.mode + KS_MODE_BIG_ENDIAN

        # All
        ks = Ks(self.arch, self.mode)

        try:
            encoding, count = ks.asm(self.data)
            return encoding
        except Exception as e:
            pass

        # x86 AT&T
        try:
            if self.arch == KS_ARCH_X86:
                ks.syntax = KS_OPT_SYNTAX_ATT
                encoding, count = ks.asm(self.data)
                return encoding
        except Exception as e:
            # must raise
            raise

    def disassemble(self, base_addr):
        # ARM
        if self.arch == CS_ARCH_ARM:
            if self.mode == 2 or self.mode == 4:
                if self.endian == CS_MODE_BIG_ENDIAN:
                    self.mode = CS_MODE_ARM + self.endian
                else:
                    self.mode = CS_MODE_ARM

            elif self.mode == 8:
                # 64bit ARM64 only supports little endian
                self.arch = CS_ARCH_ARM64
                self.mode = CS_MODE_LITTLE_ENDIAN

        # PowerPC
        elif self.arch == CS_ARCH_PPC:
            if self.mode == 4:
                # 32 bit PowerPC architecture only supports big endian
                self.mode += CS_MODE_BIG_ENDIAN
            elif self.mode == 8:
                if self.endian == CS_MODE_BIG_ENDIAN:
                    self.mode += self.endian

        # Mips
        elif self.arch == CS_ARCH_MIPS:
            if self.endian == CS_MODE_BIG_ENDIAN:
                self.mode += CS_MODE_BIG_ENDIAN

        md = Cs(self.arch, self.mode)

        ret = ""
        change = Code()
        for i in md.disasm(self.data, base_addr):
            ret += "0x%x:\t%-30s\t%s\t%s\n" % (i.address, change.bytes_to_hex_space(i.bytes), i.mnemonic, i.op_str)

        return ret


if __name__ == "__main__":
    # Testcases
    data = b"ADD             X8, X8, X20"
    ks = Ks(KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN)
    encoding, count = ks.asm(data)
    print(encoding)