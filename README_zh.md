# Reverse Widget
Reverse Wigdet 是一个完全使用 Python 实现的加解密、编解码、哈希以及支持多种架构的汇编和反汇编引擎**可视化**工具。具有如下特性
- 多个分组加密和解密算法：AES, DES, 3DES, RC2
- 编码和解码：URL, Base64
- 多个哈希算法：MD5, SHA1, SHA224, SHA256, SHA384, SHA512
- 多种架构的汇编和反汇编器：x86, ARM, mips, Sparc, PowerPC

## 细节性描述

### 加解密

- 支持输入和输出的数据为字符串、十六进制和 Base64 编码
- 支持绝大部分的加密模式，包括 ECB, CBC, CFB, OFB, CTR, OPENPGP, OPENPGP, CCM, EAX, SIV, GCM, OCB
- 支持三种填充模式：pkcs7, iso7816 和 ansix923

![encrypt_zh](images/encrypt_zh.png)



### 编解码

- 支持多个哈希算法
- 不仅包含对普通字符串的哈希计算，也包括对文件的哈希，可快速计算大文件的哈希值

![hash_zh](images/hash_zh.png)



### 汇编和反汇编

支持多种架构（x86, ARM, mips, Sparc, PowerPC）、字长（16/32/64bit）、大小端

![disasm_zh](images/disasm_zh.png)

汇编支持的输入格式：Intel 语法格式的汇编指令，也包括 AT&T 语法格式的汇编指令（ x86）
- `add  x8, x8, x20`
- `add %ecx, %eax` (AT&T x86)

反汇编支持的输入格式：十六进制或者可打印的十六进制

- `08 01 14 8b`   
- `0801148b`
- `\x08\x01\x14\x8b`

局限性

- x86 只支持小端模式（受限于上游的 Keystone/Capstone 引擎）
- ARM64 只有小端模式（当前 AArch64 架构本身只有小端 ）
- PowerPC32 只有大端模式（当前 PowerPC32 架构本身只有小端）

## 编译

关于怎样编译和安装，请查看 [Compile & Docs_zh](https://github.com/liyansong2018/ReverseWidget/wiki/Compile-&-Docs_zh)

## 开箱即用的发行版

参见已发布的版本



这是业余时间编写的一个软件，可能存在一些Bug，正在不断完善中，请谅解