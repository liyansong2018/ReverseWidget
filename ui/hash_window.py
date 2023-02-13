# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hash_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HashWindow(object):
    def setupUi(self, HashWindow):
        HashWindow.setObjectName("HashWindow")
        HashWindow.resize(490, 319)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/resources/pictures/hacker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HashWindow.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(HashWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(HashWindow)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(HashWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.textBrowser.setFont(font)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 1, 1, 1)
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.hashButton = QtWidgets.QPushButton(HashWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.hashButton.setFont(font)
        self.hashButton.setStyleSheet("")
        self.hashButton.setObjectName("hashButton")
        self.verticalLayout_1.addWidget(self.hashButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_1.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_1, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.openButton = QtWidgets.QPushButton(HashWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.openButton.setFont(font)
        self.openButton.setObjectName("openButton")
        self.verticalLayout_3.addWidget(self.openButton)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(HashWindow)
        QtCore.QMetaObject.connectSlotsByName(HashWindow)

    def retranslateUi(self, HashWindow):
        _translate = QtCore.QCoreApplication.translate
        HashWindow.setWindowTitle(_translate("HashWindow", "File Hash"))
        self.hashButton.setText(_translate("HashWindow", "Hash"))
        self.openButton.setText(_translate("HashWindow", "Open File"))
