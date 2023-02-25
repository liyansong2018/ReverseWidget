"""Thanks
@ https://doc.qt.io/qtforpython-5/PySide2/QtCore/QRegExp.html
@ https://github.com/pyside/Examples/blob/master/examples/richtext/syntaxhighlighter.py
@ https://srinikom.github.io/pyside-docs/PySide/QtGui/QColor.html
"""

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QRect, QRegExp
from PyQt5.QtWidgets import QWidget, QTextEdit, QTextBrowser
from PyQt5.QtGui import (QColor, QPainter, QFont, QSyntaxHighlighter,
                         QTextFormat, QTextCharFormat)

class HighlighterJava(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(HighlighterJava, self).__init__(parent)

        # keyword
        keywordFormat = QtGui.QTextCharFormat()
        keywordFormat.setForeground(QtCore.Qt.darkBlue)
        keywordFormat.setFontWeight(QtGui.QFont.Bold)

        keywordPatterns = ["\\bchar\\b", "\\bclass\\b", "\\bconst\\b",
                "\\bdouble\\b", "\\benum\\b", "\\bexplicit\\b", "\\bfriend\\b",
                "\\binline\\b", "\\bint\\b", "\\blong\\b", "\\bnamespace\\b",
                "\\boperator\\b", "\\bprivate\\b", "\\bprotected\\b",
                "\\bpublic\\b", "\\bshort\\b", "\\bsignals\\b", "\\bsigned\\b",
                "\\bslots\\b", "\\bstatic\\b", "\\bstruct\\b",
                "\\btemplate\\b", "\\btypedef\\b", "\\btypename\\b",
                "\\bunion\\b", "\\bunsigned\\b", "\\bvirtual\\b", "\\bvoid\\b",
                "\\bvolatile\\b"]

        self.highlightingRules = [(QtCore.QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]

        # class
        classFormat = QtGui.QTextCharFormat()
        classFormat.setFontWeight(QtGui.QFont.Bold)
        classFormat.setForeground(QtCore.Qt.darkMagenta)
        self.highlightingRules.append((QtCore.QRegExp("\\bQ[A-Za-z]+\\b"),
                classFormat))

        # comment1
        singleLineCommentFormat = QtGui.QTextCharFormat()
        singleLineCommentFormat.setForeground(QtCore.Qt.red)
        self.highlightingRules.append((QtCore.QRegExp("//[^\n]*"),
                singleLineCommentFormat))

        self.multiLineCommentFormat = QtGui.QTextCharFormat()
        self.multiLineCommentFormat.setForeground(QtCore.Qt.red)

        # string
        quotationFormat = QtGui.QTextCharFormat()
        quotationFormat.setForeground(QtCore.Qt.darkGreen)
        self.highlightingRules.append((QtCore.QRegExp("\".*\""),
                quotationFormat))

        # function
        functionFormat = QtGui.QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(QtCore.Qt.blue)
        self.highlightingRules.append((QtCore.QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))

        # comment2
        self.commentStartExpression = QtCore.QRegExp("/\\*")
        self.commentEndExpression = QtCore.QRegExp("\\*/")

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QtCore.QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startIndex)

            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength,
                    self.multiLineCommentFormat)
            startIndex = self.commentStartExpression.indexIn(text,
                    startIndex + commentLength)



class HighlighterXml(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(HighlighterXml, self).__init__(parent)

        self.highlightingRules = []

        # QT not support all regexp!!!

        # label1 reg = (?<=<)([^/].*?)(?=\s|>)
        reg = QtCore.QRegExp('(<)([^/].*)(\s|>)')
        reg.setMinimal(True)
        format = QtGui.QTextCharFormat()
        #format.setFontWeight(QtGui.QFont.Bold)
        format.setForeground(QtCore.Qt.blue)
        self.highlightingRules.append((reg, format))

        # label2 reg = "(?<=</)(.*?)(?=\s|>)"
        reg = QtCore.QRegExp('(</)(.*)(>)')
        reg.setMinimal(True)
        format = QtGui.QTextCharFormat()
        #format.setFontWeight(QtGui.QFont.Bold)
        format.setForeground(QtCore.Qt.blue)
        self.highlightingRules.append((reg, format))

        # label3
        reg = QtCore.QRegExp('/>')
        reg.setMinimal(True)
        format = QtGui.QTextCharFormat()
        #format.setFontWeight(QtGui.QFont.Bold)
        format.setForeground(QtCore.Qt.blue)
        self.highlightingRules.append((reg, format))

        # attribute
        reg = QtCore.QRegExp(' .*=')
        reg.setMinimal(True)
        format = QtGui.QTextCharFormat()
        format.setForeground(QtCore.Qt.darkGreen)
        self.highlightingRules.append((reg, format))

        # string reg = \".*?\"
        reg = QtCore.QRegExp('\".*\"')
        reg.setMinimal(True)
        format = QtGui.QTextCharFormat()
        format.setForeground(QtGui.QColor(204, 0, 57))
        self.highlightingRules.append((reg, format))

        # comment
        self.commentStartExpression = QtCore.QRegExp("<!--")
        self.commentEndExpression = QtCore.QRegExp("!-->")

        self.multiLineCommentFormat = QtGui.QTextCharFormat()
        self.multiLineCommentFormat.setForeground(QtCore.Qt.darkRed)

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QtCore.QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startIndex)

            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength,
                    self.multiLineCommentFormat)
            startIndex = self.commentStartExpression.indexIn(text,
                    startIndex + commentLength)


