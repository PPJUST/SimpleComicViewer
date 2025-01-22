# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_image_infoULuCQG.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(181, 207)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_comic_icon = QLabel(Form)
        self.label_comic_icon.setObjectName(u"label_comic_icon")

        self.horizontalLayout_2.addWidget(self.label_comic_icon)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_2.addWidget(self.label_11)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_comic_filesize = QLabel(Form)
        self.label_comic_filesize.setObjectName(u"label_comic_filesize")

        self.gridLayout.addWidget(self.label_comic_filesize, 2, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_comic_page_count = QLabel(Form)
        self.label_comic_page_count.setObjectName(u"label_comic_page_count")

        self.gridLayout.addWidget(self.label_comic_page_count, 3, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.verticalLayout_comic_filepath = QVBoxLayout()
        self.verticalLayout_comic_filepath.setObjectName(u"verticalLayout_comic_filepath")

        self.gridLayout.addLayout(self.verticalLayout_comic_filepath, 0, 1, 1, 1)

        self.verticalLayout_comic_filename = QVBoxLayout()
        self.verticalLayout_comic_filename.setObjectName(u"verticalLayout_comic_filename")

        self.gridLayout.addLayout(self.verticalLayout_comic_filename, 1, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalLayout.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_image_icon = QLabel(Form)
        self.label_image_icon.setObjectName(u"label_image_icon")

        self.horizontalLayout.addWidget(self.label_image_icon)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout.addWidget(self.label_12)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_page_index = QLabel(Form)
        self.label_page_index.setObjectName(u"label_page_index")

        self.gridLayout_2.addWidget(self.label_page_index, 3, 1, 1, 1)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)

        self.verticalLayout_image_filename = QVBoxLayout()
        self.verticalLayout_image_filename.setObjectName(u"verticalLayout_image_filename")

        self.gridLayout_2.addLayout(self.verticalLayout_image_filename, 0, 1, 1, 1)

        self.label_image_filesize = QLabel(Form)
        self.label_image_filesize.setObjectName(u"label_image_filesize")

        self.gridLayout_2.addWidget(self.label_image_filesize, 1, 1, 1, 1)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_image_size = QLabel(Form)
        self.label_image_size.setObjectName(u"label_image_size")

        self.gridLayout_2.addWidget(self.label_image_size, 2, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_comic_icon.setText(QCoreApplication.translate("Form", u"\u6f2b\u753b\u56fe\u6807", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u6f2b\u753b\u4fe1\u606f", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u5927\u5c0f:", None))
        self.label_comic_filesize.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u540d:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u603b\u9875\u6570:", None))
        self.label_comic_page_count.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u8def\u5f84:", None))
        self.label_image_icon.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u56fe\u6807", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u4fe1\u606f", None))
        self.label_page_index.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u5927\u5c0f:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u9875\u7801:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u5c3a\u5bf8:", None))
        self.label_image_filesize.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u540d:", None))
        self.label_image_size.setText("")
    # retranslateUi

