# 漫画信息类
import os

import lzytools.archive
import lzytools.file


class ComicInfo:
    """漫画信息类"""
    def __init__(self,path:str):
        """:param path: 漫画文件路径"""
        self.path = os.path.normpath(path)  # 漫画文件路径
        self.filetype = ''  # 文件类型，文件夹folder/压缩文件archive
        self.filename = ''  # 文件名（含文件扩展名）
        self.filetitle = ''  # 文件标题（不含文件扩展名）
        self.filesize = 0  # 文件总大小，byte
        self.filesize_real = 0  # 实际漫画文件大小，byte（针对压缩文件，为其解压后大小）
        self.page_count = 0  # 页数
        self.image_list = []  # 所含图片路径，如果是文件夹，则为本地文件路径；如果是压缩文件，则为压缩文件内部路径

        # 提取信息
        self._get_filetype()  # 提取文件类型
    def _get_filetype(self):
        """提取文件类型"""
        if os.path.isdir(self.path):
            self.filetype = 'folder'
        else:
            if lzytools.archive.is_archive(self.path):
                self.filetype = 'archive'
            else:
                self.filetype = 'unsupported'

    def _get_filename(self):
        """提取文件名和文件标题"""
        self.filename = os.path.basename(self.path)
        if self.filetype == 'folder':
            self.filetitle = self.filename
        elif self.filetype == 'archive':
            self.filetitle = lzytools.archive.get_filetitle(self.filename)

    def _get_filesize(self):
        """提取文件大小"""
        self.filesize = lzytools.file.get_size(self.path)

        if self.filetype == 'archive':
            self.filesize_real = lzytools.archive.get_real_size(self.path)
        else:
            self.filesize_real = self.filesize
