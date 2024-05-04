# 预览控件，双页显示漫画图像

from PySide6.QtWidgets import *

from module import function_image, function_config
from module.class_comic_info import ComicInfo
from ui.show_comic.label_image_page import LabelImageList


class WidgetComicPreviewDouble(QWidget):
    """预览控件，双页显示漫画图像"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # ui设置
        self.resize(parent.size())
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)
        # 左页
        self.label_left = LabelImageList(self)
        self.layout.addWidget(self.label_left)
        # 右页
        self.label_right = LabelImageList(self)
        self.layout.addWidget(self.label_right)

        # 初始化
        self.index = 1  # 当前左页显示的索引号，从1开始，与页数对应
        self._index_right = self.index + 1  # 右页索引号
        self._comic_info = None  # 漫画信息类
        self._MIN_INDEX = 1  # 最小索引号
        self._MAX_INDEX = None  # 最大索引号
        self._PRELOAD_PAGES = None  # 预载图片数

        self.load_setting()

    def load_setting(self):
        """加载设置"""
        self._PRELOAD_PAGES = function_config.GetSetting.preload_pages()

    def load_comic(self, comic_info: ComicInfo):
        """加载漫画数据"""
        self._comic_info = comic_info
        self.index = 1
        self._index_right = self.index + 1
        self._MAX_INDEX = self._comic_info.page_count

        self.label_left.reset_comic(comic_path=self._comic_info.path, comic_filetype=self._comic_info.filetype)
        self.label_right.reset_comic(comic_path=self._comic_info.path, comic_filetype=self._comic_info.filetype)
        self.show_images()

    def show_images(self):
        """显示预览图像"""
        # 检查左页图像是否为横向图像，如果是横向图像，则仅显示左页，不显示右页，且重设右页索引
        # 设置左页
        show_image_left = self._comic_info.page_list[self.index - 1]  # 页数索引从1开始，需要还原
        self.label_left.reset_image(show_image_left)
        self.label_left.show_image()
        # 右页，右页索引超限时或左页/右页为横向图像时不显示
        if self._index_right > self._MAX_INDEX:
            self.label_right.hide_label()
            self._index_right = self.index
        else:
            show_image_right = self._comic_info.page_list[self._index_right - 1]
            if function_image.is_horizontal_image(show_image_left) or function_image.is_horizontal_image(
                    show_image_right):
                self.label_right.hide_label()
                self._index_right = self.index
            else:
                self.label_right.reset_image(show_image_right)
                self.label_right.show_image()

    def next_page(self):
        """显示下一页图像"""
        if self.index + 1 > self._MAX_INDEX or self._index_right + 1 > self._MAX_INDEX:
            return
        self.index = self._index_right + 1
        self._index_right = self.index + 1
        self.show_images()

    def previous_page(self):
        """显示上一页图像"""
        if self.index - 1 < self._MIN_INDEX or self._index_right - 1 < self._MIN_INDEX:
            return
        show_image_left = self._comic_info.page_list[self.index - 2]
        show_image_right = self._comic_info.page_list[self.index - 1]
        if function_image.is_horizontal_image(show_image_left) or function_image.is_horizontal_image(show_image_right):
            self.index -= 1
            self._index_right = self.index + 1
        else:
            self._index_right = self.index - 1
            self.index = self._index_right - 1
        self.show_images()

    def reset_preview_size(self):
        """重设预览控件大小"""
        self.label_left.reset_max_size(self)
        self.label_left.show_image()

        self.label_right.reset_max_size(self)
        self.label_right.show_image()