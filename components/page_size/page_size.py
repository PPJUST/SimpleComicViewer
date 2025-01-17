import lzytools._qt_pyside6
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from components.page_size.icon_base64 import _FIT_HEIGHT, _FIT_WIDTH, _FIT_WIDGET, _ROTATE_LEFT, _ROTATE_RIGHT
from components.page_size.icon_base64 import _FIT_HEIGHT_RED, _FIT_WIDTH_RED, _FIT_WIDGET_RED, _FULL_SIZE_RED
from components.page_size.icon_base64 import _FULL_SIZE, _ZOOM_IN, _ZOOM_OUT
from components.page_size.ui_page_size import Ui_Form


class PageSize(QWidget):
    """页面大小设置"""
    FitHeight = Signal(name='适应高度')
    FitWidth = Signal(name='适应宽度')
    FitWidget = Signal(name='适应页面')
    FullSize = Signal(name='实际大小')
    RotateLeft = Signal(name='左旋转')
    RotateRight = Signal(name='右旋转')
    ZoomIn = Signal(name='放大')
    ZoomOut = Signal(name='缩小')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._set_icon()

        # 设置透明背景
        # lzytools._qt_pyside6.set_transparent_background(self)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_fit_height)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_fit_width)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_fit_widght)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_rotate_left)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_rotate_right)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_full_size)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_zoom_in)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_zoom_out)

        # 绑定信号
        self.ui.toolButton_fit_height.clicked.connect(self.FitHeight.emit)
        self.ui.toolButton_fit_height.clicked.connect(self.highlight)
        self.ui.toolButton_fit_width.clicked.connect(self.FitWidth.emit)
        self.ui.toolButton_fit_width.clicked.connect(self.highlight)
        self.ui.toolButton_fit_widght.clicked.connect(self.FitWidget.emit)
        self.ui.toolButton_fit_widght.clicked.connect(self.highlight)
        self.ui.toolButton_full_size.clicked.connect(self.FullSize.emit)
        self.ui.toolButton_full_size.clicked.connect(self.highlight)
        self.ui.toolButton_rotate_left.clicked.connect(self.RotateLeft.emit)
        self.ui.toolButton_rotate_left.clicked.connect(self.highlight)
        self.ui.toolButton_rotate_right.clicked.connect(self.RotateRight.emit)
        self.ui.toolButton_rotate_right.clicked.connect(self.highlight)
        self.ui.toolButton_zoom_in.clicked.connect(self.ZoomIn.emit)
        self.ui.toolButton_zoom_in.clicked.connect(self.highlight)
        self.ui.toolButton_zoom_out.clicked.connect(self.ZoomOut.emit)
        self.ui.toolButton_zoom_out.clicked.connect(self.highlight)

    def highlight(self):
        """高亮目前模式图标"""
        # 重置
        self._set_icon()
        # 高亮
        button = self.sender()
        if button is self.ui.toolButton_fit_height:
            self.ui.toolButton_fit_height.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_FIT_HEIGHT_RED))
        elif button is self.ui.toolButton_fit_width:
            self.ui.toolButton_fit_width.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_FIT_WIDTH_RED))
        elif button is self.ui.toolButton_fit_widght:
            self.ui.toolButton_fit_widght.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_FIT_WIDGET_RED))
        elif button is self.ui.toolButton_full_size:
            self.ui.toolButton_full_size.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_FULL_SIZE_RED))
        else:
            self._set_icon()

    def _set_icon(self):
        self.ui.toolButton_fit_height.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_FIT_HEIGHT))
        self.ui.toolButton_fit_width.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_FIT_WIDTH))
        self.ui.toolButton_fit_widght.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_FIT_WIDGET))
        self.ui.toolButton_full_size.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_FULL_SIZE))
        self.ui.toolButton_rotate_left.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_ROTATE_LEFT))
        self.ui.toolButton_rotate_right.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_ROTATE_RIGHT))
        self.ui.toolButton_zoom_in.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_ZOOM_IN))
        self.ui.toolButton_zoom_out.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_ZOOM_OUT))

    def enterEvent(self, event):
        super().enterEvent(event)
        self.ui.toolButton_fit_height.setVisible(True)
        self.ui.toolButton_fit_width.setVisible(True)
        self.ui.toolButton_fit_widght.setVisible(True)
        self.ui.toolButton_rotate_left.setVisible(True)
        self.ui.toolButton_rotate_right.setVisible(True)
        self.ui.toolButton_full_size.setVisible(True)
        self.ui.toolButton_zoom_in.setVisible(True)
        self.ui.toolButton_zoom_out.setVisible(True)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.ui.toolButton_fit_height.setVisible(False)
        self.ui.toolButton_fit_width.setVisible(False)
        self.ui.toolButton_fit_widght.setVisible(False)
        self.ui.toolButton_rotate_left.setVisible(False)
        self.ui.toolButton_rotate_right.setVisible(False)
        self.ui.toolButton_full_size.setVisible(False)
        self.ui.toolButton_zoom_in.setVisible(False)
        self.ui.toolButton_zoom_out.setVisible(False)


if __name__ == '__main__':
    app = QApplication()
    ui = PageSize()
    ui.show()
    app.exec()
