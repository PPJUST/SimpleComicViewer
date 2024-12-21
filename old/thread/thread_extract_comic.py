# 从路径list中提取符合要求的漫画文件夹和漫画压缩包的子线程

from PySide6.QtCore import QThread, Signal

from module import function_comic


class ThreadExtractComic(QThread):
    """从路径list中提取符合要求的漫画文件夹和漫画压缩包的子线程"""
    signal_comic_list = Signal(list)

    def __init__(self, paths: list, parent=None):
        super().__init__(parent)
        self._paths = paths

    def run(self):
        print('开始')
        comic_list = function_comic.extract_comic(self._paths)
        self.signal_comic_list.emit(comic_list)
        print('结束')
