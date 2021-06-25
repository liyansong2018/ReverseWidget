English | Chinese

# Reverse Widget

Reverse Widget is a lightweight GUI Software that implements some typical  block cipher,  coding, hashing, and multi-architecture assemble/disassembly framework. Highlight Features:

- Some Typical Encryption Algorithms: AES, DES, 3DES, RC2
- Useful Coding: URL, Base64
- Common Hash: MD5, SHA1, SHA224, SHA256, SHA384, SHA512
- Multi-architecture Assembler and Disassembler: x86, ARM, mips, Sparc, PowerPC

## Detailed Description

### Encrypt/Decrypt

- Support input and output data for String, Hexadecimal and Base64 encoding String
- Support most encryption modes, including ECB, CBC, CFB, OFB, CTR, OPENPGP, OPENPGP, CCM, EAX, SIV, GCM, OCB
- Support three kinds of padding: pkcs7, iso7816 and ansix923

![encrypt_en](images/encrypt_en.png)



### Encode/Decode

- Support multiple hash algorithms
- Not only includes the hash calculation of ordinary strings, but also the hash of files, which can quickly calculate the hash value of large files

![hash_en](images/hash_en.png)



### Assemble/Disassemble

Support multiple architectures (x86, ARM, mips, Sparc, PowerPC), word length (16/32/64bit), big and little endian

![disasm_en](images/disasm_en.png)

The input format supported by assembly: Intel syntax format assembly instructions, and AT&T syntax format assembly instructions (x86)

- `add  x8, x8, x20`
- `add %ecx, %eax` (AT&T x86)

Input format supported by disassembly: hexadecimal or printable hexadecimal

- `08 01 14 8b`   
- `0801148b`
- `\x08\x01\x14\x8b`

Limitations

- X86 only supports little endian (limited by upstream keystone / capstone engine)

- Arm64 only supports little endian (currently aarch64 architecture only has little endian)

- Powerpc32 only supports big endian (currently powerpc32 architecture only has big endian)

## Compilation & Docs

Comming...

See [COMPILE.md](...) file for how to compile and install Reverse Widget. 

## Convenient Tool

Comming...

This is a software written in my spare time. There may be some bugs. It is being improved. Please understand.