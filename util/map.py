#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   map.py    
@Contact :   https://github.com/liyansong2018/ReverseWidget
@License :   (C)Copyright 2021, liyansong
'''

from keystone import *
from capstone import *


# asm---------------------------------
ARCH_BEFORE = 0
MODE_BEFORE = 0
ENDIAN_BEFORE = 0

map_arch_ks = {
    "x86": KS_ARCH_X86,
    "ARM": KS_ARCH_ARM,
    "MIPS": KS_ARCH_MIPS,
    "Sparc": KS_ARCH_SPARC,
    "PowerPC": KS_ARCH_PPC
}

map_arch_cs = {
    "x86": CS_ARCH_X86,
    "ARM": CS_ARCH_ARM,
    "MIPS": CS_ARCH_MIPS,
    "Sparc": CS_ARCH_SPARC,
    "PowerPC": CS_ARCH_PPC
}

map_mode = {
    "16bit": 2,
    "32bit": 4,
    "64bit": 8
}

map_endian_ks = {
    "Little Endian": KS_MODE_LITTLE_ENDIAN,
    "Big Endian": KS_MODE_BIG_ENDIAN
}

map_endian_cs = {
    "Little Endian": CS_MODE_LITTLE_ENDIAN,
    "Big Endian": CS_MODE_BIG_ENDIAN
}