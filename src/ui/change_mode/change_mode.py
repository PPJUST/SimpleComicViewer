import lzytools.qt_pyside6
from PySide6.QtCore import *
from PySide6.QtWidgets import *

from constant import _SINGLE_PAGE, _DOUBLE_PAGE, _VERTICAL_SCROLL, _HORIZONTAL_SCROLL, _HORIZONTAL_SCROLL_RED, \
    _VERTICAL_SCROLL_RED, _DOUBLE_PAGE_RED, _SINGLE_PAGE_RED
from .ui_change_mode import Ui_Form


class ChangeMode(QWidget):
    """切换浏览模式"""
    SinglePage = Signal(name='单页')
    DoublePage = Signal(name='双页')
    VerticalScroll = Signal(name='纵向卷轴')
    HorizontalScroll = Signal(name='横向卷轴')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._set_icon()

        # 设置透明背景
        lzytools.qt_pyside6.set_transparent_background(self)
        lzytools.qt_pyside6.set_transparent_background(self.ui.toolButton_single_page)
        lzytools.qt_pyside6.set_transparent_background(self.ui.toolButton_double_page)
        lzytools.qt_pyside6.set_transparent_background(self.ui.toolButton_vertical_scroll)
        lzytools.qt_pyside6.set_transparent_background(self.ui.toolButton_horizontal_scroll)

        # 绑定信号
        self.ui.toolButton_single_page.clicked.connect(self.SinglePage.emit)
        self.ui.toolButton_single_page.clicked.connect(self.highlight)
        self.ui.toolButton_double_page.clicked.connect(self.DoublePage.emit)
        self.ui.toolButton_double_page.clicked.connect(self.highlight)
        self.ui.toolButton_vertical_scroll.clicked.connect(self.VerticalScroll.emit)
        self.ui.toolButton_vertical_scroll.clicked.connect(self.highlight)
        self.ui.toolButton_horizontal_scroll.clicked.connect(self.HorizontalScroll.emit)
        self.ui.toolButton_horizontal_scroll.clicked.connect(self.highlight)

    def highlight(self):
        """高亮目前模式图标"""
        # 重置
        self._set_icon()
        # 高亮
        button = self.sender()
        if button is self.ui.toolButton_single_page:
            self.ui.toolButton_single_page.setIcon(lzytools.qt_pyside6.base64_to_pixmap(_SINGLE_PAGE_RED))
        elif button is self.ui.toolButton_double_page:
            self.ui.toolButton_double_page.setIcon(lzytools.qt_pyside6.base64_to_pixmap(_DOUBLE_PAGE_RED))
        elif button is self.ui.toolButton_vertical_scroll:
            self.ui.toolButton_vertical_scroll.setIcon(lzytools.qt_pyside6.base64_to_pixmap(_VERTICAL_SCROLL_RED))
        elif button is self.ui.toolButton_horizontal_scroll:
            self.ui.toolButton_horizontal_scroll.setIcon(lzytools.qt_pyside6.base64_to_pixmap(_HORIZONTAL_SCROLL_RED))

    def _set_icon(self):
        self.ui.toolButton_single_page.setIcon(lzytools.qt_pyside6.base64_to_pixmap(_SINGLE_PAGE))
        self.ui.toolButton_double_page.setIcon(lzytools.qt_pyside6.base64_to_pixmap(_DOUBLE_PAGE))
        self.ui.toolButton_vertical_scroll.setIcon(lzytools.qt_pyside6.base64_to_pixmap(_VERTICAL_SCROLL))
        self.ui.toolButton_horizontal_scroll.setIcon(lzytools.qt_pyside6.base64_to_pixmap(_HORIZONTAL_SCROLL))

    def enterEvent(self, event):
        super().enterEvent(event)
        self.ui.toolButton_single_page.setVisible(True)
        self.ui.toolButton_double_page.setVisible(True)
        self.ui.toolButton_vertical_scroll.setVisible(True)
        self.ui.toolButton_horizontal_scroll.setVisible(True)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.ui.toolButton_single_page.setVisible(False)
        self.ui.toolButton_double_page.setVisible(False)
        self.ui.toolButton_vertical_scroll.setVisible(False)
        self.ui.toolButton_horizontal_scroll.setVisible(False)


if __name__ == '__main__':
    app = QApplication()
    ui = ChangeMode()
    ui.show()
    app.exec()
