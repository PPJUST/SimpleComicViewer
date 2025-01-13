# 提取和存储漫画信息的类
import os

from module import function_normal, function_comic


class ComicInfo:
    """提取和存储漫画信息的类"""

    def __init__(self, path: str):
        self.path = os.path.normpath(path)  # 文件路径
        self.filetype = ''  # 文件类型
        self.filename = ''  # 文件名（含后缀）
        self.filetitle = ''  # 文件标题（不含后缀）
        self.filesize = 0  # 文件大小，byte
        self.page_count = 0  # 漫画页数
        self.page_list = []  # 漫画内图片路径，如果是压缩包则为压缩包内部路径

        self._guess_filetype()
        self._extract_filename()
        self._count_filesize()
        self._count_page()



    def _count_filesize(self):
        """计算文件大小"""
        if self.filetype == 'folder':
            self.filesize = function_normal.get_folder_size(self.path)
        elif self.filetype == 'archive':
            self.filesize = os.path.getsize(self.path)

    def _count_page(self):
        """统计页数"""
        if self.filetype == 'folder':
            self.page_list = function_comic.extract_folder_images(self.path)
        elif self.filetype == 'archive':
            self.page_list = function_comic.extract_archive_images(self.path)

        self.page_count = len(self.page_list)
