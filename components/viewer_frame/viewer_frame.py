import lzytools._qt_pyside6
from PySide6.QtWidgets import *


class ViewerFrame(QScrollArea):
    """预览控件框架"""

    def __init__(self, parent=None,layout='horizontal'):
        super().__init__(parent)
        # 设置外部框架控件
        self.content_widget = QWidget(self)
        self.setWidget(self.content_widget)
        self.setWidgetResizable(True)  # 使内容区域自适应大小
        if layout.lower() == 'horizontal':
            self.layout = QHBoxLayout(self.content_widget)
        elif layout.lower() == 'vertical':
            self.layout = QVBoxLayout(self.content_widget)
        # 设置透明背景
        lzytools._qt_pyside6.set_transparent_background(self)
        lzytools._qt_pyside6.set_transparent_background(self.content_widget)
