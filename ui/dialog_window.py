#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dialog_window.py    
@Contact :   https://github.com/liyansong2018/ReverseWidget
@License :   (C)Copyright 2021, liyansong

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/25 21:53   liyansong     1.0         None
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui


class DialogWindow(QWidget):
    def __init__(self, parent=None):
        super(DialogWindow, self).__init__(parent)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/resources/pictures/hacker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def msg_information(self, data):
        QMessageBox.information(self, self.tr("Info"), data, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def msg_question(self, data):
        QMessageBox.question(self, self.tr("Question"), data, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def msg_warning(self, data):
        QMessageBox.warning(self, self.tr("Warning"), data, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def msg_critical(self, data):
        QMessageBox.critical(self, self.tr("Critical"), data, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def msg_about(self, data):
        QMessageBox.about(self, self.tr("About"), data)


    def diaglog_about(self):
        info = self.tr("Reverse Widget\nVersion: V1.1\nAuthor: Yansong Li\nPowered by open-source software")
        self.msg_about(info)

    def dialog_user_key(self):
        info = self.tr("Please check secret key or iv")
        self.msg_information(info)

    def dialog_user_iv(self):
        info = self.tr("The length of IV should be equal to the length of the secret key")
        self.msg_information(info)

    def dialog_user_iv_3des(self):
        info = self.tr("The length of IV should be equal to 8 Bytes")
        self.msg_information(info)

    def diaglog_user_input(self):
        info = self.tr("Please check your input data")
        self.msg_information(info)

    def dialog_input_format(self):
        info = self.tr("Please confirm the format of the input data")
        self.msg_information(info)

    def dialog_user_arch(self):
        info = self.tr("Please select architecture")
        self.msg_information(info)

    def dialog_user_mode(self):
        info = self.tr("Please select 16/32/64bit")
        self.msg_information(info)

    def dialog_user_endian(self):
        info = self.tr("Please select endian")
        self.msg_information(info)

# class DiaglogInstance():
#     @classmethod
#     def dialog_user_key(cls):
#         dialog = DialogWindow()
#         info = dialog.tr("Please check secret key or iv")
#         dialog.msg_information(info)
#
#     @classmethod
#     def dialog_user_iv(cls):
#         info = "The length of IV should be equal to the length of the secret key"
#         dialog = DialogWindow()
#         dialog.msg_information(info)
#
#     @classmethod
#     def dialog_user_iv_3des(cls):
#         info = "The length of IV should be equal to 8 Bytes"
#         dialog = DialogWindow()
#         dialog.msg_information(info)
#
#     @classmethod
#     def diaglog_user_input(cls):
#         dialog = DialogWindow()
#         info = dialog.tr("Please check your input data")
#         dialog.msg_information(info)
#
#     @classmethod
#     def dialog_input_format(cls):
#         info = "Please confirm the format of the input data"
#         dialog = DialogWindow()
#         dialog.msg_information(info)
#
#     @classmethod
#     def dialog_user_arch(cls):
#         info = "Please select architecture"
#         dialog = DialogWindow()
#         dialog.msg_information(info)
#
#     @classmethod
#     def dialog_user_mode(cls):
#         info = "Please select 16/32/64bit"
#         dialog = DialogWindow()
#         dialog.msg_information(info)
#
#     @classmethod
#     def dialog_user_endian(cls):
#         info = "Please select endian"
#         dialog = DialogWindow()
#         dialog.msg_information(info)

if __name__ == "__main__":
    # Testcases
    app = QApplication(sys.argv)
    win = DialogWindow()
    win.show()
    sys.exit(app.exec_())