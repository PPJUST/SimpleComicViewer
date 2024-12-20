from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui_change_mode import Ui_Form

class WidgetChangeMode(QWidget):
    """切换浏览模式"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def _set_icon(self):
        self.ui.toolButton_single_page.setIcon()
        self.ui.toolButton_double_page.setIcon()
        self.ui.toolButton_vertical_scroll.setIcon()
        self.ui.toolButton_horizontal_scroll.setIcon()


if __name__=='__main__':
    app = QApplication()
    ui = WidgetChangeMode()
    ui.show()
    app.exec()
