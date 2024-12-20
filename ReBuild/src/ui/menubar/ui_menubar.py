# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_menubarsPiiSE.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QToolButton,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(207, 26)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.toolButton_option = QToolButton(Form)
        self.toolButton_option.setObjectName(u"toolButton_option")

        self.gridLayout.addWidget(self.toolButton_option, 0, 0, 1, 1)

        self.toolButton_previous = QToolButton(Form)
        self.toolButton_previous.setObjectName(u"toolButton_previous")

        self.gridLayout.addWidget(self.toolButton_previous, 0, 1, 1, 1)

        self.toolButton_autoplay = QToolButton(Form)
        self.toolButton_autoplay.setObjectName(u"toolButton_autoplay")

        self.gridLayout.addWidget(self.toolButton_autoplay, 0, 2, 1, 1)

        self.toolButton_next = QToolButton(Form)
        self.toolButton_next.setObjectName(u"toolButton_next")

        self.gridLayout.addWidget(self.toolButton_next, 0, 3, 1, 1)

        self.toolButton_playlist = QToolButton(Form)
        self.toolButton_playlist.setObjectName(u"toolButton_playlist")

        self.gridLayout.addWidget(self.toolButton_playlist, 0, 4, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u9009\u9879\u680f", None))
        self.toolButton_option.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.toolButton_previous.setText(QCoreApplication.translate("Form", u"<", None))
        self.toolButton_autoplay.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u64ad\u653e", None))
        self.toolButton_next.setText(QCoreApplication.translate("Form", u">", None))
        self.toolButton_playlist.setText(QCoreApplication.translate("Form", u"\u5217\u8868", None))
    # retranslateUi

