# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_sizeNoiTkj.ui'
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
        Form.resize(94, 95)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.toolButton_zoom_out = QToolButton(Form)
        self.toolButton_zoom_out.setObjectName(u"toolButton_zoom_out")

        self.gridLayout.addWidget(self.toolButton_zoom_out, 3, 1, 1, 1)

        self.toolButton_fit_height = QToolButton(Form)
        self.toolButton_fit_height.setObjectName(u"toolButton_fit_height")

        self.gridLayout.addWidget(self.toolButton_fit_height, 1, 1, 1, 1)

        self.toolButton_fit_width = QToolButton(Form)
        self.toolButton_fit_width.setObjectName(u"toolButton_fit_width")

        self.gridLayout.addWidget(self.toolButton_fit_width, 1, 0, 1, 1)

        self.toolButton_rotate_left = QToolButton(Form)
        self.toolButton_rotate_left.setObjectName(u"toolButton_rotate_left")

        self.gridLayout.addWidget(self.toolButton_rotate_left, 4, 0, 1, 1)

        self.toolButton_zoom_in = QToolButton(Form)
        self.toolButton_zoom_in.setObjectName(u"toolButton_zoom_in")

        self.gridLayout.addWidget(self.toolButton_zoom_in, 3, 0, 1, 1)

        self.toolButton_rotate_right = QToolButton(Form)
        self.toolButton_rotate_right.setObjectName(u"toolButton_rotate_right")

        self.gridLayout.addWidget(self.toolButton_rotate_right, 4, 1, 1, 1)

        self.toolButton_fit_widght = QToolButton(Form)
        self.toolButton_fit_widght.setObjectName(u"toolButton_fit_widght")

        self.gridLayout.addWidget(self.toolButton_fit_widght, 0, 0, 1, 1)

        self.toolButton_full_size = QToolButton(Form)
        self.toolButton_full_size.setObjectName(u"toolButton_full_size")

        self.gridLayout.addWidget(self.toolButton_full_size, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5207\u6362\u5927\u5c0f", None))
        self.toolButton_zoom_out.setText(QCoreApplication.translate("Form", u"\u7f29\u5c0f", None))
        self.toolButton_fit_height.setText(QCoreApplication.translate("Form", u"\u9002\u9ad8", None))
        self.toolButton_fit_width.setText(QCoreApplication.translate("Form", u"\u9002\u5bbd", None))
        self.toolButton_rotate_left.setText(QCoreApplication.translate("Form", u"\u5de6\u65cb", None))
        self.toolButton_zoom_in.setText(QCoreApplication.translate("Form", u"\u653e\u5927", None))
        self.toolButton_rotate_right.setText(QCoreApplication.translate("Form", u"\u53f3\u65cb", None))
        self.toolButton_fit_widght.setText(QCoreApplication.translate("Form", u"\u9002\u9875", None))
        self.toolButton_full_size.setText(QCoreApplication.translate("Form", u"\u5b9e\u9645", None))
    # retranslateUi

