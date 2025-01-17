from PySide6.QtCore import QSize
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from common.size_mode import PageSizeMode


class LabelImage(QLabel):
    """自适应大小显示图片"""
    ZOOM_WIDTH = 50

    def __init__(self, image_path: str = None):
        """:param image_path: str，图片路径"""
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.pixmap_original = None
        if image_path:
            self.pixmap_original = QPixmap(image_path)

    def set_image(self, image_path: str = None):
        """设置图片"""
        self.pixmap_original = QPixmap(image_path)
        self._image_size_auto()

    def zoom_in(self):
        """放大固定尺寸（奕宽度为基准放大）"""
        if self.pixmap_original and not self.pixmap_original.isNull():
            current_width, current_height = self.pixmap().width(), self.pixmap().height()
            zoom_width = current_width + self.ZOOM_WIDTH
            zoom_height = int(zoom_width / current_width * current_height)
            size = QSize(zoom_width, zoom_height)
            scaled_pixmap = self.pixmap_original.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)

    def zoom_out(self):
        """缩小固定尺寸（奕宽度为基准缩小）"""
        if self.pixmap_original and not self.pixmap_original.isNull():
            current_width, current_height = self.pixmap().width(), self.pixmap().height()
            zoom_width = current_width - self.ZOOM_WIDTH
            zoom_height = int(zoom_width / current_width * current_height)
            if zoom_width <= 0 or zoom_height <= 0:  # 防止负数尺寸
                zoom_width, zoom_height = 1, 1
            size = QSize(zoom_width, zoom_height)
            scaled_pixmap = self.pixmap_original.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)

    def rotate_left(self):
        """向左旋转图片"""
        self._rotate(-90)

    def rotate_right(self):
        """向右旋转图片"""
        self._rotate(90)

    def update_image_size(self, size_mode: PageSizeMode, arg=None):
        """更新图片尺寸"""
        if size_mode is PageSizeMode.Fixed:
            self._image_size_keep()
        if size_mode is PageSizeMode.FitPage:
            self._image_size_fit_page(arg)
        elif size_mode is PageSizeMode.FitHieght:
            self._image_size_fit_height(arg)
        elif size_mode is PageSizeMode.FitWidth:
            self._image_size_fit_width(arg)
        elif size_mode is PageSizeMode.FullSize:
            self._image_size_full_size()

    def _image_size_keep(self):
        """更新图片尺寸，保持图片尺寸，仅处理旋转操作"""
        # 在宽高比变动时才更新图片
        if self.pixmap_original and not self.pixmap_original.isNull():
            ratio_current = round(self.pixmap().width() / self.pixmap().height(), 1)
            ratio_original = round(self.pixmap_original.width() / self.pixmap_original.height(), 1)
            if ratio_current != ratio_original:
                size = QSize(self.pixmap().height(), self.pixmap().width())
                scaled_pixmap = self.pixmap_original.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.setPixmap(scaled_pixmap)

    def _image_size_auto(self):
        """更新图片尺寸，适合其自身尺寸"""
        if self.pixmap_original and not self.pixmap_original.isNull():
            scaled_pixmap = self.pixmap_original.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)

    def _image_size_fit_page(self, qsize: QSize):
        """更新图片尺寸，适合页面框架尺寸"""
        if self.pixmap_original and not self.pixmap_original.isNull():
            scaled_pixmap = self.pixmap_original.scaled(qsize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)

    def _image_size_fit_height(self, height: int):
        """更新图片尺寸，适合高度"""
        # 备忘录 需要考虑滑动条的宽度
        if self.pixmap_original and not self.pixmap_original.isNull():
            calc_width = int(height / self.pixmap_original.height() * self.pixmap_original.width())
            size = QSize(calc_width, height)
            scaled_pixmap = self.pixmap_original.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)

    def _image_size_fit_width(self, width: int):
        """更新图片尺寸，适合宽度"""
        # 备忘录 需要考虑滑动条的宽度
        if self.pixmap_original and not self.pixmap_original.isNull():
            calc_height = int(width / self.pixmap_original.width() * self.pixmap_original.height()) - 1
            size = QSize(width, calc_height)
            scaled_pixmap = self.pixmap_original.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)

    def _image_size_full_size(self):
        """更新图片尺寸，实际大小"""
        if self.pixmap_original and not self.pixmap_original.isNull():
            self.setPixmap(self.pixmap_original)

    def _rotate(self, angle: int):
        """旋转图片
        :param angle: 旋转角度"""
        # 使用 QTransform 进行旋转
        transform = QTransform()
        transform.rotate(angle)
        # 应用
        self.pixmap_original = self.pixmap_original.transformed(transform)  # 直接替换原变量
