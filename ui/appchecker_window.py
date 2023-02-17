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
        AppcheckerWindow.resize(550, 360)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        AppcheckerWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/resources/pictures/hacker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AppcheckerWindow.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(AppcheckerWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
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
        self.textBrowser = QtWidgets.QTextBrowser(AppcheckerWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.textBrowser.setFont(font)
        self.textBrowser.setMarkdown("")
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.openButton = QtWidgets.QPushButton(AppcheckerWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.openButton.setFont(font)
        self.openButton.setObjectName("openButton")
        self.verticalLayout_3.addWidget(self.openButton)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(AppcheckerWindow)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(AppcheckerWindow)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.labelSDKVersion = QtWidgets.QLabel(AppcheckerWindow)
        self.labelSDKVersion.setText("")
        self.labelSDKVersion.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelSDKVersion.setObjectName("labelSDKVersion")
        self.gridLayout_9.addWidget(self.labelSDKVersion, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(AppcheckerWindow)
        self.label_4.setObjectName("label_4")
        self.gridLayout_9.addWidget(self.label_4, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_3 = QtWidgets.QLabel(AppcheckerWindow)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)
        self.labelMiniSDKVersion = QtWidgets.QLabel(AppcheckerWindow)
        self.labelMiniSDKVersion.setText("")
        self.labelMiniSDKVersion.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelMiniSDKVersion.setObjectName("labelMiniSDKVersion")
        self.gridLayout_8.addWidget(self.labelMiniSDKVersion, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_8, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_7, 1, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_2 = QtWidgets.QLabel(AppcheckerWindow)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(AppcheckerWindow)
        self.label.setMouseTracking(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.labelPackage = QtWidgets.QLabel(AppcheckerWindow)
        self.labelPackage.setText("")
        self.labelPackage.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelPackage.setObjectName("labelPackage")
        self.gridLayout_6.addWidget(self.labelPackage, 0, 1, 1, 1)
        self.labelVersion = QtWidgets.QLabel(AppcheckerWindow)
        self.labelVersion.setText("")
        self.labelVersion.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelVersion.setObjectName("labelVersion")
        self.gridLayout_6.addWidget(self.labelVersion, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelGoogle = QtWidgets.QLabel(AppcheckerWindow)
        self.labelGoogle.setMaximumSize(QtCore.QSize(40, 40))
        self.labelGoogle.setText("")
        self.labelGoogle.setPixmap(QtGui.QPixmap("ui/resources/pictures/google-play.png"))
        self.labelGoogle.setScaledContents(True)
        self.labelGoogle.setOpenExternalLinks(True)
        self.labelGoogle.setObjectName("labelGoogle")
        self.horizontalLayout_2.addWidget(self.labelGoogle)
        self.labelApkpure = QtWidgets.QLabel(AppcheckerWindow)
        self.labelApkpure.setMaximumSize(QtCore.QSize(40, 40))
        self.labelApkpure.setText("")
        self.labelApkpure.setPixmap(QtGui.QPixmap("ui/resources/pictures/apkpure.png"))
        self.labelApkpure.setScaledContents(True)
        self.labelApkpure.setOpenExternalLinks(True)
        self.labelApkpure.setObjectName("labelApkpure")
        self.horizontalLayout_2.addWidget(self.labelApkpure)
        self.labelCombo = QtWidgets.QLabel(AppcheckerWindow)
        self.labelCombo.setMaximumSize(QtCore.QSize(40, 40))
        self.labelCombo.setText("")
        self.labelCombo.setPixmap(QtGui.QPixmap("ui/resources/pictures/apkcombo.png"))
        self.labelCombo.setScaledContents(True)
        self.labelCombo.setOpenExternalLinks(True)
        self.labelCombo.setObjectName("labelCombo")
        self.horizontalLayout_2.addWidget(self.labelCombo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.fullInfoButton = QtWidgets.QPushButton(AppcheckerWindow)
        self.fullInfoButton.setObjectName("fullInfoButton")
        self.verticalLayout.addWidget(self.fullInfoButton)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 2, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 2, 0, 1, 1)

        self.retranslateUi(AppcheckerWindow)
        QtCore.QMetaObject.connectSlotsByName(AppcheckerWindow)

    def retranslateUi(self, AppcheckerWindow):
        _translate = QtCore.QCoreApplication.translate
        AppcheckerWindow.setWindowTitle(_translate("AppcheckerWindow", "APK Checker"))
        self.checkButton.setText(_translate("AppcheckerWindow", "Check"))
        self.textBrowser.setHtml(_translate("AppcheckerWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\',\'微软雅黑\'; font-size:9.07563pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'微软雅黑\'; font-size:9.07563pt;\"><br /></p></body></html>"))
        self.openButton.setText(_translate("AppcheckerWindow", "Open APK"))
        self.textEdit.setHtml(_translate("AppcheckerWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\',\'微软雅黑\'; font-size:9.07563pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.07563pt;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("AppcheckerWindow", "Target SDK Version"))
        self.label_3.setText(_translate("AppcheckerWindow", "Min SDK Version"))
        self.label_2.setText(_translate("AppcheckerWindow", "Version name"))
        self.label.setText(_translate("AppcheckerWindow", "Package name"))
        self.fullInfoButton.setText(_translate("AppcheckerWindow", "Full APK Information"))
