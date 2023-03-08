#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ui_helper.py    
@Contact :   https://github.com/liyansong2018/ReverseWidget
@License :   (C)Copyright 2021, liyansong
'''

import html
import re
from PyQt5.Qt import *


class UiHelper:
    all_widget = []

    def __init__(self, ui, present_widget=None):
        self.ui = ui
        if present_widget:
            UiHelper.all_widget.append(present_widget)

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


    def widget_show(self, widgets):
        """
        Show target and close unnecessary widgets
        :param widgets: target widgets
        :return: null
        """
        # add widget to all_widget
        # add widget to changeLayout
        for widget in widgets:
            if widget not in UiHelper.all_widget:
                UiHelper.all_widget.append(widget)
                self.ui.changeLayout.addWidget(widget, 0, 0, 1, 1)

        # close other widget
        for widget in UiHelper.all_widget:
            if widget not in widgets:
                widget.close()

        # show widget
        for widget in widgets:
            widget.show()

class Helper:
    @staticmethod
    def get_version():
        with open("VERSION") as fp:
            return (fp.readline(), fp.readline())

    @staticmethod
    def font_bold(font):
        return "<b>" + font + "</b>"

    @classmethod
    def font_red(cls, info):
        """
        Mark the error message in red
        :param info: error
        :return: red font
        """
        return '<font color="red"> %s </font>' % html.escape(info)


class string(str):
    def replace(self, regex, cls):
        self = re.sub(regex, cls, self)
        this = string(self)
        return this
