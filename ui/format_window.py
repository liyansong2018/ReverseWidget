# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'format_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormatWindow(object):
    def setupUi(self, FormatWindow):
        FormatWindow.setObjectName("FormatWindow")
        FormatWindow.resize(798, 453)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        FormatWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/resources/pictures/hacker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormatWindow.setWindowIcon(icon)
        FormatWindow.setStyleSheet("QGroupBox{\n"
"    border:0px\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(FormatWindow)
        self.gridLayout.setContentsMargins(20, 0, 20, 0)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(12)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(FormatWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 1, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(FormatWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("")
        self.textEdit.setLineWidth(0)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(FormatWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(FormatWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(FormatWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formatButton = QtWidgets.QPushButton(self.groupBox)
        self.formatButton.setMinimumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.formatButton.setFont(font)
        self.formatButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.formatButton.setStyleSheet("")
        self.formatButton.setCheckable(True)
        self.formatButton.setAutoExclusive(True)
        self.formatButton.setAutoDefault(False)
        self.formatButton.setObjectName("formatButton")
        self.horizontalLayout_2.addWidget(self.formatButton)
        self.compressButton = QtWidgets.QPushButton(self.groupBox)
        self.compressButton.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.compressButton.setFont(font)
        self.compressButton.setCheckable(True)
        self.compressButton.setAutoExclusive(True)
        self.compressButton.setObjectName("compressButton")
        self.horizontalLayout_2.addWidget(self.compressButton)
        self.escapeButton = QtWidgets.QPushButton(self.groupBox)
        self.escapeButton.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.escapeButton.setFont(font)
        self.escapeButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.escapeButton.setStyleSheet("")
        self.escapeButton.setCheckable(True)
        self.escapeButton.setAutoExclusive(True)
        self.escapeButton.setObjectName("escapeButton")
        self.horizontalLayout_2.addWidget(self.escapeButton)
        self.unescapeButton = QtWidgets.QPushButton(self.groupBox)
        self.unescapeButton.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.unescapeButton.setFont(font)
        self.unescapeButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.unescapeButton.setStyleSheet("")
        self.unescapeButton.setCheckable(True)
        self.unescapeButton.setAutoExclusive(True)
        self.unescapeButton.setObjectName("unescapeButton")
        self.horizontalLayout_2.addWidget(self.unescapeButton)
        self.unicodeButton = QtWidgets.QPushButton(self.groupBox)
        self.unicodeButton.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.unicodeButton.setFont(font)
        self.unicodeButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.unicodeButton.setStyleSheet("")
        self.unicodeButton.setCheckable(True)
        self.unicodeButton.setAutoExclusive(True)
        self.unicodeButton.setObjectName("unicodeButton")
        self.horizontalLayout_2.addWidget(self.unicodeButton)
        self.unicodeDecodeButton = QtWidgets.QPushButton(self.groupBox)
        self.unicodeDecodeButton.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.unicodeDecodeButton.setFont(font)
        self.unicodeDecodeButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.unicodeDecodeButton.setCheckable(True)
        self.unicodeDecodeButton.setAutoExclusive(True)
        self.unicodeDecodeButton.setObjectName("unicodeDecodeButton")
        self.horizontalLayout_2.addWidget(self.unicodeDecodeButton)
        self.horizontalLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(FormatWindow)
        self.label_2.setMaximumSize(QtCore.QSize(35, 35))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("ui/resources/pictures/xml.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.covertButton = QtWidgets.QPushButton(FormatWindow)
        self.covertButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.covertButton.setFont(font)
        self.covertButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.covertButton.setStyleSheet("QGroupBox{\n"
"    border:0px\n"
"}\n"
"QPushButton{\n"
"    text-align:center;\n"
"    text-decoration:none;\n"
"    background:#ffffff;\n"
"    /*color: #fff;*/\n"
"    color:#000000;\n"
"\n"
"    height: 36px;\n"
"    width: 36px;    \n"
"    \n"
"      border-radius: 18px;\n"
"    /*border:1px solid #dadada;\n"
"    white-space: nowrap;*/\n"
"}\n"
"\n"
"QPushButton::checked,QPushButton::hover{\n"
"    background-image: url(\"ui/resources/pictures/blue_menu.png\");\n"
"    color:#ffffff;\n"
"    font-weight: bold;\n"
"}")
        self.covertButton.setCheckable(True)
        self.covertButton.setAutoExclusive(True)
        self.covertButton.setObjectName("covertButton")
        self.horizontalLayout.addWidget(self.covertButton)
        self.label = QtWidgets.QLabel(FormatWindow)
        self.label.setMaximumSize(QtCore.QSize(35, 35))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui/resources/pictures/json-file.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(FormatWindow)
        QtCore.QMetaObject.connectSlotsByName(FormatWindow)

    def retranslateUi(self, FormatWindow):
        _translate = QtCore.QCoreApplication.translate
        FormatWindow.setWindowTitle(_translate("FormatWindow", "Format Output"))
        self.label_4.setText(_translate("FormatWindow", "Raw"))
        self.label_5.setText(_translate("FormatWindow", "Format"))
        self.formatButton.setText(_translate("FormatWindow", "Format"))
        self.compressButton.setText(_translate("FormatWindow", "Compress"))
        self.escapeButton.setText(_translate("FormatWindow", "Escape"))
        self.unescapeButton.setText(_translate("FormatWindow", "Unescape"))
        self.unicodeButton.setText(_translate("FormatWindow", "Unicode Encode"))
        self.unicodeDecodeButton.setText(_translate("FormatWindow", "Unicode Decode"))
        self.covertButton.setText(_translate("FormatWindow", "<>"))
