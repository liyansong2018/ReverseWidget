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
"""The entry of ReverseWidget application.

This script contains the main running logic of the program. When I first wrote
this tool, the coding style was a bit confusing. Over time, the style of the code
added later has been optimized. If time permits, we will optimize the overall
architecture of the program later.
"""
"""程序入口

这个脚本包含了程序的主要运行逻辑。最初编写这个工具的时候，编码风格有些混乱。随着时间的推移，
后来增加的代码的编码风格已经被优化。如果时间允许，我们后续会优化程序的整体架构。
"""

# -*- encoding: utf-8 -*-
from ui.main_window import *
from util.crypt import *
from util.log import *
from ui.dialog_window import *
from util.map import *
from util.asm import *
from util.highlight import *
from urllib import parse

from ui.encrypt_window import *
from ui.code_window import *
from ui.asm_window import *

from ui.about_window import *
from ui.hash_window import *
from ui.format_window import *
from ui.appchecker_window import *
from ui.pechecker_window import *
from ui.dllinject_window import *
from ui.comment_window import *

# For macOS: not found QThread
from PyQt5.QtCore import *

import os
import json
from lxml import etree
import locale
import zipfile
import peid
from opensource.axmlprinter.apk import *
from opensource.QCodeEditor.QCodeEditor import *
import html
import webbrowser
import xmltodict
import random
import requests
import re

CRYPT = 1
CODE = 2
ASM = 3

FONT = None
ABOUT_TEXT_PATH = "./ui/resources/html/about.html"
APKINFO_PATH = "./ui/resources/html/apk_info.html"

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        QtWidgets.QMainWindow.__init__(self)
        # QTranslator object
        self.trans = []
        self.trans_num = 0

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        UiHelper(self.ui, self.ui.welcomeGroupBox).widget_show([self.ui.welcomeGroupBox])

        # Menu
        self.ui.actionOpen.triggered.connect(self.listen_action_open)
        self.ui.actionChinese.triggered.connect(lambda: self.listen_action_language(self.ui.actionChinese))
        self.ui.actionEnglish.triggered.connect(lambda: self.listen_action_language(self.ui.actionEnglish))
        # Set default language according to OS default settings
        if locale.getdefaultlocale()[0] == 'zh_CN':
            self.translate_chinese()
        self.ui.actionFont.triggered.connect(self.listen_action_font)
        self.ui.actionAbout.triggered.connect(self.listen_action_about)
        self.ui.actionAppChecker.triggered.connect(self.listen_action_appchecker)
        self.ui.actionPEChecker.triggered.connect(self.listen_action_pechecker)
        self.ui.actiondllInjector.triggered.connect(self.listen_action_dllinjector)

        # Button
        self.ui.cryptButton.clicked.connect(self.init_crypt)
        self.ui.codeButton.clicked.connect(self.init_code)
        self.ui.asmButton.clicked.connect(self.init_asm)
        self.ui.hashButton.clicked.connect(self.init_hash)
        self.ui.formatButton.clicked.connect(self.init_format)
        self.ui.commentButton.clicked.connect(self.init_comment)

        self.openfile = None
        self.function = None

    def init_ui_language(self):
        '''
        Fix display bug caused by language switching
        :return: null
        '''
        if self.function == CRYPT:
            self.init_crypt()
        elif self.function == CODE:
            self.init_code()
        elif self.function == ASM:
            self.init_asm()

    def init_ui_font(self, font=FONT):
        self.ui.centralwidget.setFont(font)
        self.ui.menubar.setFont(font)
        self.ui.statusbar.setFont(font)
        # Bug: can't modify font globally??
        self.ui.asmButton.setFont(font)
        self.ui.codeButton.setFont(font)
        self.ui.cryptButton.setFont(font)
        self.ui.formatButton.setFont(font)
        self.ui.hashButton.setFont(font)

    def listen_action_open(self):
        self.openfile = QFileDialog.getOpenFileName()[0]

    def listen_action_font(self):
        global FONT
        FONT, ok = QFontDialog.getFont()
        if ok:
            self.init_ui_font(FONT)

    def listen_action_language(self, language):
        """
        Listen language menu
        :param language: language, such as Chinese, English.
        :return: null
        """
        if language.text() == "Chinese":
            self.translate_chinese()
        elif language.text() == "English":
            self.translate_english()

        self.init_ui_language()

    def translate_chinese(self):
        _app = QApplication.instance()
        for file in os.listdir(os.path.join(os.getcwd(), 'ui/resources/language')):
            if file.endswith('.qm'):
                self.trans.append(QTranslator())
                self.trans[self.trans_num].load('ui/resources/language/%s' % file)
                _app.installTranslator(self.trans[self.trans_num])
                self.trans_num += 1

        for widget in UiHelper.all_widget:
            if widget != self.ui.welcomeGroupBox:
                widget.ui.retranslateUi(self)

        self.ui.retranslateUi(self)

    def translate_english(self):
        _app = QApplication.instance()
        for tran in self.trans:
            _app.removeTranslator(tran)

        for widget in UiHelper.all_widget:
            if widget != self.ui.welcomeGroupBox:
                widget.ui.retranslateUi(self)

        self.ui.retranslateUi(self)

    def listen_action_about(self):
        """
        open new ui of 'About'
        :return: null
        """
        about = AboutUi()
        about.show()
        about.exec_()

    def listen_action_appchecker(self):
        self.checker_ui = AppCheckerUi()
        self.checker_ui.show()

    def listen_action_pechecker(self):
        self.checker_ui = PeCheckerUi()
        self.checker_ui.show()

    def listen_action_dllinjector(self):
        if sys.platform == 'win32':
            start_dll_window()
        else:
            Log.error('Not Windows!')

    def init_crypt(self):
        self.crypto_ui = CryptoUi()
        UiHelper(self.ui).widget_show([self.crypto_ui])

    def init_code(self):
        self.code_ui = CodeUi()
        UiHelper(self.ui).widget_show([self.code_ui])

    def init_asm(self):
        self.asm_ui = AsmUi()
        UiHelper(self.ui).widget_show([self.asm_ui])

    def init_hash(self):
        self.hash_ui = HashUi()
        UiHelper(self.ui).widget_show([self.hash_ui])

    def init_format(self):
        self.format_ui = FormatUi()
        UiHelper(self.ui).widget_show([self.format_ui])

    def init_comment(self):
        self.comment_ui = CommentUi()
        UiHelper(self.ui).widget_show([self.comment_ui])


