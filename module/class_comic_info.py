# 提取漫画内容的类
import os

from module import function_normal, function_comic


class ComicInfo:
    """提取漫画内容的类"""

    def __init__(self, path: str):
        self.path = path  # 路径
        self.filename = ''  # 文件名
        self.filetype = ''  # 文件类型
        self.filesize = 0  # 文件大小，byte
        self.page_count = 0  # 漫画页数
        self.page_list = []  # 漫画内图片路径，如果是压缩包则为压缩包内部路径

        self._extract_filename()
        self._guess_filetype()
        self._count_filesize()
        self._count_page()

    def _extract_filename(self):
        """提取文件名"""
        self.filename = os.path.basename(self.path)

    def _guess_filetype(self):
        """确认文件类型"""
        if os.path.isdir(self.path):
            self.filetype = 'folder'
        else:
            if function_normal.is_archive(self.path):
                self.filetype = 'archive'
            else:
                self.filetype = 'unsupported'

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
