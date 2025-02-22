import lzytools._qt_pyside6
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication

from components.turn_page import TurnPageLeft
from components.turn_page.icon_base64 import _NEXT


class TurnPageRight(TurnPageLeft):
    """翻页"""

    def __init__(self, parent=None):
        super().__init__(parent)

    def _set_icon(self):
        self.ui.toolButton_turn_page.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_NEXT))
        self.ui.toolButton_turn_page.setIconSize(QSize(64, 64))


if __name__ == '__main__':
    app = QApplication()
    ui = TurnPageRight()
    ui.show()
    app.exec()
