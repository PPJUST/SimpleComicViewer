# 添加右键菜单
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

import common.file_dialog
from components.context_menu.context_menu import ContextMenu
from components.mainWindow._mainWindow_viewer import _MainWindowViewer


class _MainWindowMenu(_MainWindowViewer):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 实例化右键菜单
        self.contextMenu = ContextMenu(self)

        # 连接信号
        self.contextMenu.OpenDir.connect(self.open_dir)
        self.contextMenu.OpenArchive.connect(self.open_archive)
        self.contextMenu.OpenPDF.connect(self.open_pdf)
        #
        # self.contextMenu.PreviousComic.connect(self.previous_comic)
        # self.contextMenu.NextComic.connect(self.next_comic)
        # self.contextMenu.RandomMode.connect(self.random_mode)
        #
        # self.contextMenu.OtherOption.connect(self.open_option)
        self.contextMenu.Quit.connect(self._quit)

        # 绑定右键
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self._show_menu)

    def open_dir(self):
        dirpath = common.file_dialog.select_folder()
        if dirpath:
            self.drop_paths([dirpath])

    def open_archive(self):
        filepath = common.file_dialog.select_archive()
        if filepath:
            self.drop_paths([filepath])

    def open_pdf(self):
        filepath = common.file_dialog.select_pdf()
        if filepath:
            self.drop_paths([filepath])

    def _quit(self):
        sys.exit()

    def _show_menu(self, pos):
        self.contextMenu.exec(self.mapToGlobal(pos))


if __name__ == '__main__':
    app = QApplication()
    ui = _MainWindowViewer()
    ui.show()
    app.exec()
