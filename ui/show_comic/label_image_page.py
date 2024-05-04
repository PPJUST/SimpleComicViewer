# 显示图片的label，作为单页/双页预览控件的子控件

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

from module import function_comic, function_image
from constant import _MARGIN


class LabelImageList(QLabel):
    """显示图片的label，作为单页/双页预览控件的子控件"""

    def __init__(self, parent=None, ):
        super().__init__(parent)
        # 初始化
        self._comic_path = None  # 漫画文件的路径
        self._comic_filetype = None  # 漫画文件的文件类型
        self._image_path = None  # 需显示图像的文件路径
        self._image_size = None  # 需显示图像的文件宽高
        self._image_pixmap = None  # 需显示图像的pixmap对象
        self._max_size = None  # label的最大大小（父控件的大小）

        if parent:
            self._max_size = QSize(parent.width() - _MARGIN, parent.height() - _MARGIN)
            self.setFixedSize(self._max_size)

    def reset_comic(self, comic_path: str, comic_filetype: str):
        """重设漫画参数
        :param comic_path: 漫画文件的路径
        :param comic_filetype: 漫画文件的类型，archive/folder"""
        self._comic_path = comic_path
        self._comic_filetype = comic_filetype

    def reset_image(self, image_path: str):
        """重设图片参数，并重设label大小"""
        self._image_path = image_path
        self._image_pixmap = None
        self._get_image_size()
        self._change_size()

    def reset_max_size(self, parent):
        """重设大小参数
        :param parent: 父控件"""
        self._max_size = QSize(parent.width() - _MARGIN, parent.height() - _MARGIN)
        self._get_image_size()
        self._change_size()

    def show_image(self):
        """预加载图片"""
        if not self._image_pixmap:
            self.load_pixmap()
        scaled_pixmap = self._image_pixmap.scaled(
            self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setPixmap(scaled_pixmap)

    def load_pixmap(self):
        """读取pixmap"""
        if self._comic_filetype == 'folder':
            self._image_pixmap = QPixmap(self._image_path)
        elif self._comic_filetype == 'archive':
            img_bytes = function_comic.read_image_in_archive(
                archive=self._comic_path, image_path=self._image_path)
            self._image_pixmap = QPixmap()
            self._image_pixmap.loadFromData(img_bytes)

    def hide_image(self):
        """隐藏图片"""
        self.clear()

    def hide_label(self):
        """隐藏label控件"""
        self.hide_image()
        self.setFixedSize(0, 0)

    def _get_image_size(self):
        """获取图片宽高"""
        self._image_size = function_image.get_image_size(self._image_path)

    def _change_size(self):
        """修改label的大小，匹配图像大小"""
        label_rate = self._max_size.width() / self._max_size.height()
        image_rate = self._image_size[0] / self._image_size[1]
        if label_rate > image_rate:  # 以label的高为基准
            label_size = self._calc_size_by_height()
        else:  # 以label的宽为基准
            label_size = self._calc_size_by_width()

        self.setFixedSize(label_size)

    def _calc_size_by_width(self):
        """以label的宽为基准计算新的尺寸"""
        image_width, image_height = self._image_size
        new_height = int(image_height * self._max_size.width() / image_width)
        new_size = QSize(self._max_size.width(), new_height)
        return new_size

    def _calc_size_by_height(self):
        """以label的高为基准计算新的尺寸"""
        image_width, image_height = self._image_size
        new_width = int(image_width * self._max_size.height() / image_height)
        new_size = QSize(new_width, self._max_size.height())
        return new_size
