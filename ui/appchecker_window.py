# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appchecker_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AppcheckerWindow(object):
    def setupUi(self, AppcheckerWindow):
        AppcheckerWindow.setObjectName("AppcheckerWindow")
        AppcheckerWindow.resize(490, 319)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/resources/pictures/hacker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AppcheckerWindow.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(AppcheckerWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(AppcheckerWindow)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(AppcheckerWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.textBrowser.setFont(font)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 1, 1, 1)
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.checkButton = QtWidgets.QPushButton(AppcheckerWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.checkButton.setFont(font)
        self.checkButton.setStyleSheet("")
        self.checkButton.setObjectName("checkButton")
        self.verticalLayout_1.addWidget(self.checkButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_1.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_1, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.openButton = QtWidgets.QPushButton(AppcheckerWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.openButton.setFont(font)
        self.openButton.setObjectName("openButton")
        self.verticalLayout_3.addWidget(self.openButton)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(AppcheckerWindow)
        QtCore.QMetaObject.connectSlotsByName(AppcheckerWindow)

    def retranslateUi(self, AppcheckerWindow):
        _translate = QtCore.QCoreApplication.translate
        AppcheckerWindow.setWindowTitle(_translate("AppcheckerWindow", "APK Checker"))
        self.checkButton.setText(_translate("AppcheckerWindow", "Check"))
        self.openButton.setText(_translate("AppcheckerWindow", "Open APK"))
