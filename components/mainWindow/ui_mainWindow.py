# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainWindowtARXXh.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QSizePolicy,
    QStackedWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(673, 605)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_single = QWidget()
        self.page_single.setObjectName(u"page_single")
        self.horizontalLayout_10 = QHBoxLayout(self.page_single)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.page_single)
        self.page_double_left = QWidget()
        self.page_double_left.setObjectName(u"page_double_left")
        self.horizontalLayout_2 = QHBoxLayout(self.page_double_left)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.page_double_left)
        self.page_double_right = QWidget()
        self.page_double_right.setObjectName(u"page_double_right")
        self.horizontalLayout_4 = QHBoxLayout(self.page_double_right)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.page_double_right)
        self.page_vertical_scroll = QWidget()
        self.page_vertical_scroll.setObjectName(u"page_vertical_scroll")
        self.horizontalLayout_12 = QHBoxLayout(self.page_vertical_scroll)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.page_vertical_scroll)
        self.page_horizontal_scroll_left = QWidget()
        self.page_horizontal_scroll_left.setObjectName(u"page_horizontal_scroll_left")
        self.horizontalLayout_6 = QHBoxLayout(self.page_horizontal_scroll_left)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.page_horizontal_scroll_left)
        self.page_horizontal_scroll_right = QWidget()
        self.page_horizontal_scroll_right.setObjectName(u"page_horizontal_scroll_right")
        self.horizontalLayout_8 = QHBoxLayout(self.page_horizontal_scroll_right)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.page_horizontal_scroll_right)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SimpleComicViewer", None))
    # retranslateUi

