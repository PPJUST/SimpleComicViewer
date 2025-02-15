# 图片信息类
import io
import os.path

import lzytools.image
from PIL import Image

from common.comic_info import ComicInfo
from common.comic_type import ComicType


class ImageInfo:
    """图片信息类"""

    def __init__(self, comic_info: ComicInfo, image_path: str):
        self.comic_info = comic_info
        self.comic_type = comic_info.filetype  # 图片所属漫画的类型
        self.path = image_path  # 图片路径，漫画类型为文件夹时，为本地文件路径，漫画类型为压缩文件时，为压缩包内部文件路径
        self.filename = os.path.basename(self.path)  # 图片文件名（含文件扩展名）
        self.filetype = os.path.splitext(self.filename)[1]  # 图片类型，即其文件扩展名
        self.filetitle = os.path.splitext(self.filename)[0]  # 图片文件标题（不含文件扩展名）
        self.filesize = 0  # 图片总大小，byte
        self.size = (0, 0)  # 图片尺寸，格式为(宽, 高)
        self.page_index = 1  # 图片页码

        self.image_bytes = b''  # bytes图片对象

        # 更新参数
        self._read_image()
        self._get_filesize()
        self._get_size()
        self._set_page_index()

    def _set_page_index(self):
        """设置图片对应的页码"""
        self.page_index = self.comic_info.image_list.index(self.path) + 1

    def _read_image(self):
        """读取图片"""
        if self.comic_type == ComicType.Folder:
            self.image_bytes = lzytools.image.read_image(self.path)
        elif self.comic_type == ComicType.Archive:
            self.image_bytes = lzytools.archive.read_image(self.comic_info.path, self.path)

    def _get_filesize(self):
        """获取图片文件大小"""
        self.filesize = len(self.image_bytes)

    def _get_size(self):
        """获取图片尺寸"""
        image = Image.open(io.BytesIO(self.image_bytes))
        self.size = image.size
