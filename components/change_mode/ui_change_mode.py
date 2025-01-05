# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_change_modehCmHlm.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
        Form.resize(94, 51)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.toolButton_single_page = QToolButton(Form)
        self.toolButton_single_page.setObjectName(u"toolButton_single_page")

        self.gridLayout.addWidget(self.toolButton_single_page, 0, 0, 1, 1)

        self.toolButton_double_page = QToolButton(Form)
        self.toolButton_double_page.setObjectName(u"toolButton_double_page")

        self.gridLayout.addWidget(self.toolButton_double_page, 0, 1, 1, 1)

        self.toolButton_vertical_scroll = QToolButton(Form)
        self.toolButton_vertical_scroll.setObjectName(u"toolButton_vertical_scroll")

        self.gridLayout.addWidget(self.toolButton_vertical_scroll, 1, 0, 1, 1)

        self.toolButton_horizontal_scroll = QToolButton(Form)
        self.toolButton_horizontal_scroll.setObjectName(u"toolButton_horizontal_scroll")

        self.gridLayout.addWidget(self.toolButton_horizontal_scroll, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5207\u6362\u6a21\u5f0f", None))
        self.toolButton_single_page.setText(QCoreApplication.translate("Form", u"\u5355\u9875", None))
        self.toolButton_double_page.setText(QCoreApplication.translate("Form", u"\u53cc\u9875", None))
        self.toolButton_vertical_scroll.setText(QCoreApplication.translate("Form", u"\u7eb5\u5377", None))
        self.toolButton_horizontal_scroll.setText(QCoreApplication.translate("Form", u"\u6a2a\u5377", None))
    # retranslateUi

