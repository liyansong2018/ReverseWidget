# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pechecker_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PecheckerWindow(object):
    def setupUi(self, PecheckerWindow):
        PecheckerWindow.setObjectName("PecheckerWindow")
        PecheckerWindow.resize(550, 360)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/resources/pictures/hacker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PecheckerWindow.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(PecheckerWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(PecheckerWindow)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(PecheckerWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.textBrowser.setFont(font)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 1, 1, 1)
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.checkButton = QtWidgets.QPushButton(PecheckerWindow)
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
        self.openButton = QtWidgets.QPushButton(PecheckerWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.openButton.setFont(font)
        self.openButton.setObjectName("openButton")
        self.verticalLayout_3.addWidget(self.openButton)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(PecheckerWindow)
        QtCore.QMetaObject.connectSlotsByName(PecheckerWindow)

    def retranslateUi(self, PecheckerWindow):
        _translate = QtCore.QCoreApplication.translate
        PecheckerWindow.setWindowTitle(_translate("PecheckerWindow", "PE Checker"))
        self.checkButton.setText(_translate("PecheckerWindow", "Check"))
        self.openButton.setText(_translate("PecheckerWindow", "Open PE"))
