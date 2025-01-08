# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainWindowsdBDTp.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QScrollArea,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

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
        self.scrollArea_5 = QScrollArea(self.page_single)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.Widget_single = QWidget()
        self.Widget_single.setObjectName(u"Widget_single")
        self.Widget_single.setGeometry(QRect(0, 0, 671, 603))
        self.horizontalLayout_11 = QHBoxLayout(self.Widget_single)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_5.setWidget(self.Widget_single)

        self.horizontalLayout_10.addWidget(self.scrollArea_5)

        self.stackedWidget.addWidget(self.page_single)
        self.page_double_left = QWidget()
        self.page_double_left.setObjectName(u"page_double_left")
        self.horizontalLayout_2 = QHBoxLayout(self.page_double_left)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_double_left)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.Widget_double_left = QWidget()
        self.Widget_double_left.setObjectName(u"Widget_double_left")
        self.Widget_double_left.setGeometry(QRect(0, 0, 671, 603))
        self.horizontalLayout_3 = QHBoxLayout(self.Widget_double_left)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.Widget_double_left)

        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_double_left)
        self.page_double_right = QWidget()
        self.page_double_right.setObjectName(u"page_double_right")
        self.horizontalLayout_4 = QHBoxLayout(self.page_double_right)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.page_double_right)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.Widget_double_right = QWidget()
        self.Widget_double_right.setObjectName(u"Widget_double_right")
        self.Widget_double_right.setGeometry(QRect(0, 0, 671, 603))
        self.horizontalLayout_5 = QHBoxLayout(self.Widget_double_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2.setWidget(self.Widget_double_right)

        self.horizontalLayout_4.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.page_double_right)
        self.page_vertical_scroll = QWidget()
        self.page_vertical_scroll.setObjectName(u"page_vertical_scroll")
        self.horizontalLayout_12 = QHBoxLayout(self.page_vertical_scroll)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_6 = QScrollArea(self.page_vertical_scroll)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.Widget_vertical_scroll = QWidget()
        self.Widget_vertical_scroll.setObjectName(u"Widget_vertical_scroll")
        self.Widget_vertical_scroll.setGeometry(QRect(0, 0, 671, 603))
        self.verticalLayout = QVBoxLayout(self.Widget_vertical_scroll)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_6.setWidget(self.Widget_vertical_scroll)

        self.horizontalLayout_12.addWidget(self.scrollArea_6)

        self.stackedWidget.addWidget(self.page_vertical_scroll)
        self.page_horizontal_scroll_left = QWidget()
        self.page_horizontal_scroll_left.setObjectName(u"page_horizontal_scroll_left")
        self.horizontalLayout_6 = QHBoxLayout(self.page_horizontal_scroll_left)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.page_horizontal_scroll_left)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.Widget_horizontal_scroll_left = QWidget()
        self.Widget_horizontal_scroll_left.setObjectName(u"Widget_horizontal_scroll_left")
        self.Widget_horizontal_scroll_left.setGeometry(QRect(0, 0, 671, 603))
        self.horizontalLayout_7 = QHBoxLayout(self.Widget_horizontal_scroll_left)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3.setWidget(self.Widget_horizontal_scroll_left)

        self.horizontalLayout_6.addWidget(self.scrollArea_3)

        self.stackedWidget.addWidget(self.page_horizontal_scroll_left)
        self.page_horizontal_scroll_right = QWidget()
        self.page_horizontal_scroll_right.setObjectName(u"page_horizontal_scroll_right")
        self.horizontalLayout_8 = QHBoxLayout(self.page_horizontal_scroll_right)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.page_horizontal_scroll_right)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.Widget_horizontal_scroll_right = QWidget()
        self.Widget_horizontal_scroll_right.setObjectName(u"Widget_horizontal_scroll_right")
        self.Widget_horizontal_scroll_right.setGeometry(QRect(0, 0, 671, 603))
        self.horizontalLayout_9 = QHBoxLayout(self.Widget_horizontal_scroll_right)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4.setWidget(self.Widget_horizontal_scroll_right)

        self.horizontalLayout_8.addWidget(self.scrollArea_4)

        self.stackedWidget.addWidget(self.page_horizontal_scroll_right)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SimpleComicViewer", None))
    # retranslateUi

