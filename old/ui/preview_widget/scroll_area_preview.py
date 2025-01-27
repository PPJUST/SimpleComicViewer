# 预览控件，滚动显示漫画图像
# 显示方案：提前创建全部图像对应大小的空Label，按进度预载图像显示在Label上，超限的图像丢弃

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QSizePolicy, QHBoxLayout, QWidget, QVBoxLayout

from module import function_normal
from module.class_comic_info import ComicInfo
from module.function_config_get import GetSetting
from ui.preview_widget.label_image_scroll import LabelImageScroll
from ui.preview_widget.scroll_area_smooth import ScrollAreaSmooth


class ScrollAreaPreview(ScrollAreaSmooth):
    """预览控件，滚动显示漫画图像"""
    signal_scrolled = Signal()

    def __init__(self, scroll_type: str, parent=None):
        """:param scroll_type: 滚动类型，横向h/纵向v"""
        super().__init__(parent)
        # ui设置
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sizeAdjustPolicy()
        self.setWidgetResizable(True)
        self.resize(parent.size())

        self.widget = QWidget(None)
        if scroll_type == 'h':
            self.layout = QHBoxLayout()
        elif scroll_type == 'v':
            self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setWidget(self.widget)

        # 设置滚动条的信号
        if scroll_type == 'h':
            self.horizontalScrollBar().valueChanged.connect(self._slider_scrolled)
        elif scroll_type == 'v':
            self.verticalScrollBar().valueChanged.connect(self._slider_scrolled)

        # 初始化
        self.index = 1  # 当前显示的索引，从1开始，与页数对应
        self._comic_info = None  # 漫画信息类
        self._scroll_type = scroll_type  # 滚动类型，横向h/纵向v，用于计算索引号
        self._value_group_list = []  # 滚动条值与索引的对应列表，[(0,150),(151,200)...]
        self._MIN_INDEX = 1  # 最小索引
        self._MAX_INDEX = None  # 最大索引
        self._PRELOAD_PAGES = None  # 预载图片数

        self._load_setting()
        self._show_default_image()


    def is_scroll_end(self):
        """是否已经滚动到底部"""
        if self._scroll_type == 'h':
            scroll_bar_position = self.horizontalScrollBar().value()
            max_position = self.horizontalScrollBar().maximum()
        elif self._scroll_type == 'v':
            scroll_bar_position = self.verticalScrollBar().value()
            max_position = self.verticalScrollBar().maximum()

        return scroll_bar_position == max_position
