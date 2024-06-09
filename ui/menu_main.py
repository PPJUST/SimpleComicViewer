# 主窗口的右键菜单
from PySide6.QtCore import Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu, QFileDialog

from module.function_config_get import GetSetting
from module.function_config_reset import ResetSetting


class MenuMain(QMenu):
    """主窗口的右键菜单"""
    signal_open_previous_comic = Signal()
    signal_open_next_comic = Signal()
    signal_open_random_comic = Signal()
    signal_choose_comic_folder = Signal(str)
    signal_choose_comic_archive = Signal(list)
    signal_open_file = Signal()
    signal_remove_queue = Signal()
    signal_delete_file = Signal()
    signal_open_option = Signal()
    signal_open_about = Signal()
    signal_quit = Signal()

    def __init__(self):
        super().__init__()
        self.adjustSize()

        # 设置菜单项
        self.action_random_play = QAction('随机播放')
        self.action_random_play.setCheckable(True)
        self.action_random_play.setChecked(GetSetting.random_play())
        self.action_random_play.triggered.connect(self._set_random_play)
        self.addAction(self.action_random_play)





        self.action_choose_comic_folder = QAction('选择漫画文件夹')
        self.action_choose_comic_folder.triggered.connect(self._choose_comic_folder)
        self.addAction(self.action_choose_comic_folder)

        self.action_choose_comic_archive = QAction('选择漫画压缩包')
        self.action_choose_comic_archive.triggered.connect(self._choose_comic_archive)
        self.addAction(self.action_choose_comic_archive)

        self._line_781 = QAction('----------')
        self._line_781.setEnabled(False)
        self.addAction(self._line_781)

        self.action_open_previous = QAction('打开上一本漫画')
        self.action_open_previous.triggered.connect(self.signal_open_previous_comic.emit)
        self.addAction(self.action_open_previous)

        self.action_open_next = QAction('打开下一本漫画')
        self.action_open_next.triggered.connect(self.signal_open_next_comic.emit)
        self.addAction(self.action_open_next)

        self.action_open_random = QAction('打开随机漫画')
        self.action_open_random.triggered.connect(self.signal_open_random_comic.emit)
        self.addAction(self.action_open_random)

        self._line_354 = QAction('----------')
        self._line_354.setEnabled(False)
        self.addAction(self._line_354)

        self.action_open_file = QAction('打开本地文件')
        self.action_open_file.triggered.connect(self.signal_open_file.emit)
        self.addAction(self.action_open_file)

        self.action_remove_queue = QAction('删除该队列项')
        self.action_remove_queue.triggered.connect(self.signal_remove_queue.emit)
        self.addAction(self.action_remove_queue)

        self.action_delete_file = QAction('删除本地文件')
        self.action_delete_file.triggered.connect(self.signal_delete_file.emit)
        self.addAction(self.action_delete_file)

        self._line_652 = QAction('----------')
        self._line_652.setEnabled(False)
        self.addAction(self._line_652)

        self.action_option = QAction('选项')
        self.action_option.triggered.connect(self.signal_open_option.emit)
        self.addAction(self.action_option)

        self.action_about = QAction('关于')
        self.action_about.triggered.connect(self.signal_open_about.emit)
        self.addAction(self.action_about)

        self.action_quit = QAction('退出')
        self.action_quit.triggered.connect(self.signal_quit.emit)
        self.addAction(self.action_quit)

        # 禁用未完成的菜单项
        self.action_about.setEnabled(False)

    @staticmethod
    def _set_random_play():
        """设置随机播放选项"""
        ResetSetting.random_play(not GetSetting.random_play())



    def _choose_comic_folder(self):
        """选择漫画文件夹"""
        folder = QFileDialog.getExistingDirectory()
        if folder:
            self.signal_choose_comic_folder.emit(folder)

    def _choose_comic_archive(self):
        """选择漫画压缩包"""
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        filter_ = '压缩文件 (*.zip *.rar)'
        file_dialog.setNameFilter(filter_)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            self.signal_choose_comic_archive.emit(selected_files)
