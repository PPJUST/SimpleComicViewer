import lzytools._qt_pyside6
import lzytools.archive
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap, QTransform
from PySide6.QtWidgets import QLabel

from common.image_info import ImageInfo
from common.mode_image_size import ModeImageSize


class LabelImage(QLabel):
    """显示图片的控件"""
    ZOOM_WIDTH = 50  # 缩放时以宽度为基准进行缩放操作

    def __init__(self, image_info: str = None):
        """:param image_info: 图片信息类"""
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 参数设置
        self.pixmap_original: QPixmap = None  # 原始pixmap图片对象
        self.image_info: ImageInfo = image_info  # 图片信息类
        if self.image_info:
            self.pixmap_original = lzytools._qt_pyside6.bytes_to_pixmap(self.image_info.image_bytes)

    def is_showed_image(self) -> bool:
        """当前label是否已显示图片"""
        if self.pixmap() and not self.pixmap().isNull():
            return True
        else:
            return False

    def clear_image(self):
        """清除显示"""
        self.clear()

    def set_image(self, image_info: ImageInfo, angle: int = 0):
        """设置图片
        :param image_info: 图片信息类
        :param angle: 旋转角度"""
        self.image_info = image_info
        self.pixmap_original = lzytools._qt_pyside6.bytes_to_pixmap(image_info.image_bytes)
        if angle:
            self._rotate(angle)

    def set_label_size(self, size_mode: ModeImageSize, parent_size: QSize, is_show_image: bool = True):
        """设置label尺寸
        :param size_mode: 图片尺寸模式
        :param parent_size: 父控件尺寸"""
        # 调整label尺寸
        if size_mode is ModeImageSize.Fixed:
            pass
        if size_mode is ModeImageSize.FitPage:
            self._fit_page(parent_size)
        elif size_mode is ModeImageSize.FitHeight:
            self._fit_height(parent_size)
        elif size_mode is ModeImageSize.FitWidth:
            self._fit_width(parent_size)
        elif size_mode is ModeImageSize.FullSize:
            self._full_size()
        # 更新图片
        if is_show_image:
            self.show_image()

    def show_image(self):
        """显示图片"""
        if self.pixmap_original and not self.pixmap_original.isNull():
            scaled_pixmap = self.pixmap_original.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)

    def _fit_page(self, qsize: QSize):
        """以父控件为基准，保持图片纵横比设置label尺寸"""
        if self.pixmap_original and not self.pixmap_original.isNull():
            image_width = self.pixmap_original.width()
            image_height = self.pixmap_original.height()
            frame_width = qsize.width()
            frame_height = qsize.height()
            # 计算纵横比
            aspect_ratio = image_width / image_height
            # 根据框架宽度计算新高度
            new_width = frame_width
            new_height = int(frame_width / aspect_ratio)
            # 如果新高度超出框架高度，则根据框架高度计算新宽度
            if new_height > frame_height:
                new_width = int(frame_height * aspect_ratio)
            else:
                new_height = frame_height

            self.setFixedSize(new_width, new_height)

    def _fit_height(self, qsize: QSize):
        """以父控件的高度为基准，保持图片纵横比设置label尺寸"""
        # 备忘录 需要考虑滑动条的宽度
        if self.pixmap_original and not self.pixmap_original.isNull():
            image_width = self.pixmap_original.width()
            image_height = self.pixmap_original.height()
            frame_height = qsize.height()

            new_width = int(frame_height / image_height * image_width)
            self.setFixedSize(new_width, frame_height)

    def _fit_width(self, qsize: QSize):
        """以父控件的宽度为基准，保持图片纵横比设置label尺寸"""
        # 备忘录 需要考虑滑动条的宽度
        if self.pixmap_original and not self.pixmap_original.isNull():
            image_width = self.pixmap_original.width()
            image_height = self.pixmap_original.height()
            frame_width = qsize.width()

            new_height = int(frame_width / image_width * image_height)
            self.setFixedSize(frame_width, new_height)

    def _full_size(self):
        """以图片的实际尺寸设置label尺寸"""
        if self.pixmap_original and not self.pixmap_original.isNull():
            image_width = self.pixmap_original.width()
            image_height = self.pixmap_original.height()
            self.setFixedSize(image_width, image_height)

    def zoom_in(self, is_show_image: bool = True):
        """放大固定尺寸（以宽度为基准放大）"""
        if self.pixmap_original and not self.pixmap_original.isNull():
            label_width, label_height = self.size().width(), self.size().height()
            zoom_width = label_width + self.ZOOM_WIDTH
            zoom_height = int(zoom_width / label_width * label_height)
            self.setFixedSize(zoom_width, zoom_height)
        if is_show_image:
            self.show_image()

    def zoom_out(self, is_show_image: bool = True):
        """缩小固定尺寸（以宽度为基准缩小）"""
        if self.pixmap_original and not self.pixmap_original.isNull():
            label_width, label_height = self.size().width(), self.size().height()
            zoom_width = label_width - self.ZOOM_WIDTH
            zoom_height = int(zoom_width / label_width * label_height)
            if zoom_width <= 0 or zoom_height <= 0:  # 防止负数尺寸
                zoom_width, zoom_height = 1, 1
            self.setFixedSize(zoom_width, zoom_height)
        if is_show_image:
            self.show_image()

    def rotate_left(self):
        """向左旋转图片"""
        self._rotate(-90)
        self.show_image()

    def rotate_right(self):
        """向右旋转图片"""
        self._rotate(90)
        self.show_image()

    def _rotate(self, angle: int):
        """旋转图片
        :param angle: 旋转角度"""
        # 使用 QTransform 进行旋转
        transform = QTransform()
        transform.rotate(angle)
        # 应用
        self.pixmap_original = self.pixmap_original.transformed(transform)  # 直接替换原变量
