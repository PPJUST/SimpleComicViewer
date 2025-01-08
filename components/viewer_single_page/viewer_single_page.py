import lzytools._qt_pyside6
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from components.label_image import LabelImage
from components.turn_page.ui_turn_page import Ui_Form
from components.turn_page.icon_base64 import _PREVIOUS


class ViewerFrame(QScrollArea):
    """预览控件框架"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # 设置外部框架控价
        self.content_widget = QWidget(self)
        self.setWidget(self.content_widget)
        self.setWidgetResizable(True)  # 使内容区域自适应大小
        self.layout = QHBoxLayout(self.content_widget)
        # 设置透明背景
        lzytools._qt_pyside6.set_transparent_background(self)
        lzytools._qt_pyside6.set_transparent_background(self.content_widget)

        # 设置图片显示控件
        self.label_image = LabelImage()
        self.layout.addWidget(self.label_image)

