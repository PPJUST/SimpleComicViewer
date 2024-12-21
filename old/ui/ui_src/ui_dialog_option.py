# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_optionoRlbdH.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(235, 152)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_skip_solid_color_page = QCheckBox(Dialog)
        self.checkBox_skip_solid_color_page.setObjectName(u"checkBox_skip_solid_color_page")

        self.verticalLayout.addWidget(self.checkBox_skip_solid_color_page)

        self.checkBox_sharpen_image = QCheckBox(Dialog)
        self.checkBox_sharpen_image.setObjectName(u"checkBox_sharpen_image")

        self.verticalLayout.addWidget(self.checkBox_sharpen_image)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.spinBox_preload_pages = QSpinBox(Dialog)
        self.spinBox_preload_pages.setObjectName(u"spinBox_preload_pages")

        self.horizontalLayout_3.addWidget(self.spinBox_preload_pages)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_switch_page_mode = QComboBox(Dialog)
        self.comboBox_switch_page_mode.setObjectName(u"comboBox_switch_page_mode")

        self.horizontalLayout.addWidget(self.comboBox_switch_page_mode)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_confirm = QPushButton(Dialog)
        self.pushButton_confirm.setObjectName(u"pushButton_confirm")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_confirm.sizePolicy().hasHeightForWidth())
        self.pushButton_confirm.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButton_confirm)

        self.pushButton_cancel = QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        sizePolicy.setHeightForWidth(self.pushButton_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButton_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8bbe\u7f6e", None))
        self.checkBox_skip_solid_color_page.setText(QCoreApplication.translate("Dialog", u"\u8df3\u8fc7\u7eaf\u8272\u9875", None))
        self.checkBox_sharpen_image.setText(QCoreApplication.translate("Dialog", u"\u9510\u5316\u56fe\u50cf", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u9884\u8f7d\u56fe\u50cf\u9875\u6570\uff1a", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u8fbe\u5230\u9996\u5c3e\u9875\u65f6", None))
        self.pushButton_confirm.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

