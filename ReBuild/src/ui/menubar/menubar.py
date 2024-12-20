from PySide6.QtCore import Signal, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication
import lzytools.qt_pyside6
from ui_menubar import Ui_Form
from constant import *
import base64
class Menubar(QWidget):
    """选项栏"""
    Option = Signal(name='打开选项')
    PreviousPage  = Signal(name='上一页')
    AutoPlay = Signal(name='自动播放')
    NextPage = Signal(name='下一页')
    Playlist = Signal(name='打开列表')
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # 设置透明背景
        # lzytools.qt_pyside6.set_transparent_background(self)
        lzytools.qt_pyside6.set_transparent_background(self.ui.toolButton_option)
        lzytools.qt_pyside6.set_transparent_background(self.ui.toolButton_previous)
        lzytools.qt_pyside6.set_transparent_background(self.ui.toolButton_autoplay)
        lzytools.qt_pyside6.set_transparent_background(self.ui.toolButton_next)
        lzytools.qt_pyside6.set_transparent_background(self.ui.toolButton_playlist)

        # 绑定信号
        self.ui.toolButton_option.clicked.connect(self.Option.emit)
        self.ui.toolButton_previous.clicked.connect(self.PreviousPage.emit)
        self.ui.toolButton_autoplay.clicked.connect(self.AutoPlay.emit)
        self.ui.toolButton_next.clicked.connect(self.NextPage.emit)
        self.ui.toolButton_playlist.clicked.connect(self.Playlist.emit)

    def _set_icon(self):
        pass




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