import lzytools._qt_pyside6
import lzytools.archive
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap, QTransform, QImage
from PySide6.QtWidgets import QLabel, QSizePolicy

from common.image_info import ImageInfo
from common.image_size_mode import ImageSizeMode


class LabelImage(QLabel):
    """显示图片的控件"""
    ZOOM_WIDTH = 50  # 缩放时以宽度为基准进行缩放操作

    def __init__(self, image_info: str = None):
        """:param image_info: 图片信息类"""
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 参数设置
        self.pixmap_original:QPixmap = None  # 原始pixmap图片对象
        self.image_info:ImageInfo = image_info  # 图片信息类
        if self.image_info:
            self.pixmap_original = lzytools._qt_pyside6.bytes_to_pixmap(self.image_info.image_bytes)
        self.width_fixed = None  # 图片尺寸模式为Fixed时的图片宽度（单独赋值给变量，防止在读取pixmap()对象计算高度时不统一的情形）

    def set_image(self, image_info: ImageInfo, angle: int = 0):
        """设置图片
        :param image_info: 图片信息类
        :param angle: 旋转角度"""
        self.image_info = image_info
        self.pixmap_original = lzytools._qt_pyside6.bytes_to_pixmap(image_info.image_bytes)
        if angle:
            self._rotate(angle)

    def zoom_in(self):
        """放大固定尺寸（以宽度为基准放大）"""
        if self.pixmap_original and not self.pixmap_original.isNull() and self.pixmap():
            current_width, current_height = self.pixmap().width(), self.pixmap().height()
            zoom_width = current_width + self.ZOOM_WIDTH
            zoom_height = int(zoom_width / current_width * current_height)
            size = QSize(zoom_width, zoom_height)
            scaled_pixmap = self.pixmap_original.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)
            self.width_fixed = zoom_width

    def zoom_out(self):
        """缩小固定尺寸（以宽度为基准缩小）"""
        if self.pixmap_original and not self.pixmap_original.isNull() and self.pixmap():
            current_width, current_height = self.pixmap().width(), self.pixmap().height()
            zoom_width = current_width - self.ZOOM_WIDTH
            zoom_height = int(zoom_width / current_width * current_height)
            if zoom_width <= 0 or zoom_height <= 0:  # 防止负数尺寸
                zoom_width, zoom_height = 1, 1
            size = QSize(zoom_width, zoom_height)
            scaled_pixmap = self.pixmap_original.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)
            self.width_fixed = zoom_width

    def rotate_left(self):
        """向左旋转图片"""
        self._rotate(-90)

    def rotate_right(self):
        """向右旋转图片"""
        self._rotate(90)

    def show_image(self, image_size_mode: ImageSizeMode, arg=None):
        """显示图片
        :param image_size_mode: 图片大小模式
        :param arg: 对应模式的大小参数"""
        if image_size_mode is ImageSizeMode.Fixed:
            self._image_size_keep_width()
        if image_size_mode is ImageSizeMode.FitPage:
            self._image_size_fit_page(arg)
        elif image_size_mode is ImageSizeMode.FitHeight:
            self._image_size_fit_height(arg)
        elif image_size_mode is ImageSizeMode.FitWidth:
            self._image_size_fit_width(arg)
        elif image_size_mode is ImageSizeMode.FullSize:
            self._image_size_full_size()

    def _image_size_keep_width(self):
        """以宽度为基准，固定尺寸显示图片"""
        if not self.pixmap() or self.pixmap().isNull():
            self._image_size_fit_self()
        else:
            self._image_size_fit_width(self.width_fixed)

    def _image_size_fit_self(self):
        """适合label自身大小，显示图片"""
        if self.pixmap_original and not self.pixmap_original.isNull():
            scaled_pixmap = self.pixmap_original.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)
            self.width_fixed = self.pixmap().width()

    def _image_size_fit_page(self, qsize: QSize):
        """以框架控件为基准，显示图片"""
        if self.pixmap_original and not self.pixmap_original.isNull():
            scaled_pixmap = self.pixmap_original.scaled(qsize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)

    def _image_size_fit_height(self, height: int):
        """以指定高度为基准，显示图片"""
        # 备忘录 需要考虑滑动条的宽度
        if self.pixmap_original and not self.pixmap_original.isNull():
            calc_width = int(height / self.pixmap_original.height() * self.pixmap_original.width())
            size = QSize(calc_width, height)
            scaled_pixmap = self.pixmap_original.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)

    def _image_size_fit_width(self, width: int):
        """以指定宽度为基准，显示图片"""
        # 备忘录 需要考虑滑动条的宽度
        if self.pixmap_original and not self.pixmap_original.isNull():
            calc_height = int(width / self.pixmap_original.width() * self.pixmap_original.height())
            size = QSize(width, calc_height)
            scaled_pixmap = self.pixmap_original.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)

    def _image_size_full_size(self):
        """以实际大小显示图片"""
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
