# 鼠标经过时自动显示并延迟隐藏的button

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout

from constant import _BUTTON_LARGE
from ui.toolButton_right_click_and_hidden import ToolButtonRightClickAndHidden


class WidgetHiddenButton(QWidget):
    """鼠标经过时自动显示并延迟隐藏的button"""
    clicked = Signal()
    rightClicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        # 设置ui
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.button = ToolButtonRightClickAndHidden()
        self.button.setFixedSize(_BUTTON_LARGE, _BUTTON_LARGE)
        self.layout.addWidget(self.button)
        self.installEventFilter(self.button)
        self.button.raise_()  # 使该label显示在widget之上
        self.button.clicked.connect(self.clicked.emit)
        self.button.rightClicked.connect(self.rightClicked.emit)

    def set_icon(self, icon):
        """设置图标"""
        self.button.set_icon(icon)

    def reset_xy(self, x: int, y: int):
        """重设坐标轴位置"""
        self.setGeometry(x, y, _BUTTON_LARGE, _BUTTON_LARGE)
