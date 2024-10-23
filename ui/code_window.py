# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'code_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CodeWindow(object):
    def setupUi(self, CodeWindow):
        CodeWindow.setObjectName("CodeWindow")
        CodeWindow.resize(900, 550)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        CodeWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/pictures/hacker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CodeWindow.setWindowIcon(icon)
        CodeWindow.setStyleSheet("QGroupBox {\n"
"    border: 0px;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(CodeWindow)
        self.gridLayout.setContentsMargins(20, 0, 20, 0)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.outputButtonBox = QtWidgets.QGroupBox(CodeWindow)
        self.outputButtonBox.setTitle("")
        self.outputButtonBox.setObjectName("outputButtonBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.outputButtonBox)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.outputButton_1 = QtWidgets.QPushButton(self.outputButtonBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.outputButton_1.setFont(font)
        self.outputButton_1.setObjectName("outputButton_1")
        self.horizontalLayout_3.addWidget(self.outputButton_1)
        self.outputButton_2 = QtWidgets.QPushButton(self.outputButtonBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.outputButton_2.setFont(font)
        self.outputButton_2.setObjectName("outputButton_2")
        self.horizontalLayout_3.addWidget(self.outputButton_2)
        self.cryptInputBox = QtWidgets.QGroupBox(self.outputButtonBox)
        self.cryptInputBox.setTitle("")
        self.cryptInputBox.setObjectName("cryptInputBox")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.cryptInputBox)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        self.horizontalLayout_3.addWidget(self.cryptInputBox)
        self.gridLayout.addWidget(self.outputButtonBox, 1, 0, 1, 1)
        self.codeOutputGroupBox = QtWidgets.QGroupBox(CodeWindow)
        self.codeOutputGroupBox.setTitle("")
        self.codeOutputGroupBox.setObjectName("codeOutputGroupBox")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.codeOutputGroupBox)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.codeOutput = QtWidgets.QTextBrowser(self.codeOutputGroupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.codeOutput.setFont(font)
        self.codeOutput.setObjectName("codeOutput")
        self.horizontalLayout_19.addWidget(self.codeOutput)
        self.gridLayout.addWidget(self.codeOutputGroupBox, 2, 0, 1, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(CodeWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setStyleSheet("")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.urlTab = QtWidgets.QWidget()
        self.urlTab.setStyleSheet("border: 0px;")
        self.urlTab.setObjectName("urlTab")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.urlTab)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.urlTabText = QtWidgets.QTextEdit(self.urlTab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.urlTabText.setFont(font)
        self.urlTabText.setStyleSheet("")
        self.urlTabText.setLineWidth(0)
        self.urlTabText.setCursorWidth(1)
        self.urlTabText.setObjectName("urlTabText")
        self.horizontalLayout_17.addWidget(self.urlTabText)
        self.tabWidget_2.addTab(self.urlTab, "")
        self.htmlTab = QtWidgets.QWidget()
        self.htmlTab.setStyleSheet("border: 0px;")
        self.htmlTab.setObjectName("htmlTab")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.htmlTab)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.htmlTabText = QtWidgets.QTextEdit(self.htmlTab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.htmlTabText.setFont(font)
        self.htmlTabText.setLineWidth(0)
        self.htmlTabText.setObjectName("htmlTabText")
        self.horizontalLayout_22.addWidget(self.htmlTabText)
        self.tabWidget_2.addTab(self.htmlTab, "")
        self.base64Tab_2 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.base64Tab_2.setFont(font)
        self.base64Tab_2.setStyleSheet("border: 0px;")
        self.base64Tab_2.setObjectName("base64Tab_2")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.base64Tab_2)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.base64TabText = QtWidgets.QTextEdit(self.base64Tab_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.base64TabText.setFont(font)
        self.base64TabText.setObjectName("base64TabText")
        self.horizontalLayout_18.addWidget(self.base64TabText)
        self.tabWidget_2.addTab(self.base64Tab_2, "")
        self.hashTab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.hashTab.setFont(font)
        self.hashTab.setStyleSheet("border: 0px;")
        self.hashTab.setObjectName("hashTab")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.hashTab)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.hashTabText = QtWidgets.QTextEdit(self.hashTab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.hashTabText.setFont(font)
        self.hashTabText.setObjectName("hashTabText")
        self.horizontalLayout_20.addWidget(self.hashTabText)
        self.tabWidget_2.addTab(self.hashTab, "")
        self.unicodeTab = QtWidgets.QWidget()
        self.unicodeTab.setStyleSheet("border: 0px;")
        self.unicodeTab.setObjectName("unicodeTab")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.unicodeTab)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.unicodeTabText = QtWidgets.QTextEdit(self.unicodeTab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.unicodeTabText.setFont(font)
        self.unicodeTabText.setObjectName("unicodeTabText")
        self.horizontalLayout_23.addWidget(self.unicodeTabText)
        self.tabWidget_2.addTab(self.unicodeTab, "")
        self.padTab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.padTab.setFont(font)
        self.padTab.setStyleSheet("border: 0px;")
        self.padTab.setObjectName("padTab")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.padTab)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.padTabText = QtWidgets.QTextEdit(self.padTab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.padTabText.setFont(font)
        self.padTabText.setObjectName("padTabText")
        self.horizontalLayout_24.addWidget(self.padTabText)
        self.tabWidget_2.addTab(self.padTab, "")
        self.gridLayout.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.retranslateUi(CodeWindow)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CodeWindow)

    def retranslateUi(self, CodeWindow):
        _translate = QtCore.QCoreApplication.translate
        CodeWindow.setWindowTitle(_translate("CodeWindow", "Code"))
        self.outputButton_1.setText(_translate("CodeWindow", "Encode"))
        self.outputButton_2.setText(_translate("CodeWindow", "Decode"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.urlTab), _translate("CodeWindow", "URL"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.htmlTab), _translate("CodeWindow", "HTML"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.base64Tab_2), _translate("CodeWindow", "Base64"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.hashTab), _translate("CodeWindow", "Hash"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.unicodeTab), _translate("CodeWindow", "Unicode"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.padTab), _translate("CodeWindow", "Convert"))
