import lzytools.qt_pyside6
from PySide6.QtWidgets import *

from constant import _NEXT2
from turn_page_left import TurnPageLeft


class TurnPageRight(TurnPageLeft):
    """翻页"""

    def __init__(self, parent=None):
        super().__init__(parent)

    def _set_icon(self):
        self.ui.toolButton_turn_page.setIcon(lzytools.qt_pyside6.base64_to_pixmap(_NEXT2))


if __name__ == '__main__':
    app = QApplication()
    ui = TurnPageRight()
    ui.show()
    app.exec()