class CryptoUi(QtWidgets.QWidget):
    """
    Responsible for crypto
    """
    def __new__(cls, *args, **kwargs):
        """
        Singleton: only one window is allowed.
        """
        if not hasattr(cls, '_instance'):
            cls._instance = super(CryptoUi, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        Singleton: only once init
        """
        if not hasattr(CryptoUi, '_init'):
            super().__init__()
            self.init_ui()
            CryptoUi._init = True

    def init_ui(self):
        self.ui = Ui_CryptoWindow()
        self.ui.setupUi(self)

        self.ui.choiceAlgorithm.currentIndexChanged.connect(self.listen_algorithm)
        self.ui.lineEdit_2.setPlaceholderText("CBC/CFB/OFB/OPENPGP")
        self.ui.outputButton_1.clicked.connect(self.listen_action_encrypt)
        self.ui.outputButton_2.clicked.connect(self.listen_action_decrypt)

    def listen_action_encrypt(self):
        algorithm_choice = self.ui.choiceAlgorithm.currentText()
        self.start_encrypt(algorithm_choice)

    def listen_action_decrypt(self):
        algorithm_choice = self.ui.choiceAlgorithm.currentText()
        self.start_decrypt(algorithm_choice)

    def listen_algorithm(self):
        ui_helper = UiHelper(self.ui)
        ui_helper.combobox_item_disable(self.ui.modelComboBox, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        ui_helper.combobox_item_disable(self.ui.keySizeComboBox, 1, 2, 3, 4)  # 64/128/192/256

        name = self.ui.choiceAlgorithm.currentText()
        self.ui.nameLable.setText(name)

        if name == "AES":
            ui_helper.combobox_item_able(self.ui.modelComboBox, MODE_ECB, MODE_CBC, MODE_CFB, MODE_OFB, MODE_CTR,
                                         MODE_OPENPGP, MODE_CCM, MODE_EAX, MODE_GCM, MODE_SIV, MODE_OCB)  # 9 SIV Bug
            ui_helper.combobox_item_able(self.ui.keySizeComboBox, KEY_128, KEY_192, KEY_256)
            self.ui.keySizeComboBox.setCurrentIndex(KEY_128 - 1)

        elif name in ("DES", "RC2"):
            ui_helper.combobox_item_able(self.ui.modelComboBox, MODE_ECB, MODE_CBC, MODE_CFB, MODE_OFB, MODE_CTR,
                                         MODE_OPENPGP, MODE_EAX)
            ui_helper.combobox_item_able(self.ui.keySizeComboBox, KEY_64)
            self.ui.keySizeComboBox.setCurrentIndex(KEY_64 - 1)

        elif name == "3DES":
            ui_helper.combobox_item_able(self.ui.modelComboBox, MODE_ECB, MODE_CBC, MODE_CFB, MODE_OFB, MODE_CTR,
                                         MODE_OPENPGP, MODE_EAX)
            ui_helper.combobox_item_able(self.ui.keySizeComboBox, KEY_128, KEY_192)
            self.ui.keySizeComboBox.setCurrentIndex(KEY_128 - 1)

    def start_encrypt(self, algorithm_choice):
        Log.debug("start_encrypt", algorithm_choice)
        param_process = ParamProcess(self.ui)
        param_process.set_param(algorithm_choice)
        param = param_process.get_param()
        Log.info("encrypt", "parameter", param)

        if len(param) != 0:
            cipher = Cipher(model=param[0], padding=param[1], key_length=param[2], key=param[3], iv=param[4])

            try:
                encrypted_data = cipher.get_ciphertext(data=param[5], algorithm=algorithm_choice)
            except Exception as e:
                error = str(type(e)) + ": " + e.args[0]
                Log.error(error)
                self.ui.hexText.setText(error)
                return

            Log.info("encrypted data", encrypted_data)

            code = Code()
            # output hex
            output_hex = code.bytes_to_hex(encrypted_data)
            self.ui.hexText.setText(output_hex)
            # output base64
            output_base64 = code.bytes_to_base64(encrypted_data)
            self.ui.base64Text.setText(output_base64)

    def start_decrypt(self, algorithm_choice):
        Log.debug("start_decrypt", algorithm_choice)
        param_process = ParamProcess(self.ui)
        param_process.set_param(algorithm_choice)
        param = param_process.get_param()
        Log.info("aes_decrypt()", "parameter", param)

        if len(param) != 0:
            cipher = Cipher(model=param[0], padding=param[1], key_length=param[2], key=param[3], iv=param[4])
            try:
                plaintext = cipher.get_plaintext(data=param[5], algorithm=algorithm_choice)

            except Exception as e:
                error = str(type(e)) + ": " + e.args[0]
                Log.error(error)
                self.ui.hexText.setText(error)
                return

            Log.info("encrypted data", plaintext)

            code = Code()
            # output hex
            output_hex = code.bytes_to_hex(plaintext)
            self.ui.hexText.setText(output_hex)

            # output base64
            output_base64 = code.bytes_to_base64(plaintext)
            self.ui.base64Text.setText(output_base64)

            # output string
            output_string = plaintext.decode("utf-8")
            self.ui.stringText.setText(output_string)


class CodeUi(QtWidgets.QWidget):
    """
    Responsible for code
    """
    def __new__(cls, *args, **kwargs):
        """
        Singleton: only one window is allowed.
        """
        if not hasattr(cls, '_instance'):
            cls._instance = super(CodeUi, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        Singleton: only once init
        """
        if not hasattr(CodeUi, '_init'):
            super().__init__()
            self.init_ui()
            CodeUi._init = True

    def init_ui(self):
        self.ui = Ui_CodeWindow()
        self.ui.setupUi(self)

        self.ui.outputButton_1.clicked.connect(self.listen_action_encode)
        self.ui.outputButton_2.clicked.connect(self.listen_action_decode)

    def listen_action_encode(self):
        self.start_encode()

    def listen_action_decode(self):
        self.start_decode()

    def start_encode(self):
        """
        Qtable widget for encode
        :return: null
        """
        TAG = 'Encode'
        Log.info(">>> %s" % TAG)
        current_index = self.ui.tabWidget_2.currentIndex()
        code = Code()
        _input = ''
        _output = ''

        try:
            # URL Encode
            if current_index == 0:
                _input = self.ui.urlTabText.toPlainText()
                _input = _input.encode("utf-8")
                Log.info("input: %s" % _input)
                _output = parse.quote(_input)
                Log.info("output: %s" % _output)
                self.ui.codeOutput.setText(_output)

            # HTML Encode
            if current_index == 1:
                _input = self.ui.htmlTabText.toPlainText()
                Log.info("input: %s" % _input)
                _output = html.escape(_input)
                Log.info("output: %s" % _output)
                self.ui.codeOutput.setPlainText(_output)

            # Base64 Encode
            elif current_index == 2:
                _input = self.ui.base64TabText.toPlainText()
                _input = _input.encode("utf-8")
                Log.info("input: %s" % _input)
                _output = code.bytes_to_base64(_input)
                # delete CR LF
                strip_output = ''
                for char in _output:
                    if char == '\r' or char == '\n':
                        continue
                    strip_output += char

                Log.info("output: %s" % _output)
                self.ui.codeOutput.setText(strip_output)

            # Hash from text: MD5, SHA1, SHA224, SHA256, SHA384, SHA512
            elif current_index == 3:
                _input = self.ui.hashTabText.toPlainText()
                Log.info("input: %s" % _input)
                # 1.data
                if _input != "":
                    _input = _input.encode("utf-8")
                    _output = code.get_str_hash(_input)

                Log.info("output: %s" % _output)
                self.ui.codeOutput.setText(_output)

            # Unicode Encode
            elif current_index == 4:
                _input = self.ui.unicodeTabText.toPlainText()
                Log.info("input: %s" % _input)
                _output = _input.encode("raw_unicode_escape").decode()
                Log.info("output: %s" % _output)
                self.ui.codeOutput.setText(_output)

            # Reserve funciton
            elif current_index == 5:
                pass

        except Exception as e:
            self.ui.codeOutput.setText(Helper.font_red(str(e)))
            Log.error(str(e))

    def start_decode(self):
        """
        Qtable widget for decode
        :return:
        """
        TAG = 'Decode'
        Log.info(">>> %s" % TAG)
        current_index = self.ui.tabWidget_2.currentIndex()
        code = Code()
        _input = ''
        _output = ''

        try:
            # URL Decode
            if current_index == 0:
                _input = self.ui.urlTabText.toPlainText()
                Log.info("input: %s" % _input)
                _output = parse.unquote(_input)
                Log.info("output: %s" % _output)
                self.ui.codeOutput.setText(_output)

            # HTML Decode
            if current_index == 1:
                _input = self.ui.htmlTabText.toPlainText()
                Log.info("input: %s" % _input)
                _output = html.unescape(_input)
                Log.info("output: %s" % _output)
                self.ui.codeOutput.setPlainText(_output)

            # Base64 Decode
            elif current_index == 2:
                _input = self.ui.base64TabText.toPlainText()
                Log.info("input: %s" % _input)
                _output = code.base64_to_bytes(_input)
                Log.info("output: %s" % _output)
                self.ui.codeOutput.setText(_output.decode("utf-8"))

            # Hash from file: MD5, SHA1, SHA224, SHA256, SHA384, SHA512
            elif current_index == 3:
                pass

            # Unicode Decode
            elif current_index == 4:
                _input = self.ui.unicodeTabText.toPlainText()
                Log.info("input: %s" % _input)
                _output = _input.encode("utf-8").decode("unicode_escape")
                Log.info("output: %s" % _output)
                self.ui.codeOutput.setText(_output)

            # Reserve funciton
            elif current_index == 5:
                pass

        except Exception as e:
            self.ui.codeOutput.setText(Helper.font_red(str(e)))
            Log.error(str(e))


class AsmUi(QtWidgets.QWidget):
    """
    Responsible for assemble
    """
    def __new__(cls, *args, **kwargs):
        """
        Singleton: only one window is allowed.
        """
        if not hasattr(cls, '_instance'):
            cls._instance = super(AsmUi, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        Singleton: only once init
        """
        if not hasattr(AsmUi, '_init'):
            super().__init__()
            self.init_ui()
            AsmUi._init = True

    def init_ui(self):
        self.ui = Ui_AsmWindow()
        self.ui.setupUi(self)

        # Set defalut options
        self.ui.x86Button.click()
        self.ui.mode32Button.click()
        self.ui.littleButton.click()
        global ARCH_BEFORE
        global MODE_BEFORE
        global ENDIAN_BEFORE
        ARCH_BEFORE = self.ui.x86Button.text()
        MODE_BEFORE = self.ui.mode32Button.text()
        ENDIAN_BEFORE = self.ui.littleButton.text()
        self.ui.lineEditBaseAddr.setText("0x0804800")

        self.listen_arch(self.ui.x86Button)
        self.ui.x86Button.toggled.connect(lambda: self.listen_arch(self.ui.x86Button))
        self.ui.armButton.toggled.connect(lambda: self.listen_arch(self.ui.armButton))
        self.ui.mipsButton.toggled.connect(lambda: self.listen_arch(self.ui.mipsButton))
        self.ui.sparcButton.toggled.connect(lambda: self.listen_arch(self.ui.sparcButton))
        self.ui.powerPcButton.toggled.connect(lambda: self.listen_arch(self.ui.powerPcButton))

        self.ui.mode16Button.toggled.connect(lambda: self.listen_mode(self.ui.mode16Button))
        self.ui.mode32Button.toggled.connect(lambda: self.listen_mode(self.ui.mode32Button))
        self.ui.mode64Button.toggled.connect(lambda: self.listen_mode(self.ui.mode64Button))

        self.ui.littleButton.toggled.connect(lambda: self.listen_endian(self.ui.littleButton))
        self.ui.bigButton.toggled.connect(lambda: self.listen_endian(self.ui.bigButton))

        self.ui.outputButton_1.clicked.connect(self.listen_action_asm)
        self.ui.outputButton_2.clicked.connect(self.listen_action_disasm)

    def listen_action_asm(self):
        self.start_asm()

    def listen_action_disasm(self):
        self.start_disasm()

    def listen_arch(self, arch):
        """
        Monitor architecture changes selected by users.
        :param arch: x86, ARM, MIPS, Sparc, PowerPC
        :return: null
        """
        if True:
            global ARCH_BEFORE
            ARCH_BEFORE = arch.text()

            # x86 or ARM64 architecture only supports little endian
            if ARCH_BEFORE == "x86" or (ARCH_BEFORE == "ARM" and MODE_BEFORE == "64bit"):
                self.ui.bigButton.close()
                self.ui.littleButton.click()
            else:
                self.ui.bigButton.show()

            # 32 bit PowerPC architecture only supports big endian
            if ARCH_BEFORE == "PowerPC" and MODE_BEFORE == "32bit":
                self.ui.littleButton.close()
                self.ui.bigButton.click()
            else:
                self.ui.littleButton.show()

    def listen_mode(self, mode):
        """
        Monitor mode changes selected by users.
        :param mode: 32bit, 64bit
        :return: null
        """
        if True:
            global MODE_BEFORE
            MODE_BEFORE = mode.text()

            # x86 or ARM64 architecture only supports little endian
            if ARCH_BEFORE == "x86" or (ARCH_BEFORE == "ARM" and MODE_BEFORE == "64bit"):
                self.ui.bigButton.close()
                self.ui.littleButton.click()
            else:
                self.ui.bigButton.show()

            # 32 bit PowerPC architecture only supports big endian
            if ARCH_BEFORE == "PowerPC" and MODE_BEFORE == "32bit":
                self.ui.littleButton.close()
                self.ui.bigButton.click()
            else:
                self.ui.littleButton.show()

            if MODE_BEFORE == "16bit":
                self.ui.lineEditBaseAddr.setText("0x1000")
            elif MODE_BEFORE == "32bit":
                self.ui.lineEditBaseAddr.setText("0x0804800")
            else:
                self.ui.lineEditBaseAddr.setText("0x400000")

    def listen_endian(self, endian):
        """
        Monitor endian changes selected by users.
        :param endian: little, big endian
        :return: null
        """
        if endian.isChecked():
            global ENDIAN_BEFORE
            ENDIAN_BEFORE = endian.text()

    def start_asm(self):
        arch = map_arch_ks.get(ARCH_BEFORE)
        mode = map_mode.get(MODE_BEFORE)
        asm_code = self.ui.inputData.toPlainText()
        endian = map_endian_ks.get(ENDIAN_BEFORE)

        if arch == None:
            dialog = DialogWindow()
            dialog.dialog_user_arch()
            return

        if mode == None:
            dialog = DialogWindow()
            dialog.dialog_user_mode()
            return

        if endian == None:
            dialog = DialogWindow()
            dialog.dialog_user_endian()
            return

        if "\\" in asm_code:
            dialog = DialogWindow()
            dialog.diaglog_user_input()
            return

        asm_code = asm_code.encode()

        try:
            asm = Asm(arch, mode, asm_code, endian)
            result = asm.assemble(int(self.ui.lineEditBaseAddr.text(), 16))

            # Format Result
            trans = Code()
            result_hex = trans.list_to_hex_space(result)
            result_escaped = trans.list_to_escaped_space(result)
            self.ui.outputAsmHex.setText(result_hex)
            self.ui.outputAsmEscaped.setText(result_escaped)
            self.ui.outputAsmEscaped.show()
        except Exception as e:
            Log.error("start_asm()", e)
            dialog = DialogWindow()
            dialog.diaglog_user_input()
            return

    def start_disasm(self):
        arch = map_arch_cs.get(ARCH_BEFORE)
        mode = map_mode.get(MODE_BEFORE)
        binary_input = self.ui.inputData.toPlainText()
        endian = map_endian_cs.get(ENDIAN_BEFORE)

        if arch == None:
            dialog = DialogWindow()
            dialog.dialog_user_arch()
            return

        if mode == None:
            dialog = DialogWindow()
            dialog.dialog_user_mode()
            return

        if endian == None:
            dialog = DialogWindow()
            dialog.dialog_user_endian()
            return

        trans = Code()
        try:
            # user input: \x00\x11
            binary_bytes = trans.escaped_to_bytes(binary_input)
        except Exception as e:
            Log.error(e)
            try:
                # user input: 0011 or 00 01
                binary_bytes = trans.hex_to_bytes(binary_input.replace(" ", ""))
            except Exception as e1:
                Log.error("start_disasm()", e1)
                dialog = DialogWindow()
                dialog.diaglog_user_input()
                return

        try:
            asm = Asm(arch, mode, binary_bytes, endian)
            result = asm.disassemble(int(self.ui.lineEditBaseAddr.text(), 16))
            self.ui.outputAsmHex.setText(result)
            self.ui.outputAsmEscaped.close()
        except Exception as e:
            Log.error("start_disasm()", e)
            dialog = DialogWindow()
            dialog.diaglog_user_input()


class AboutUi(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)
        try:
            with open(ABOUT_TEXT_PATH) as fp:
                Log.info("Open file %s" % ABOUT_TEXT_PATH)
                _info = Helper.get_version()
                self.ui.textBrowserAbout.setHtml(fp.read() % (_info[0], _info[1]))
            if FONT:
                self.init_ui_font(FONT)
        except OSError as e:
            Log.error("Open error! %s" % e)

    def init_ui_font(self, font=FONT):
        self.ui.textBrowserAbout.setFont(font)


class HashUi(QtWidgets.QWidget):
    def __new__(cls, *args, **kwargs):
        """
        Singleton: only one window is allowed.
        """
        if not hasattr(cls, '_instance'):
            cls._instance = super(HashUi, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        Singleton: only once init
        """
        if not hasattr(HashUi, '_init'):
            super().__init__()
            self.init_ui()
            HashUi._init = True

    def init_ui(self):
        self.ui = Ui_HashWindow()
        self.ui.setupUi(self)
        self.openfile = None
        self.ui.openButton.clicked.connect(self.listen_action_open)
        self.ui.hashButton.clicked.connect(self.listen_action_hash)

    def listen_action_open(self):
        self.openfile = QFileDialog.getOpenFileName()[0]
        self.ui.textEdit.setText(self.openfile)
        self.listen_action_hash()

    def listen_action_hash(self):
        """
        Compute hash and crc of file
        :return: null
        """
        if self.openfile:
            self.ui.hashButton.setEnabled(False)
            if os.path.getsize(self.openfile) > 1024 * 1024 * 100:
                self.ui.textBrowser.setText("The file size is large, please waitting...")

            self.value = ''         # multi thread result
            self.thread_num = 0     # thread stop num
            # hash
            self.thread_hash = PreventFastClickThreadSignal(self.openfile, 'hash')
            self.thread_hash._signal.connect(self.set_btn)
            self.thread_hash.start()
            # crc
            self.thread_crc = PreventFastClickThreadSignal(self.openfile, 'crc')
            self.thread_crc._signal.connect(self.set_btn)
            self.thread_crc.start()

    def set_btn(self, value):
        """
        Callback function used to receive the return results of multiple threads
        :param value: hash results
        :return: null
        """
        self.value += value + '<br />'
        self.thread_num += 1
        if self.thread_num == 2:
            self.ui.hashButton.setEnabled(True)
            self.ui.textBrowser.setText(self.value)


class FormatUi(QtWidgets.QWidget):
    def __new__(cls, *args, **kwargs):
        """
        Singleton: only one window is allowed.
        """
        if not hasattr(cls, '_instance'):
            cls._instance = super(FormatUi, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        Singleton: only once init
        """
        if not hasattr(FormatUi, '_init'):
            super().__init__()
            self.init_ui()
            FormatUi._init = True

    def listen_action_format(self):
        _input = self.ui.textEdit.toPlainText()
        _input = _input.replace('\\\"', '\"')
        Log.info("Format input: %s" % _input)
        _is_json = False
        _is_xml = False
        _error_info = ''

        try:
            # handle single quote strings
            _output = self.__log_format_json(json.loads(json.dumps(eval(_input))))
            _is_json = True
        except Exception as e:
            _is_json = False
            _error_info = str(e)

        if not _is_json:
            try:
                _output = self.__log_format_xml(_input.encode('utf-8'))
                _is_xml = True
            except Exception as e:
                _is_xml = False
                _error_info = str(e)

        if _is_json:
            self.highlighter = HighlighterJson(self.ui.textBrowser.document())
            Log.info("Format output: %s" % _output)
            self.ui.textBrowser.setText(_output)
        elif _is_xml:
            self.highlighter = HighlighterXml2(self.ui.textBrowser.document())
            Log.info("Format output: %s" % _output)
            self.ui.textBrowser.setText(_output)
        # Print error
        else:
            self.ui.textBrowser.setText(Helper.font_red(_error_info))
            Log.error(_error_info)

    def listen_action_compress(self):
        _text = self.ui.textBrowser.toPlainText()
        _out = _text.replace(' ', "").replace('\n', "")
        self.ui.textBrowser.setText(_out)

    def listen_action_escape(self):
        _tmp = self.ui.textBrowser.toPlainText()
        _out = _tmp.replace('\"', '\\\"')
        self.ui.textBrowser.setText(_out)

    def listen_action_unescape(self):
        _tmp = self.ui.textBrowser.toPlainText()
        _out = _tmp.replace('\\\"', '\"')
        self.ui.textBrowser.setText(_out)

    def listen_action_unicode(self):
        _tmp = self.ui.textBrowser.toPlainText()
        _out = _tmp.encode("raw_unicode_escape").decode()
        self.ui.textBrowser.setText(_out)

    def listen_action_unicode_decode(self):
        _tmp = self.ui.textBrowser.toPlainText()
        _out = _tmp.encode("utf-8").decode("unicode_escape")
        self.ui.textBrowser.setText(_out)

    def listen_action_convert(self):
        _is_json = False
        _is_xml = False
        _error_info = ''
        _input = self.ui.textEdit.toPlainText()
        Log.info("input: %s" % _input)

        try:
            _output = xmltodict.unparse(json.loads(_input), pretty=True)
            _is_json = True
        except Exception as e:
            _is_json = False
            _error_info = str(e)

        if not _is_json:
            try:
                _output = xmltodict.parse(_input)
                _output = self.__log_format_json(_output)
                _is_xml = True
            except Exception as e:
                _is_xml = False
                _error_info = str(e)

        if _is_json | _is_xml:
            Log.info("Format output: %s" % _output)
            self.ui.textBrowser.setText(str(_output))

        # Print error
        else:
            self.ui.textBrowser.setText(Helper.font_red(_error_info))
            Log.error(_error_info)

    def init_ui(self):
        """
        Init format json ui
        """
        self.ui = Ui_FormatWindow()
        self.ui.setupUi(self)
        self.ui.formatButton.clicked.connect(self.listen_action_format)
        self.ui.compressButton.clicked.connect(self.listen_action_compress)
        self.ui.escapeButton.clicked.connect(self.listen_action_escape)
        self.ui.unescapeButton.clicked.connect(self.listen_action_unescape)
        self.ui.unicodeButton.clicked.connect(self.listen_action_unicode)
        self.ui.unicodeDecodeButton.clicked.connect(self.listen_action_unicode_decode)
        self.ui.covertButton.clicked.connect(self.listen_action_convert)

    def __log_format_json(self, dict):
        """
        Beautify json data
        :param dict: raw data (python dict)
        :return: format json
        """
        return json.dumps(dict, indent=4, ensure_ascii=False)

    def __log_format_xml(self, xml_data):
        """
        Beautify xml data
        :param xml_data:
        :return: format xml
        """
        _root = etree.XML(xml_data)
        return etree.tostring(_root, pretty_print=True).decode('utf-8')


class CommentUi(QtWidgets.QWidget):
    """
    Responsible for comment format such as '# // \n'
    """
    def __new__(cls, *args, **kwargs):
        """
        Singleton: only one window is allowed.
        """
        if not hasattr(cls, '_instance'):
            cls._instance = super(CommentUi, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        Singleton: only once init
        """
        if not hasattr(CommentUi, '_init'):
            super().__init__()
            self.init_ui()
            CommentUi._init = True

    def init_ui(self):
        self.ui = Ui_CommentWindow()
        self.ui.setupUi(self)
        self.ui.formatButton.clicked.connect(self.listen_action_format)
        self.ui.transButton.clicked.connect(self.listen_action_trans)
        self.api_exhusted = False
        self.out = None

    def listen_action_format(self):
        _input = self.ui.textEdit.toPlainText()
        _output = []
        _tmp = string(_input)
        # delete # // /* */ <!-- -->
        _tmp = re.sub(r'/\*|\*/|//|#|<!--|-->', "", _tmp).strip().split('\n\n')
        for period in _tmp:
            my = period.strip().replace('\n', ' ').replace('  ', ' ')
            _output.append(my)

        self.ui.textEditFormat.setText('\n\n'.join(_output).strip())

    def listen_action_trans(self):
        self.listen_action_format()
        _input = self.ui.textEditFormat.toPlainText()
        # TODO: translation
        # select language
        # icon: https://www.flaticon.com/search?author_id=1&style_id=118&type=standard&word=flag
        # lang: https://fanyi-api.baidu.com/doc/21
        if self.ui.toComboBox.currentText() == 'Chinese':
            _to_ = 'zh'
        elif self.ui.toComboBox.currentText() == 'Jpanese':
            _to_ = 'jp'
        elif self.ui.toComboBox.currentText() == 'Korean':
            _to_ = 'kor'
        elif self.ui.toComboBox.currentText() == 'Spanish':
            _to_ = 'spa'
        elif self.ui.toComboBox.currentText() == 'Italian':
            _to_ = 'it'

        # select translator
        try:
            if self.ui.transComboBox.currentText() == 'Baidu':
                _tmp = _input.split('\n\n')
                self.out = ''
                for period in _tmp:
                    self.baidu_trans(period, 'auto', _to_) + '\n\n'
            elif self.ui.transComboBox.currentText() == 'Google':
                pass
            if self.api_exhusted:
                return
            self.ui.transBrowser.setText(self.out)
        except Exception as e:
            Log.error(str(e))
            self.ui.transBrowser.setText(Helper.font_red(str(e)))

    def baidu_trans(self, query, from_, to_):
        """
        为保证翻译质量，请将单次请求长度控制在 6000 bytes以内（汉字约为输入参数 2000 个）
        :param query: 请求翻译query	UTF-8编码
        :param from_: 翻译源语言	可设置为auto
        :param to_: 翻译目标语言	不可设置为auto
        :return: 翻译结果
        """
        appid = '20230309001593277'
        secret = 'uy48JQfdUcbNmMkGZ5At'
        salt = ''.join(random.sample('0123456789', 10))
        sign = self.get_sign(appid, query, salt, secret).hexdigest()

        # Use the standard API provided by the request library instead of format url
        # which will auto format special characters in URL
        GET = False
        url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'appid': appid, 'q': query, 'from': from_, 'to': to_, 'salt': salt, 'sign': sign}
        # Get
        if GET:
            response = requests.get(url, params=payload)
        # Post
        else:
            response = requests.post(url, data=payload, headers=headers)

        if 'error_code' in response.json():
            if response.json()['error_code'] == '54004':
                # TODO: 如果API资源耗尽，则需要计算sign
                self.api_exhusted = True
                self.thread_trans = PreventFastClickThreadSignal(None, 'trans', query, from_, to_)
                self.thread_trans._signal.connect(self.get_ret)
                self.thread_trans.start()
                hint = self.tr("Free API resources have been exhausted, switching to alternate routes is slow! Please be patient and wait...")
                Log.error(hint)
                self.ui.transBrowser.setText(Helper.font_red(hint))
                return ''
                # retval = self.baidu_trans_free(query, from_, to_)
                # return retval

        retval = response.json()['trans_result'][0]['dst']
        self.out += retval
        return retval

    def get_sign(self, appid, q, salt, secret):
        """
        百度翻译API签名计算，来源于 https://fanyi-api.baidu.com/doc/21
        :param appid: 应用ID
        :param q: 请求翻译query	UTF-8编码
        :param salt: 10位随机数
        :param secret: 密钥
        :return: sign
        """
        return hashlib.md5((appid + q + salt + secret).encode())

    def get_ret(self, value):
        self.out += value
        self.out += '\n'
        self.ui.transBrowser.setText(self.out)


class AppCheckerUi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.apk_package = ''
        self.apk_version = ''
        self.apk_minisdk = ''
        self.apk_targetsdk = ''

    def init_ui(self):
        self.ui = Ui_AppcheckerWindow()
        self.ui.setupUi(self)
        self.openfile = None
        self.info_manif = None
        self.editor_code = None
        self.ui.openButton.clicked.connect(self.listen_action_open)
        self.ui.checkButton.clicked.connect(self.listen_action_check)
        self.ui.fullInfoButton.clicked.connect(self.listen_action_full)
        self.activate_link()

    def listen_action_open(self):
        try:
            self.openfile = QFileDialog.getOpenFileName(filter='APK files (*.apk)')[0]
            self.ui.textEdit.setText(self.openfile)
            self._axmlprinter(self.openfile)
            self.listen_action_check()
        except Exception as e:
            pass

    def listen_action_check(self):
        """
        Start checking APK packer informaion
        :return: null
        """
        if self.openfile:
            try:
                _tmp = self.check(self.openfile, 'config/apk_shell.json')
                with open(APKINFO_PATH, encoding='utf-8') as fp:
                    _result = fp.read() % (_tmp['manufacturer'], ', '.join(_tmp['data']), _tmp['url'], _tmp['url'])
                self.ui.textBrowser.setHtml(_result)
                if self.editor_code:
                    self.editor_code.hide()
            except Exception as e:
                self.ui.textBrowser.setText(Helper.font_red(str(e)))
                self.ui.labelHint.setText(Helper.font_red(self.tr("No valid information found!")))
                Log.error(str(e))
            finally:
                self.ui.textBrowser.show()

    def listen_action_full(self):
        """
        Display full manifest.xml
        :return: null
        """
        try:
            #self.highlighter = HighlighterXml(self.ui.textBrowser.document())
            #self.ui.textBrowser.setText(self.info_manif)
            if not self.editor_code:
                self.editor_code = QCodeEditor(SyntaxHighlighter=HighlighterXml2, parent=self.ui.groupBox_2)
            self.editor_code.setPlainText(self.info_manif)
            self.ui.textBrowser.hide()
            self.ui.gridLayout_2.addWidget(self.editor_code, 0, 0, 1, 1)
            self.editor_code.show()
        except Exception as e:
            Log.error(str(e))
            self.ui.textBrowser.setText(Helper.font_red(str(e)))

    def check(self, apk_file, packer):
        """
        Check APK packer infomation
        :param apk_file: android application path
        :param packer: android packer json file path
        :return: packer: information
        """
        _zip = zipfile.ZipFile(apk_file)
        _zip_name = []
        for file in _zip.namelist():
            _zip_name.append(os.path.basename(file))

        with open(packer, 'r', encoding='utf-8') as fp:
            config = json.load(fp)
            for key in config:
                for character in config[key]['data']:
                    if character in _zip_name:
                        return config[key]

    def _axmlprinter(self, apk_file):
        """
        Parse AndroidManifest.xml
        :param apk_file: android application path
        :return: null
        """
        _zip = zipfile.ZipFile(apk_file)
        _ap = AXMLPrinter(_zip.read("AndroidManifest.xml"))
        _buff = _ap.get_xml_obj()
        self.info_manif =_ap.get_xml()

        _manifest = _buff.getElementsByTagName("manifest")
        if _manifest[0].hasAttribute("package"):
            self.apk_package = _manifest[0].getAttribute("package")
        if _manifest[0].hasAttribute("android:versionName"):
            self.apk_version = _manifest[0].getAttribute("android:versionName")

        _uses_sdk = _manifest[0].getElementsByTagName("uses-sdk")
        if _uses_sdk[0].hasAttribute("android:minSdkVersion"):
            self.apk_minisdk = _uses_sdk[0].getAttribute("android:minSdkVersion")
        if _uses_sdk[0].hasAttribute("android:targetSdkVersion"):
            self.apk_targetsdk = _uses_sdk[0].getAttribute("android:targetSdkVersion")

        self.ui.labelPackage.setText(Helper.font_red(self.apk_package))
        self.ui.labelVersion.setText(Helper.font_red(self.apk_version))
        self.ui.labelMiniSDKVersion.setText(Helper.font_red(self.apk_minisdk))
        self.ui.labelSDKVersion.setText(Helper.font_red(self.apk_targetsdk))

    def activate_link(self):
        self.ui.labelGoogle.mousePressEvent = self._clicked_google
        self.ui.labelApkpure.mousePressEvent = self._clicked_apkpure
        self.ui.labelCombo.mousePressEvent = self._clicked_apkcombo

    def _clicked_google(self, unkonwn):
        """
        Click google label to open link
        :return: null
        """
        webbrowser.open('https://play.google.com/store/apps/details?id=%s' % self.apk_package)

    def _clicked_apkpure(self, unkonwn):
        """
        Click apkpure label to open link
        :return: null
        """
        webbrowser.open('https://apkpure.com/a/%s' % self.apk_package)

    def _clicked_apkcombo(self, unkonwn):
        """
        Click apkcombo label to open link
        :return: null
        """
        webbrowser.open('https://apkcombo.com/a/%s' % self.apk_package)


class PeCheckerUi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = Ui_PecheckerWindow()
        self.ui.setupUi(self)
        self.openfile = None
        self.ui.openButton.clicked.connect(self.listen_action_open)
        self.ui.checkButton.clicked.connect(self.listen_action_check)

    def listen_action_open(self):
        self.openfile = QFileDialog.getOpenFileName()[0]
        self.ui.textEdit.setText(self.openfile)
        self.listen_action_check()

    def listen_action_check(self):
        if self.openfile:
            self.ui.checkButton.setEnabled(False)
            if os.path.getsize(self.openfile) > 1024 * 1024:
                self.ui.textBrowser.setText("The file size is large, please waitting...")
            self.thread_check = PreventFastClickThreadSignal(self.openfile, "pecheck")
            self.thread_check._signal.connect(self.set_btn)
            self.thread_check.start()

    def set_btn(self, value):
        self.ui.checkButton.setEnabled(True)
        self.ui.textBrowser.setText(value)


class PreventFastClickThreadSignal(QThread):
    """
    Processing time-consuming operations
    """
    _signal = pyqtSignal(str)

    def __init__(self, path, task, query=None, from_=None, to_=None):
        """
        Constructor
        :param path: file path
        :param task: hash,pecheck,etc.
        """
        super().__init__()
        self.path = path
        self.task = task
        # Translate
        self.query = query
        self.from_ = from_
        self.to_ = to_

    def run(self):
        # Caculate file hash
        if self.task == 'hash':
            code = Code()
            ret = code.get_file_hash_html(self.path)

        # Compute file crc
        if self.task == 'crc':
            code = Code()
            ret = code.get_file_crc32_html(self.path)

        # Check PE file
        elif self.task == 'pecheck':
            ret = self._check(self.path)

        # Translate
        elif self.task == 'trans':
            ret = self._trans(self.query, self.from_, self.to_)

        self._signal.emit(ret)

    def _check(self, path):
        """
        Use peid to check pe file
        :param path: file path
        :return:
        """
        _ret = ''
        try:
            _data = peid.identify_packer(path)
            for i in _data[0]:
                if isinstance(i, list):
                    for j in i:
                        _ret += j + '\n'
                else:
                    _ret += i + '\n'
        except Exception as e:
            _ret = str(e)
        return _ret

    def _trans(self, query, from_, to_):
        """
        这是自己实现的模拟百度翻译Web浏览器的翻译请求，不使用API，而是利用JS计算认证凭据和Cookie
        :param query: 请求翻译query	UTF-8编码
        :param from_: 翻译源语言	可设置为auto
        :param to_: 翻译目标语言	不可设置为auto
        :return: 翻译结果
        """
        # 1. Get cookie
        url_baidu = 'http://passport.baidu.com/v2/api/?login'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        response = requests.get(url=url_baidu, headers=headers)
        cookie = response.headers['Set-Cookie']

        # 2. Get token
        url_baidu_token = 'https://fanyi.baidu.com/'
        headers['Cookie'] = cookie
        response = requests.get(url=url_baidu_token, headers=headers)
        b = re.search(r"token: '.*'", response.text)
        c = re.search(r"'.*'", b.group())
        token = c.group()[1:-1]

        # 3. Get sign
        from baidu_sign import baidu_sign
        sign = baidu_sign(query)

        url = 'https://fanyi.baidu.com/v2transapi'
        headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        payload = {'query': query, 'from': from_, 'to': to_, 'sign': sign, 'token': token}

        retval = 'Unkonwn error.'
        for i in range(20):
            response = requests.post(url=url, data=payload, headers=headers)
            if 'trans_result' in response.json():
                retval = response.json()['trans_result']['data'][0]['dst']
                break
        return retval


class ParamProcess():
    def __init__(self, ui):
        self.ui = ui
        self.param = ()

    def set_param(self, type):
        """
        Processing and filtering user input parameters
        :param type: algorithm
        :return: parameters from user
        """
        if type in ("AES", "DES", "3DES", "RC2"):
            # int, str, int(16,24,32), bytes, bytes, bytes
            index = self.ui.modelComboBox.currentIndex()
            model = index + 1

            padding = self.ui.paddingComboBox.currentText()
            key_length = int(int(self.ui.keySizeComboBox.currentText()[:-3]) / 8)

            # process user select
            key = self.ui.lineEdit.text().encode()
            iv = self.ui.lineEdit_2.text().encode()

            # process user input
            input_data = self.ui.inputData.toPlainText()

            # input format
            index = self.ui.inputComboBox.currentIndex()
            code = Code()
            try:
                if index == 0:
                    input_data = code.hex_to_bytes(input_data)

                elif index == 1:
                    input_data = code.base64_to_bytes(input_data)

                elif index == 2:
                    input_data = input_data.encode("utf-8")

            except Exception as e:
                dialog = DialogWindow()
                dialog.dialog_input_format()
                return

            # padding
            # (pkcs7padding, iso7816, ansix923) -> (pkcs7, iso7816, x923)
            if padding == "pkcs7":
                padding = "pkcs7"
            elif padding == "iso7816":
                padding = "iso7816"
            elif padding == "ansix923":
                padding = "x923"

            if len(key) != key_length:
                # DiaglogInstance.dialog_user_key()
                dialog = DialogWindow()
                dialog.dialog_user_key()
                return

            if model not in (MODE_ECB, MODE_CTR, MODE_CCM, MODE_EAX, MODE_SIV, MODE_GCM, MODE_OCB):
                if type in ("3DES", "RC2") and len(iv) != 8:
                    dialog = DialogWindow()
                    dialog.dialog_user_iv_3des()
                    return

                elif len(iv) != key_length:
                    dialog = DialogWindow()
                    dialog.dialog_user_iv()
                    return

            if input_data == "":
                dialog = DialogWindow()
                dialog.diaglog_user_input()
                return

            self.param = (model, padding, key_length, key, iv, input_data)

    def get_param(self):
        """
        Get the processed parameters
        :return: Parameters after processing
        """
        return self.param


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainUi()
    window.show()
    sys.exit(app.exec_())