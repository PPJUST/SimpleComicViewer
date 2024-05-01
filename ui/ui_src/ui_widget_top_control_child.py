# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_top_control_childgQKCEl.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(92, 46)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.toolButton_preview_single = QToolButton(Form)
        self.toolButton_preview_single.setObjectName(u"toolButton_preview_single")

        self.gridLayout.addWidget(self.toolButton_preview_single, 0, 0, 1, 1)

        self.toolButton_preview_double = QToolButton(Form)
        self.toolButton_preview_double.setObjectName(u"toolButton_preview_double")

        self.gridLayout.addWidget(self.toolButton_preview_double, 0, 1, 1, 1)

        self.toolButton_preview_v = QToolButton(Form)
        self.toolButton_preview_v.setObjectName(u"toolButton_preview_v")

        self.gridLayout.addWidget(self.toolButton_preview_v, 1, 0, 1, 1)

        self.toolButton_preview_h = QToolButton(Form)
        self.toolButton_preview_h.setObjectName(u"toolButton_preview_h")

        self.gridLayout.addWidget(self.toolButton_preview_h, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.toolButton_preview_single.setText(QCoreApplication.translate("Form", u"1", None))
        self.toolButton_preview_double.setText(QCoreApplication.translate("Form", u"2", None))
        self.toolButton_preview_v.setText(QCoreApplication.translate("Form", u"v", None))
        self.toolButton_preview_h.setText(QCoreApplication.translate("Form", u"h", None))
    # retranslateUi

