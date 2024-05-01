# 鼠标经过时自动显示隐藏的button

from PySide6.QtCore import *
from PySide6.QtWidgets import *

from ui.thread_wait_time import ThreadWaitTime
from ui.toolButton_right_click_and_hidden import ToolButtonRightClickAndHidden


class WidgetHiddenButton(QWidget):
    """鼠标经过时自动显示隐藏的button"""
    clicked = Signal()
    rightClicked = Signal()

    def __init__(self, icon, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.button = ToolButtonRightClickAndHidden()
        self.button.set_icon(icon)
        self.layout.addWidget(self.button)
        self.installEventFilter(self.button)
        self.button.raise_()  # 使该label显示在widget之上
        self.button.clicked.connect(self.clicked.emit)
        self.button.rightClicked.connect(self.rightClicked.emit)

        # 固定size，用于setGeometry方法设置相对位置
        self._size = self.sizeHint()

    def reset_xy(self, x: int, y: int):
        """重设坐标轴位置"""
        self.setGeometry(x, y, self._size.width(), self._size.height())

    def set_wait_thread(self, thread: ThreadWaitTime):
        """设置延迟线程"""
        self.button.set_wait_thread(thread)
