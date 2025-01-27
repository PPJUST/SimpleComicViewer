import lzytools._qt_pyside6
from PySide6.QtCore import Signal, QSize, Qt
from PySide6.QtWidgets import QWidget, QApplication

from components.turn_page.icon_base64 import _PREVIOUS
from components.turn_page.ui_turn_page import Ui_Form


class TurnPageLeft(QWidget):
    """翻页"""
    TurnPage = Signal(name='翻页')
    TurnPageRC = Signal(name='翻页（右键点击）')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._set_icon()
        self.resize(64, 64)

        # 设置透明背景
        lzytools._qt_pyside6.set_transparent_background(self)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_turn_page)

        # 绑定信号
        self.ui.toolButton_turn_page.clicked.connect(self.TurnPage.emit)

        # 绑定右键事件
        self.ui.toolButton_turn_page.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.toolButton_turn_page.customContextMenuRequested.connect(self.TurnPageRC.emit)

    def _set_icon(self):
        self.ui.toolButton_turn_page.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_PREVIOUS))
        self.ui.toolButton_turn_page.setIconSize(QSize(64, 64))

    def enterEvent(self, event):
        super().enterEvent(event)
        self.ui.toolButton_turn_page.setVisible(True)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.ui.toolButton_turn_page.setVisible(False)


if __name__ == '__main__':
    app = QApplication()
    ui = TurnPageLeft()
    ui.show()
    app.exec()
