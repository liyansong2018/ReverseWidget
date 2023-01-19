#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ui_helper.py    
@Contact :   https://github.com/liyansong2018/ReverseWidget
@License :   (C)Copyright 2021, liyansong
'''

from PyQt5.QtCore import QVariant
from PyQt5.Qt import *


class UiHelper:
    def __init__(self, ui):
        self.ui = ui

    def combobox_item_disable(self, qcom_box,  *args):
        """
        Set qcombobox item to not optional
        :param qcom_box: qcombobox objection
        :param args: index
        :return: null
        """
        for i in range(len(args)):
            qcom_box.setItemData(args[i] - 1, QVariant(0), Qt.UserRole - 1)

    def combobox_item_able(self, qcom_box, *args):
        """
        Set qcombobox item to optional
        :param qcom_box: qcombobox objection
        :param args: index
        :return: null
        """
        for i in range(len(args)):
            qcom_box.setItemData(args[i] - 1, QVariant(1 | 32), Qt.UserRole - 1)

    def groupbox_show(self, groupbox_show, groupbox_all):
        """
        Show the UI of each tab
        :param groupbox_show: need to show
        :param groupbox_all: the entire UI covers all the goupbox that need to be changed
        :return: null
        """
        for i in groupbox_all:
            if i not in groupbox_show:
                i.close()

        for i in groupbox_show:
            i.show()

        self.ui.welcomeGroupBox.close()
        self.ui.formGroupBox.show()


class Helper:
    @staticmethod
    def get_version():
        with open("VERSION") as fp:
            return (fp.readline(), fp.readline())

    @staticmethod
    def font_bold(font):
        return "<b>" + font + "</b>"
