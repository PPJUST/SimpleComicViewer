# 主窗口
import sys
from typing import Union

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMainWindow

from constant import _ICON_ARROW_LEFT, _ICON_ARROW_RIGHT, _MARGIN_MEDIUM, _MARGIN_SMALL, _PLAYLIST_HEIGHT
from module.function_config_get import GetSetting
from module.function_config_reset import ResetSetting
from thread.thread_extract_comic import ThreadExtractComic
from thread.thread_listen_socket import ThreadListenSocket
from thread.thread_wait_time import ThreadWaitTime
from ui.dialog_option import DialogOption
from ui.dialog_wait_animation import DialogWaitAnimation
from ui.label_hover_run_info import LabelHoverRunInfo
from ui.menu_main import MenuMain
from ui.preview_widget.widget_preview_control import WidgetPreviewControl
from ui.ui_src.ui_main import Ui_MainWindow
from ui.widget_change_preview import WidgetChangePreview
from ui.widget_comic_control import WidgetComicControl
from ui.widget_hidden_button import *
from ui.widget_playlist import WidgetPlaylist


class SimpleComicViewer(QMainWindow):
    def __init__(self, args, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)

    def move_playlist_xy(self):
        """移动外部播放列表，使其贴合主窗口右下角"""
        geometry = self.geometry()
        x_lr = geometry.x() + geometry.width()
        y_lr = geometry.y() + geometry.height()

        self.widget_playlist.reset_xy(x_lr + 5, y_lr - _PLAYLIST_HEIGHT)  # +5为大致的程序边框宽度

    def update_app_title(self, path=None):
        """更新程序标题，显示当前路径"""
        self.setWindowTitle(f'SimpleComicViewer - {path}')

    def open_context_menu(self, pos):
        self.menu.exec_(self.mapToGlobal(pos))

    def moveEvent(self, event):
        """重写移动事件，用于保持外部播放列表窗口的相对位置"""
        super().moveEvent(event)
        self.move_playlist_xy()

    def closeEvent(self, event):
        """重写关闭时间，同步关闭外部播放列表窗口"""
        if self.widget_playlist:
            self.widget_playlist.close()
