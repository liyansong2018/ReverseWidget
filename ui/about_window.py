# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("AboutWindow")
        AboutWindow.resize(515, 367)
        AboutWindow.setMinimumSize(QtCore.QSize(515, 367))
        AboutWindow.setMaximumSize(QtCore.QSize(515, 367))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        AboutWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/resources/pictures/hacker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutWindow.setWindowIcon(icon)
        self.textBrowserAbout = QtWidgets.QTextBrowser(AboutWindow)
        self.textBrowserAbout.setGeometry(QtCore.QRect(-5, -9, 521, 381))
        self.textBrowserAbout.setOpenExternalLinks(True)
        self.textBrowserAbout.setOpenLinks(True)
        self.textBrowserAbout.setObjectName("textBrowserAbout")

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "About"))