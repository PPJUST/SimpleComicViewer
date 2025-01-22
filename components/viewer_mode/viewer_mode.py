import lzytools._qt_pyside6
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from common.mode_viewer import ModeViewer
from components.viewer_mode.icon_base64 import _DOUBLE_PAGE, _SINGLE_PAGE_RED, _DOUBLE_PAGE_RED, _HORIZONTAL_SCROLL_RED
from components.viewer_mode.icon_base64 import _SINGLE_PAGE, _VERTICAL_SCROLL, _VERTICAL_SCROLL_RED, _HORIZONTAL_SCROLL
from components.viewer_mode.ui_change_mode import Ui_Form


class ViewerMode(QWidget):
    """浏览模式（单页/双页/纵向卷轴/横向卷轴）"""
    SinglePage = Signal(ModeViewer, name='单页')
    DoublePage = Signal(ModeViewer, name='双页')
    VerticalScroll = Signal(ModeViewer, name='纵向卷轴')
    HorizontalScroll = Signal(ModeViewer, name='横向卷轴')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._set_icon()

        # 设置透明背景
        lzytools._qt_pyside6.set_transparent_background(self)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_single_page)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_double_page)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_vertical_scroll)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_horizontal_scroll)

        # 绑定信号
        self.ui.toolButton_single_page.clicked.connect(lambda: self.SinglePage.emit(ModeViewer.SinglePage))
        self.ui.toolButton_single_page.clicked.connect(self.highlight)
        self.ui.toolButton_double_page.clicked.connect(lambda: self.DoublePage.emit(ModeViewer.DoublePage.Left))
        self.ui.toolButton_double_page.clicked.connect(self.highlight)
        self.ui.toolButton_vertical_scroll.clicked.connect(lambda: self.VerticalScroll.emit(ModeViewer.Scroll.Vertical))
        self.ui.toolButton_vertical_scroll.clicked.connect(self.highlight)
        self.ui.toolButton_horizontal_scroll.clicked.connect(
            lambda: self.HorizontalScroll.emit(ModeViewer.Scroll.Horizontal.Left))
        self.ui.toolButton_horizontal_scroll.clicked.connect(self.highlight)

    def highlight(self):
        """高亮目前模式图标"""
        # 重置
        self._set_icon()
        # 高亮
        button = self.sender()
        if button is self.ui.toolButton_single_page:
            self.ui.toolButton_single_page.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_SINGLE_PAGE_RED))
        elif button is self.ui.toolButton_double_page:
            self.ui.toolButton_double_page.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_DOUBLE_PAGE_RED))
        elif button is self.ui.toolButton_vertical_scroll:
            self.ui.toolButton_vertical_scroll.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_VERTICAL_SCROLL_RED))
        elif button is self.ui.toolButton_horizontal_scroll:
            self.ui.toolButton_horizontal_scroll.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_HORIZONTAL_SCROLL_RED))

    def _set_icon(self):
        self.ui.toolButton_single_page.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_SINGLE_PAGE))
        self.ui.toolButton_double_page.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_DOUBLE_PAGE))
        self.ui.toolButton_vertical_scroll.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_VERTICAL_SCROLL))
        self.ui.toolButton_horizontal_scroll.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_HORIZONTAL_SCROLL))

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
    ui = ViewerMode()
    ui.show()
    app.exec()
