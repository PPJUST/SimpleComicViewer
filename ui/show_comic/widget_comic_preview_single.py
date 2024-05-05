# 预览控件，单页显示漫画图像

from PySide6.QtWidgets import *

from module.class_comic_info import ComicInfo
from module.function_config_get import GetSetting
from ui.show_comic.label_image_page import LabelImageList


class WidgetComicPreviewSingle(QScrollArea):
    """预览控件，单页显示漫画图像"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # ui设置
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sizeAdjustPolicy()
        self.setWidgetResizable(True)
        self.resize(parent.size())

        self.widget = QWidget(None)
        self.layout = QHBoxLayout()
        self.widget.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setWidget(self.widget)

        self.preview_label = LabelImageList(self)
        self.layout.addWidget(self.preview_label)

        # 初始化
        self.index = 1  # 当前显示的索引号，从1开始，与页数对应
        self._comic_info = None  # 漫画信息类
        self._MIN_INDEX = 1  # 最小索引号
        self._MAX_INDEX = None  # 最大索引号
        self._PRELOAD_PAGES = None  # 预载图片数

        self.load_setting()

    def load_setting(self):
        """加载设置"""
        self._PRELOAD_PAGES = GetSetting.preload_pages()

    def load_comic(self, comic_info: ComicInfo):
        """加载漫画数据"""
        self._comic_info = comic_info
        self.index = 1
        self._MAX_INDEX = self._comic_info.page_count
        self.preview_label.reset_comic(comic_path=self._comic_info.path, comic_filetype=self._comic_info.filetype)
        self.show_images()

    def show_images(self):
        """显示预览图像"""
        image = self._comic_info.page_list[self.index - 1]
        self.preview_label.reset_image(image)
        self.preview_label.show_image()

    def next_page(self):
        """显示下一页图像"""
        if self.index + 1 > self._MAX_INDEX:
            return
        self.index += 1
        self.show_images()

    def previous_page(self):
        """显示上一页图像"""
        if self.index - 1 < self._MIN_INDEX:
            return
        self.index -= 1
        self.show_images()

    def reset_preview_size(self):
        """重设预览控件大小"""
        self.preview_label.reset_max_size(self)
        self.preview_label.show_image()
