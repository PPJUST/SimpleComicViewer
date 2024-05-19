# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_below_control_childHsSjSW.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from ui.toolButton_right_click import ToolButtonRightClick as QToolButton


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(148, 22)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolButton_option = QToolButton(Form)
        self.toolButton_option.setObjectName(u"toolButton_option")

        self.horizontalLayout.addWidget(self.toolButton_option)

        self.toolButton_previous = QToolButton(Form)
        self.toolButton_previous.setObjectName(u"toolButton_previous")

        self.horizontalLayout.addWidget(self.toolButton_previous)

        self.toolButton_autoplay = QToolButton(Form)
        self.toolButton_autoplay.setObjectName(u"toolButton_autoplay")

        self.horizontalLayout.addWidget(self.toolButton_autoplay)

        self.toolButton_next = QToolButton(Form)
        self.toolButton_next.setObjectName(u"toolButton_next")

        self.horizontalLayout.addWidget(self.toolButton_next)

        self.toolButton_playlist = QToolButton(Form)
        self.toolButton_playlist.setObjectName(u"toolButton_playlist")

        self.horizontalLayout.addWidget(self.toolButton_playlist)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.toolButton_option.setText(QCoreApplication.translate("Form", u"...", None))
        self.toolButton_previous.setText(QCoreApplication.translate("Form", u"<", None))
        self.toolButton_autoplay.setText(QCoreApplication.translate("Form", u"||>", None))
        self.toolButton_next.setText(QCoreApplication.translate("Form", u">", None))
        self.toolButton_playlist.setText(QCoreApplication.translate("Form", u"\u2261", None))
    # retranslateUi

