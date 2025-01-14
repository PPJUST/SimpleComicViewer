import lzytools._qt_pyside6
from PySide6.QtCore import Signal
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QApplication

from components.menubar.icon_base64 import _OPTION, _PREVIOUS, _AUTOPLAY_ENABLE, _NEXT, _PLAYLIST, _AUTOPLAY_DISABLE
from components.menubar.ui_menubar import Ui_Form


class Menubar(QWidget):
    """选项栏"""
    Option = Signal(name='打开选项')
    PreviousPage = Signal(name='上一页')
    PreviousRC = Signal(name='上一项（右键点击）')
    AutoPlayStart = Signal(name='开始自动播放')
    AutoPlayStop = Signal(name='停止自动播放')
    NextPage = Signal(name='下一页')
    NextRC = Signal(name='下一项（右键点击）')
    Playlist = Signal(name='打开列表')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._set_icon()
        self._is_autoplay = False

        # 设置透明背景
        lzytools._qt_pyside6.set_transparent_background(self)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_option)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_previous)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_autoplay)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_next)
        lzytools._qt_pyside6.set_transparent_background(self.ui.toolButton_playlist)

        # 绑定信号
        self.ui.toolButton_option.clicked.connect(self.Option.emit)
        self.ui.toolButton_previous.clicked.connect(self.PreviousPage.emit)
        self.ui.toolButton_autoplay.clicked.connect(self.change_autoplay_state)
        self.ui.toolButton_next.clicked.connect(self.NextPage.emit)
        self.ui.toolButton_playlist.clicked.connect(self.Playlist.emit)

        # 绑定右键事件
        self.ui.toolButton_previous.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.toolButton_previous.customContextMenuRequested.connect(self.PreviousRC.emit)
        self.ui.toolButton_next.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.toolButton_next.customContextMenuRequested.connect(self.NextRC.emit)

    def change_autoplay_state(self):
        self._is_autoplay = not self._is_autoplay
        self.reset_autoplay_icon()
        self.emit_signal()

    def reset_autoplay_icon(self):
        if self._is_autoplay:
            self.ui.toolButton_autoplay.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_AUTOPLAY_DISABLE))
        else:
            self.ui.toolButton_autoplay.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_AUTOPLAY_ENABLE))
    def emit_signal(self):
        if self._is_autoplay:
            self.AutoPlayStart.emit()
        else:
            self.AutoPlayStop.emit()
    def _set_icon(self):
        self.ui.toolButton_option.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_OPTION))
        self.ui.toolButton_previous.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_PREVIOUS))
        self.ui.toolButton_autoplay.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_AUTOPLAY_ENABLE))
        self.ui.toolButton_next.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_NEXT))
        self.ui.toolButton_playlist.setIcon(lzytools._qt_pyside6.base64_to_pixmap(_PLAYLIST))

    def enterEvent(self, event):
        super().enterEvent(event)
        self.ui.toolButton_option.setVisible(True)
        self.ui.toolButton_previous.setVisible(True)
        self.ui.toolButton_autoplay.setVisible(True)
        self.ui.toolButton_next.setVisible(True)
        self.ui.toolButton_playlist.setVisible(True)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.ui.toolButton_option.setVisible(False)
        self.ui.toolButton_previous.setVisible(False)
        self.ui.toolButton_autoplay.setVisible(False)
        self.ui.toolButton_next.setVisible(False)
        self.ui.toolButton_playlist.setVisible(False)


if __name__ == "__main__":
    app = QApplication()
    ui = Menubar()
    ui.show()
    app.exec()