class HighlighterXml2(QtGui.QSyntaxHighlighter):
    '''
    Class for highlighting xml text inherited from QSyntaxHighlighter

    reference:
        http://www.yasinuludag.com/blog/?p=49

    '''

    def __init__(self, parent=None):

        super(HighlighterXml2, self).__init__(parent)

        self.highlightingRules = []

        xmlElementFormat = QTextCharFormat()
        xmlElementFormat.setForeground(QtCore.Qt.blue)  # blue
        self.highlightingRules.append((QRegExp("\\b[A-Za-z0-9_]+(?=[\s/>])"), xmlElementFormat))

        xmlAttributeFormat = QTextCharFormat()
        xmlAttributeFormat.setFontItalic(True)
        xmlAttributeFormat.setForeground(QColor("#177317"))  # green
        self.highlightingRules.append((QRegExp("\\b[A-Za-z0-9_]+(?=\\=)"), xmlAttributeFormat))
        self.highlightingRules.append((QRegExp("="), xmlAttributeFormat))

        self.valueFormat = QTextCharFormat()
        self.valueFormat.setForeground(QColor("#e35e00"))  # orange
        self.valueStartExpression = QRegExp("\"")
        self.valueEndExpression = QRegExp("\"(?=[\s></])")

        singleLineCommentFormat = QTextCharFormat()
        singleLineCommentFormat.setForeground(QColor("#a0a0a4"))  # grey
        self.highlightingRules.append((QRegExp("<!--[^\n]*-->"), singleLineCommentFormat))

        textFormat = QTextCharFormat()
        textFormat.setForeground(QColor("#000000"))  # black
        # (?<=...)  - lookbehind is not supported
        self.highlightingRules.append((QRegExp(">(.+)(?=</)"), textFormat))

        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(QtCore.Qt.blue)  # blue
        keywordFormat.setFontWeight(QFont.Bold)
        keywordPatterns = ["\\b?xml\\b", "/>", ">", "<", "</"]
        self.highlightingRules += [(QRegExp(pattern), keywordFormat)
                                   for pattern in keywordPatterns]

    # VIRTUAL FUNCTION WE OVERRIDE THAT DOES ALL THE COLLORING
    def highlightBlock(self, text):
        # for every pattern
        for pattern, format in self.highlightingRules:
            # Create a regular expression from the retrieved pattern
            expression = QRegExp(pattern)
            # Check what index that expression occurs at with the ENTIRE text
            index = expression.indexIn(text)
            # While the index is greater than 0
            while index >= 0:
                # Get the length of how long the expression is true, set the format from the start to the length with the text format
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                # Set index to where the expression ends in the text
                index = expression.indexIn(text, index + length)

                # HANDLE QUOTATION MARKS NOW.. WE WANT TO START WITH " AND END WITH ".. A THIRD " SHOULD NOT CAUSE THE WORDS INBETWEEN SECOND AND THIRD TO BE COLORED
        self.setCurrentBlockState(0)
        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.valueStartExpression.indexIn(text)
        while startIndex >= 0:
            endIndex = self.valueEndExpression.indexIn(text, startIndex)
            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.valueEndExpression.matchedLength()
            self.setFormat(startIndex, commentLength, self.valueFormat)
            startIndex = self.valueStartExpression.indexIn(text, startIndex + commentLength);


class HighlighterJson(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(HighlighterJson, self).__init__(parent)

        self.highlightingRules = []

        # QT not support all regexp!!!
        # string reg = \".*?\"
        reg = QtCore.QRegExp('\".*\"')
        reg.setMinimal(True)
        format = QtGui.QTextCharFormat()
        format.setForeground(QtGui.QColor("#e35e00"))   # orange
        self.highlightingRules.append((reg, format))

        # key reg = ".*":
        reg = QtCore.QRegExp('".*":')
        reg.setMinimal(True)
        format = QtGui.QTextCharFormat()
        format.setFontWeight(QtGui.QFont.Bold)
        format.setForeground(QtGui.QColor("#000070"))   # blue
        self.highlightingRules.append((reg, format))


    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QtCore.QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)
