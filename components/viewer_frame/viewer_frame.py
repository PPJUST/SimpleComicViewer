import lzytools._qt_pyside6
from PySide6.QtWidgets import *

from common.comic_info import ComicInfo


class ViewerFrame(QScrollArea):
    """预览控件框架"""

    def __init__(self, parent=None, layout='horizontal'):
        super().__init__(parent)
        self.setWidgetResizable(True)  # 使内容区域自适应大小
        # 设置外部框架控件
        self.content_widget = QWidget()
        if layout.lower() == 'horizontal':
            self.layout = QHBoxLayout()
        elif layout.lower() == 'vertical':
            self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.content_widget.setLayout(self.layout)
        self.setWidget(self.content_widget)
        # 设置透明背景
        lzytools._qt_pyside6.set_transparent_background(self)
        lzytools._qt_pyside6.set_transparent_background(self.content_widget)

        # 设置参数
        self.comic: ComicInfo = None  # 当前显示的漫画类

    def set_comic(self, comic_path: str):
        """设置漫画类
        :param comic_path: 漫画路径"""
        # 防止报错，先检查路径对应文件是否为漫画
        self.comic = ComicInfo(comic_path)

    def show_image(self):
        """显示图片"""

    def previous_page(self):
        """上一页"""

    def next_page(self):
        """下一页"""

    def zoom_in(self):
        """放大页面"""

    def zoom_out(self):
        """缩小页面"""

    def autoplay_start(self):
        """开始自动播放"""

    def autoplay_stop(self):
        """停止自动播放"""

    def fit_height(self):
        """页面大小适应高度"""

    def fit_widget(self):
        """页面大小适应宽度"""

    def fit_width(self):
        """页面大小适应框架"""

    def full_size(self):
        """页面实际大小"""

    def rotate_left(self):
        """页面向左旋转"""

    def rotate_right(self):
        """页面向右旋转"""
