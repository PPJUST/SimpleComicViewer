# 预览控件，单页显示漫画图像
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QSizePolicy, QWidget, QScrollArea, QHBoxLayout

from module import function_normal
from module.class_comic_info import ComicInfo
from module.function_config_get import GetSetting
from ui.preview_widget.label_image_page import LabelImagePage


class WidgetComicPreviewSingle(QScrollArea):
    """预览控件，单页显示漫画图像"""
    signal_page_changed = Signal()

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

        self.preview_label = LabelImagePage(self)
        self.layout.addWidget(self.preview_label)

        # 初始化
        self.index = 1  # 当前显示的索引号，从1开始，与页数对应
        self._comic_info = None  # 漫画信息类
        self._MIN_INDEX = 1  # 最小索引号
        self._MAX_INDEX = None  # 最大索引号
        self._PRELOAD_PAGES = None  # 预载图片数

        self._load_setting()

    def _load_setting(self):
        """加载设置"""
        self._PRELOAD_PAGES = GetSetting.preload_pages()

    def set_comic(self, comic_info: ComicInfo):
        """加载漫画数据"""
        function_normal.print_function_info()
        self._comic_info = comic_info
        self.index = 1
        self._MAX_INDEX = self._comic_info.page_count
        self.preview_label.set_comic(
            self._comic_info.path, self._comic_info.filetype)
        self._show_images()

    def _show_images(self):
        """显示图像"""
        function_normal.print_function_info()
        image = self._comic_info.page_list[self.index - 1]
        self.preview_label.set_image(image)
        self.preview_label.show_image()

    def to_next_page(self):
        """切换到下一页"""
        function_normal.print_function_info()
        if self.index + 1 > self._MAX_INDEX:
            return
        self.index += 1
        self._show_images()
        self.signal_page_changed.emit()

    def to_previous_page(self):
        """切换到上一页"""
        function_normal.print_function_info()
        if self.index - 1 < self._MIN_INDEX:
            return
        self.index -= 1
        self._show_images()
        self.signal_page_changed.emit()

    def reset_preview_size(self):
        """重设预览控件大小"""
        function_normal.print_function_info()
        self.preview_label.set_parent(self)
        self.preview_label.show_image()

    def wheelEvent(self, event):
        """设置鼠标滚轮切页"""
        function_normal.print_function_info()
        # 获取鼠标滚轮滚动的角度
        angle = event.angleDelta().y()
        # 根据角度的正负区分滚轮向上向下操作
        if angle > 0:  # 向上
            self.to_previous_page()
        else:  # 向下
            self.to_next_page()
