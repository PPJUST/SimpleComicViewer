# 预览控件，滚动显示漫画图像
# 显示方案：提前创建全部图像对应大小的空Label，按进度预载图像显示在Label上，超限的图像丢弃

from PySide6.QtCore import *
from PySide6.QtWidgets import *

from module import function_config
from module.class_comic_info import ComicInfo
from ui.show_comic.label_image_scroll import LabelImage


class ScrollAreaComicPreview(QScrollArea):
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
        self.index = 1  # 当前显示的索引号，从1开始，与页数对应
        self._comic_info = None  # 漫画信息类
        self._scroll_type = scroll_type  # 滚动类型，横向/纵向，用于计算索引号
        self._scroll_to_index_list = []  # 滚动条值与索引号的对应列表，[(0,150),(151,200)...]
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
        self._MAX_INDEX = self._comic_info.page_count
        self._create_empty_labels()
        self.show_images()

    def show_images(self):
        """显示预览图像"""
        for index in range(self.layout.count()):
            label = self.layout.itemAt(index).widget()
            if abs(self.index - 1 - index) > self._PRELOAD_PAGES:
                label.hide_image()
            else:
                label.show_image()

    def refresh_images(self):
        """刷新预览图像（仅用于更新大小）"""
        for index in range(self.layout.count()):
            label = self.layout.itemAt(index).widget()
            if abs(self.index - 1 - index) > self._PRELOAD_PAGES:
                label.hide_image()
            else:
                label.refresh_image()

    def next_page(self):
        """显示下一页图像"""
        current_index = self._calc_current_index()
        next_index = current_index + 1
        if next_index > len(self._scroll_to_index_list):
            return
        slider_start_value = self._scroll_to_index_list[next_index - 1][0]
        self._move_slider_absolute(slider_start_value)

    def previous_page(self):
        """显示上一页图像"""
        current_index = self._calc_current_index()
        next_index = current_index - 1
        if next_index < 1:
            return
        slider_start_value = self._scroll_to_index_list[next_index - 1][0]
        self._move_slider_absolute(slider_start_value)

    def reset_preview_size(self):
        """重设预览控件大小"""
        # 重置滚动条值与索引号的对应列表
        self._scroll_to_index_list.clear()
        # 修改子控件大小并更新索引列表
        for index in range(self.layout.count()):
            label = self.layout.itemAt(index).widget()
            label.reset_max_size(self)
            # 更新索引列表
            if self._scroll_type == 'h':
                self._update_index_list(label.width())
            elif self._scroll_type == 'v':
                self._update_index_list(label.height())
        # 刷新显示
        self.refresh_images()
        # 刷新索引
        self._slider_scrolled()

    def is_scroll_end(self):
        """是否已经滚动到底部"""
        if self._scroll_type == 'h':
            scroll_bar_position = self.horizontalScrollBar().value()
            max_position = self.horizontalScrollBar().maximum()
        elif self._scroll_type == 'v':
            scroll_bar_position = self.verticalScrollBar().value()
            max_position = self.verticalScrollBar().maximum()

        return scroll_bar_position == max_position

    def move_slider_relative(self, value: int):
        """移动滚动条（相对位置）"""
        new_value = self._get_slider_value() + value
        self._move_slider_absolute(new_value)

    def _create_empty_labels(self):
        """按照图像大小预先创建空的label"""
        self._clear_labels()
        for image_path in self._comic_info.page_list:
            label = LabelImage(self._scroll_type, self.widget)
            label.reset_comic(comic_path=self._comic_info.path, comic_filetype=self._comic_info.filetype)
            label.reset_image(image_path)
            label.load_pixmap()
            self.layout.addWidget(label)
            # 更新索引列表
            if self._scroll_type == 'h':
                self._update_index_list(label.width())
            elif self._scroll_type == 'v':
                self._update_index_list(label.height())

    def _clear_labels(self):
        """清空所有预生成的label"""
        while self.layout.count():
            item = self.layout.takeAt(0)
            item_widget = item.widget()
            if item_widget is not None:
                item_widget.deleteLater()

    def _update_index_list(self, label_side: int):
        """更新索引号对应列表
        :param label_side: 图像label的边长度"""
        if len(self._scroll_to_index_list) == 0:
            current_tuple = (0, label_side)
            self._scroll_to_index_list.append(current_tuple)
        else:
            last_end = self._scroll_to_index_list[-1][1]
            current_start = last_end + 1
            current_end = current_start + label_side
            current_tuple = (current_start, current_end)
            self._scroll_to_index_list.append(current_tuple)

    def _slider_scrolled(self):
        """响应滚动条移动事件"""
        self.is_scroll_end()
        current_index = self._calc_current_index()
        if self.index != current_index:
            self.index = current_index
            self.show_images()
            self.signal_scrolled.emit()

    def _calc_current_index(self):
        """根据滑动条的值估算当前索引号"""
        value = self._get_slider_value()
        for index, scroll_tuple in enumerate(self._scroll_to_index_list, start=1):
            start, end = scroll_tuple
            if start <= value <= end:
                return index

    def _get_slider_value(self) -> int:
        """获取当前滚动条的值"""
        if self._scroll_type == 'h':
            value = self.horizontalScrollBar().value()
        elif self._scroll_type == 'v':
            value = self.verticalScrollBar().value()
        return value

    def _move_slider_absolute(self, value):
        """移动滚动条（绝对位置）"""
        if self._scroll_type == 'h':
            self.horizontalScrollBar().setValue(value)
        elif self._scroll_type == 'v':
            self.verticalScrollBar().setValue(value)
