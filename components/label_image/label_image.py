from PySide6.QtGui import *
from PySide6.QtWidgets import *


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
        self.update_image_size()

    def update_image_size(self):
        """更新图片尺寸"""
        if not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)

    def resizeEvent(self, event):
        self.update_image_size()
        super().resizeEvent(event)
