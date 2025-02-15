import lzytools._qt_pyside6
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QScrollArea, QWidget, QHBoxLayout, QVBoxLayout

from common.comic_info import ComicInfo
from common.image_info import ImageInfo
from common.mode_image_size import ModeImageSize


class _ViewerFrame(QScrollArea):
    """预览控件框架"""
    imageInfoShowed = Signal(ImageInfo, name='当前显示的图片信息类')

    def __init__(self, parent=None, layout='horizontal'):
        super().__init__(parent)
        self.setWidgetResizable(True)  # 使内容区域自适应尺寸
        # 设置外部框架控件
        self.content_widget = QWidget()
        if layout.lower() == 'horizontal':
            self.layout = QHBoxLayout()
        elif layout.lower() == 'vertical':
            self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.content_widget.setLayout(self.layout)
        self.setWidget(self.content_widget)
        # 设置透明背景
        lzytools._qt_pyside6.set_transparent_background(self)
        lzytools._qt_pyside6.set_transparent_background(self.content_widget)

        # 设置参数
        self.comic_info: ComicInfo = None  # 当前显示的漫画类
        self.page_index = 0  # 当前显示的页码（从1开始）
        self.page_size_mode = ModeImageSize.Fixed  # 当前的显示模式，默认为固定尺寸

    def set_comic(self, comic_info: ComicInfo):
        """设置漫画类
        :param comic_info: ComicInfo类"""
        self.comic_info = comic_info
        self.page_index = 1

    def show_image(self):
        """显示图片"""

    def previous_page(self):
        """上一页"""

    def next_page(self):
        """下一页"""

    def zoom_in(self):
        """放大页面"""
        self.page_size_mode = ModeImageSize.Fixed

    def zoom_out(self):
        """缩小页面"""
        self.page_size_mode = ModeImageSize.Fixed

    def keep_width(self):
        """以宽度为基准，固定尺寸显示图片"""
        if self.page_size_mode is not ModeImageSize.Fixed:
            self.page_size_mode = ModeImageSize.Fixed

    def fit_width(self):
        """以指定宽度为基准，显示图片"""
        if self.page_size_mode is not ModeImageSize.FitWidth:
            self.page_size_mode = ModeImageSize.FitWidth

    def fit_height(self):
        """以指定高度为基准，显示图片"""
        if self.page_size_mode is not ModeImageSize.FitHeight:
            self.page_size_mode = ModeImageSize.FitHeight

    def fit_widget(self):
        """以框架控件为基准，显示图片"""
        if self.page_size_mode is not ModeImageSize.FitPage:
            self.page_size_mode = ModeImageSize.FitPage

    def full_size(self):
        """页面实际尺寸"""
        if self.page_size_mode is not ModeImageSize.FullSize:
            self.page_size_mode = ModeImageSize.FullSize

    def rotate_left(self):
        """页面向左旋转"""

    def rotate_right(self):
        """页面向右旋转"""

    def clear(self):
        """清除显示"""

    def _update_size(self):
        """更新尺寸"""
        if self.page_size_mode is ModeImageSize.Fixed:
            self.keep_width()
        elif self.page_size_mode is ModeImageSize.FitPage:
            self.fit_widget()
        elif self.page_size_mode is ModeImageSize.FitWidth:
            self.fit_width()
        elif self.page_size_mode is ModeImageSize.FitHeight:
            self.fit_height()
        elif self.page_size_mode is ModeImageSize.FullSize:
            self.full_size()

    # def resizeEvent(self, event):
    #     super().resizeEvent(event)
    #     self._update_size()
