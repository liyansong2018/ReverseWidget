#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py    
@Contact :   https://github.com/liyansong2018/ReverseWidget
@License :   (C)Copyright 2021, liyansong

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/25 21:47   liyansong     1.0         None
'''

from ui.main_window import *
from util.crypt import *
from util.log import *
from ui.dialog_window import *
from util.ui_helper import *
from util.map import *
from util.asm import *
from urllib import parse

VERSION = "1.0"

CRYPT = 1
CODE = 2
ASM = 3


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        QtWidgets.QMainWindow.__init__(self)
        self.trans_main_window = QTranslator()
        self.trans_dialog_window = QTranslator()
        self.trans_main = QTranslator()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.formGroupBox.close()
        self.ui.welcomeGroupBox.show()

        self.ui.actionOpen.triggered.connect(self.listen_action_open)
        self.ui.actionChinese.triggered.connect(lambda: self.listen_action_language(self.ui.actionChinese))
        self.ui.actionEnglish.triggered.connect(lambda: self.listen_action_language(self.ui.actionEnglish))
        self.ui.actionAbout.triggered.connect(self.listen_action_about)

        self.ui.cryptButton.clicked.connect(self.init_crypt)
        self.ui.codeButton.clicked.connect(self.init_code)
        self.ui.asmButton.clicked.connect(self.init_asm)

        self.ui.outputButton_1.clicked.connect(lambda: self.listen_button(self.ui.outputButton_1))
        self.ui.outputButton_2.clicked.connect(lambda: self.listen_button(self.ui.outputButton_2))

        # self.ui.tabWidget.currentChanged.connect(self.listen_output)
        self.ui.choiceAlgorithm.currentIndexChanged.connect(self.listen_algorithm)

        self.all_groupbox = [self.ui.cryptGroupBox, self.ui.cryptGroupBox2, self.ui.asmGroupBox, self.ui.inputGroupBox, \
                             self.ui.codeGroupBox, self.ui.asmEndian, self.ui.cryptInputBox, self.ui.outputCryptBox, \
                             self.ui.outputAsmBox, self.ui.codeOutputGroupBox]

        self.openfile = None
        self.function = CRYPT

    def listen_action_open(self):
        self.openfile = QFileDialog.getOpenFileName()[0]

    def listen_action_language(self, language):
        """
        Listen language menu
        :param language: language
        :return: null
        """
        if language.text() == "Chinese":
            self.translate_chinese()
        else:
            self.translate_english()

    def translate_chinese(self):
        self.trans_main_window.load("ui/resources/language/main_window.qm")
        self.trans_dialog_window.load("ui/resources/language/dialog_window.qm")
        self.trans_main.load("ui/resources/language/main.qm")
        _app = QApplication.instance()
        _app.installTranslator(self.trans_main_window)
        _app.installTranslator(self.trans_dialog_window)
        _app.installTranslator(self.trans_main)
        self.ui.retranslateUi(self)

    def translate_english(self):
        _app = QApplication.instance()
        _app.removeTranslator(self.trans_main_window)
        _app.removeTranslator(self.trans_dialog_window)
        _app.removeTranslator(self.trans_main)
        self.ui.retranslateUi(self)

    def listen_action_about(self):
        dialog = DialogWindow()
        dialog.diaglog_about()

    def init_crypt(self):
        self.function = CRYPT
        ui_code = [self.ui.cryptGroupBox, self.ui.cryptGroupBox2, self.ui.inputGroupBox, self.ui.cryptInputBox,
                   self.ui.outputCryptBox]
        ui_helper = UiHelper(self.ui)
        ui_helper.groupbox_show(ui_code, self.all_groupbox)

        self.listen_algorithm()

        self.ui.lineEdit_2.setPlaceholderText("Only support for CBC/CFB/OFB/OPENPGP")
        self.ui.outputButton_1.setText(self.tr("Encrypt"))
        self.ui.outputButton_2.setText(self.tr("Decrypt"))

    def init_code(self):
        self.function = CODE
        ui_code = [self.ui.codeGroupBox, self.ui.codeOutputGroupBox]
        ui_helper = UiHelper(self.ui)
        ui_helper.groupbox_show(ui_code, self.all_groupbox)

        self.ui.outputButton_1.setText(self.tr("Encode | Text-Hash"))
        self.ui.outputButton_2.setText(self.tr("Decode | File-Hash"))

    def init_asm(self):
        self.function = ASM
        ui_code = [self.ui.asmGroupBox, self.ui.inputGroupBox, self.ui.asmEndian, self.ui.outputAsmBox]
        ui_helper = UiHelper(self.ui)
        ui_helper.groupbox_show(ui_code, self.all_groupbox)

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

        self.ui.outputButton_1.setText(self.tr("Assemble"))
        self.ui.outputButton_2.setText(self.tr("Disassemble"))

    def listen_button(self, button):
        """
        Listen ouput Button
        :param button: output_button_1 or output_button_2
        :return: null
        """
        output_choice = button.objectName()
        algorithm_choice = self.ui.choiceAlgorithm.currentText()
        Log.debug("listen_button()", output_choice, algorithm_choice)

        if self.function == CRYPT:
            if output_choice == "outputButton_1":
                self.start_encrypt(algorithm_choice, output_choice)
            else:
                self.start_decrypt(algorithm_choice, output_choice)

        elif self.function == CODE:
            if output_choice == "outputButton_1":
                self.start_encode()
            else:
                self.start_decode()

        elif self.function == ASM:
            if output_choice == "outputButton_1":
                self.start_asm()
            else:
                self.start_disasm()

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

    def listen_arch(self, arch):
        """
        Monitor architecture changes selected by users.
        :param arch: x86, ARM, MIPS, Sparc, PowerPC
        :return: null
        """
        if arch.isChecked():
            global ARCH_BEFORE
            ARCH_BEFORE = arch.text()

            # x86 or ARM64 architecture only supports little endian
            if ARCH_BEFORE == "x86" or (ARCH_BEFORE == "ARM" and MODE_BEFORE == "64bit"):
                self.ui.bigButton.close()
            else:
                self.ui.bigButton.show()

            # 32 bit PowerPC architecture only supports big endian
            if ARCH_BEFORE == "PowerPC" and MODE_BEFORE == "32bit":
                self.ui.littleButton.close()
            else:
                self.ui.littleButton.show()

    def listen_mode(self, mode):
        """
        Monitor mode changes selected by users.
        :param mode: 32bit, 64bit
        :return: null
        """
        if mode.isChecked():
            global MODE_BEFORE
            MODE_BEFORE = mode.text()

            # ARM64 architecture only supports little endian
            if ARCH_BEFORE == "ARM" and MODE_BEFORE == "64bit":
                self.ui.bigButton.close()
            else:
                self.ui.bigButton.show()

            # 32 bit PowerPC architecture only supports big endian
            if ARCH_BEFORE == "PowerPC" and MODE_BEFORE == "32bit":
                self.ui.littleButton.close()
            else:
                self.ui.littleButton.show()

    def listen_endian(self, endian):
        """
        Monitor endian changes selected by users.
        :param endian: little, big endian
        :return: null
        """
        if endian.isChecked():
            global ENDIAN_BEFORE
            ENDIAN_BEFORE = endian.text()

    def start_encrypt(self, algorithm_choice, output_choice):
        Log.debug("start_encrypt", algorithm_choice, output_choice)
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

    def start_decrypt(self, algorithm_choice, output_choice):
        Log.debug("start_decrypt", algorithm_choice, output_choice)
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

    def start_encode(self):
        Log.debug("start_encode()")
        current_index = self.ui.tabWidget_2.currentIndex()
        code = Code()

        # URL Encode
        if current_index == 0:
            try:
                _input = self.ui.urlTabText.toPlainText()
                _input = _input.encode("utf-8")
                output = parse.quote(_input)
                self.ui.codeOutput.setText(output)
            except Exception as e:
                dialog = DialogWindow()
                dialog.diaglog_user_input()
                return

        # Base64 Encode
        elif current_index == 1:
            try:
                _input = self.ui.base64TabText.toPlainText()
                _input = _input.encode("utf-8")
                output = code.bytes_to_base64(_input)
                self.ui.codeOutput.setText(output)
            except Exception as e:
                dialog = DialogWindow()
                dialog.diaglog_user_input()
                return

        # Hash from text: MD5, SHA1, SHA224, SHA256, SHA384, SHA512
        elif current_index == 2:
            try:
                _input = self.ui.hashTabText.toPlainText()
                # 1.data
                if _input != "":
                    _input = _input.encode("utf-8")
                    output = code.get_str_hash(_input)
                    self.ui.codeOutput.setText(output)
            except Exception as e:
                dialog = DialogWindow()
                dialog.diaglog_user_input()
                return

    def start_decode(self):
        Log.debug("start_decode()")
        current_index = self.ui.tabWidget_2.currentIndex()
        code = Code()

        # URL Decode
        if current_index == 0:
            try:
                _input = self.ui.urlTabText.toPlainText()
                output = parse.unquote(_input)
                self.ui.codeOutput.setText(output)
            except Exception as e:
                dialog = DialogWindow()
                dialog.diaglog_user_input()
                return

        # Base64 Decode
        elif current_index == 1:
            try:
                _input = self.ui.base64TabText.toPlainText()
                output = code.base64_to_bytes(_input)
                self.ui.codeOutput.setText(output.decode("utf-8"))
            except Exception as e:
                dialog = DialogWindow()
                dialog.diaglog_user_input()
                return

        # Hash from file: MD5, SHA1, SHA224, SHA256, SHA384, SHA512
        elif current_index == 2:
            try:
                _input = self.openfile
                self.ui.hashTabText.setText(_input)
                output = code.get_file_hash(_input)
                self.ui.codeOutput.setText(output)
            except Exception as e:
                dialog = DialogWindow()
                dialog.diaglog_user_input()
                return

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
            result = asm.assemble()

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
            result = asm.disassemble()
            self.ui.outputAsmHex.setText(result)
            self.ui.outputAsmEscaped.close()
        except Exception as e:
            Log.error("start_disasm()", e)
            dialog = DialogWindow()
            dialog.diaglog_user_input()


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
            if padding == "pkcs7padding":
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