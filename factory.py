#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   factory.py    
@Contact :   https://github.com/liyansong2018/ReverseWidget
@License :   (C)Copyright 2021, liyansong

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/25 21:52   liyansong     1.0         None
'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Demo(QtWidgets.QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QtWidgets.QPushButton()
        self.label = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)

        self.combo = QtWidgets.QComboBox(self)
        self.combo.currentIndexChanged.connect(self.change_func)

        self.trans = QtCore.QTranslator(self)

        self.v_layout = QtWidgets.QVBoxLayout(self)
        self.v_layout.addWidget(self.combo)
        self.v_layout.addWidget(self.button)
        self.v_layout.addWidget(self.label)

        options = ([('English', ''), ('français', 'eng-fr'), ('中文', 'eng-chs'), ])

        for i, (text, lang) in enumerate(options):
            self.combo.addItem(text)
            self.combo.setItemData(i, lang)
        self.retranslateUi()

    @QtCore.pyqtSlot(int)
    def change_func(self, index):
        data = self.combo.itemData(index)
        if data:
            self.trans.load(data)
            QtWidgets.QApplication.instance().installTranslator(self.trans)
        else:
            QtWidgets.QApplication.instance().removeTranslator(self.trans)

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslateUi()
        super(Demo, self).changeEvent(event)

    def retranslateUi(self):
        self.button.setText(QtWidgets.QApplication.translate('Demo', 'Start'))
        self.label.setText(QtWidgets.QApplication.translate('Demo', 'Hello, World'))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())