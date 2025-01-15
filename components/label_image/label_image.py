import time

from PySide6.QtCore import QSize
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from common.size_mode import PageSizeMode


class LabelImage(QLabel):
    """自适应大小显示图片"""

    def __init__(self, image_path: str = None):
        """:param image_path: str，图片路径"""
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.pixmap = None
        if image_path:
            self.pixmap = QPixmap(image_path)

    def set_image(self, image_path: str = None):
        """设置图片"""
        self.pixmap = QPixmap(image_path)
        self._image_size_auto()

    def update_image_size(self, size_mode:PageSizeMode, arg=None):
        """更新图片尺寸"""
        if size_mode is PageSizeMode.FitPage:
            self._image_size_fit_page(arg)
        elif size_mode is PageSizeMode.FitHieght:
            self._image_size_fit_height(arg)
        elif size_mode is PageSizeMode.FitWidth:
            self._image_size_fit_width(arg)
        elif size_mode is PageSizeMode.FullSize:
            self._image_size_full_size()


    def _image_size_auto(self):
        """更新图片尺寸，适合其自身尺寸"""
        if self.pixmap and not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)

    def _image_size_fit_page(self,qsize:QSize):
        """更新图片尺寸，适合页面框架尺寸"""
        if self.pixmap and not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(qsize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)

    def _image_size_fit_height(self,height:int):
        """更新图片尺寸，适合高度"""
        # 备忘录 需要考虑滑动条的宽度
        if self.pixmap and not self.pixmap.isNull():
            calc_width = int(height / self.pixmap.height() *self.pixmap.width())
            size = QSize(calc_width, height)
            scaled_pixmap = self.pixmap.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)
    def _image_size_fit_width(self,width:int):
        """更新图片尺寸，适合宽度"""
        # 备忘录 需要考虑滑动条的宽度
        if self.pixmap and not self.pixmap.isNull():
            calc_height = int(width / self.pixmap.width() *self.pixmap.height())-1
            size = QSize(width, calc_height)
            scaled_pixmap = self.pixmap.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)

    def _image_size_full_size(self):
        """更新图片尺寸，实际大小"""
        if self.pixmap and not self.pixmap.isNull():
            self.setPixmap(self.pixmap)
