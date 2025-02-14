from PySide6.QtCore import *
from PySide6.QtWidgets import *


class ContextMenu(QMenu):
    """右键菜单"""
    OpenDir = Signal(name='打开文件夹')
    OpenArchive = Signal(name='打开压缩文件')
    OpenPDF = Signal(name='打开PDF')

    PreviousComic = Signal(name='上一本漫画')
    NextComic = Signal(name='下一本漫画')
    RandomMode = Signal(name='随机播放')

    OtherOption = Signal(name='更多设置')
    Quit = Signal(name='退出')

    def __init__(self, parent=None):
        super().__init__(parent)

        # 添加按钮
        # 读取类
        action_open_dir = self.addAction('打开文件夹')
        action_open_dir.triggered.connect(self.OpenDir.emit)
        action_open_archive = self.addAction('打开压缩文件')
        action_open_archive.triggered.connect(self.OpenArchive.emit)
        action_open_pdf = self.addAction('打开PDF')
        action_open_pdf.triggered.connect(self.OpenPDF.emit)
        self.addSeparator()

        # 浏览类
        action_previous_comic = self.addAction('上一本漫画')
        action_previous_comic.triggered.connect(self.PreviousComic.emit)
        action_next_comic = self.addAction('下一本漫画')
        action_next_comic.triggered.connect(self.NextComic.emit)
        action_random_mode = self.addAction('随机播放')
        action_random_mode.triggered.connect(self.RandomMode.emit)
        self.addSeparator()

        # 其他
        action_other_option = self.addAction('更多设置')
        action_other_option.triggered.connect(self.OtherOption.emit)
        action_quit = self.addAction('退出')
        action_quit.triggered.connect(self.Quit.emit)
