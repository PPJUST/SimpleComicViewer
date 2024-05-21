# 支持右键点击信号的button

from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QToolButton


class ToolButtonRightClick(QToolButton):
    """支持右键点击信号的button"""
    rightClicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.setMouseTracking(True)
        self.customContextMenuRequested.connect(self._send_right_clicked_signal)

    def set_icon(self, icon):
        """设置图标"""
        self.setIcon(QIcon(icon))

    def _send_right_clicked_signal(self):
        self.rightClicked.emit()
