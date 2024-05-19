# 预览控件，滚动显示漫画图像
# 显示方案：提前创建全部图像对应大小的空Label，按进度预载图像显示在Label上，超限的图像丢弃

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QSizePolicy, QHBoxLayout, QWidget, QVBoxLayout

from module import function_normal
from module.class_comic_info import ComicInfo
from module.function_config_get import GetSetting
from ui.preview_widget.label_image_scroll import LabelImage
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

    def _load_setting(self):
        """加载设置"""
        self._PRELOAD_PAGES = GetSetting.preload_pages()

    def set_comic(self, comic_info: ComicInfo):
        """设置漫画数据"""
        function_normal.print_function_info()
        self._comic_info = comic_info
        self.index = 1
        self._MAX_INDEX = self._comic_info.page_count
        self._create_empty_labels()
        self.show_images()
        self._move_slider_absolute(0)

    def show_images(self):
        """显示图像"""
        function_normal.print_function_info()
        for index in range(self.layout.count()):
            label = self.layout.itemAt(index).widget()
            if abs(self.index - 1 - index) > self._PRELOAD_PAGES:
                label.hide_image()
            else:
                label.show_image()

    def refresh_images(self):
        """刷新图像（更新大小）"""
        function_normal.print_function_info()
        for index in range(self.layout.count()):
            label = self.layout.itemAt(index).widget()
            if abs(self.index - 1 - index) > self._PRELOAD_PAGES:
                label.hide_image()
            else:
                label.refresh_image()

    def to_next_page(self):
        """切换到下一页"""
        function_normal.print_function_info()
        current_index = self._calc_current_index()
        next_index = current_index + 1
        if next_index > len(self._value_group_list):
            return
        next_page_slider_value = self._value_group_list[next_index - 1][0]
        self._move_slider_absolute(next_page_slider_value)

    def to_previous_page(self):
        """切换到上一页"""
        function_normal.print_function_info()
        current_index = self._calc_current_index()
        next_index = current_index - 1
        if next_index < 1:
            return
        previous_page_slider_value = self._value_group_list[next_index - 1][0]
        self._move_slider_absolute(previous_page_slider_value)

    def reset_preview_size(self):
        """重设预览控件大小"""
        function_normal.print_function_info()
        # 重置滚动条值与索引号的对应列表
        self._value_group_list.clear()
        # 更新子控件大小，并更新索引列表
        for index in range(self.layout.count()):
            label = self.layout.itemAt(index).widget()
            label.set_parent(self)
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

    def _create_empty_labels(self):
        """按照图像大小预先创建空的label"""
        self._clear_labels()
        for image_path in self._comic_info.page_list:
            label = LabelImage(self._scroll_type, self.widget)
            label.set_comic(self._comic_info.path, self._comic_info.filetype)
            label.set_image(image_path)
            label._load_pixmap()  # 备忘录，暂时先读取全部图像，之后做在子线程中读取
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
        """更新索引列表
        :param label_side: 图像label的边长度"""
        if len(self._value_group_list) == 0:
            current_tuple = (0, label_side)
            self._value_group_list.append(current_tuple)
        else:
            last_end = self._value_group_list[-1][1]
            current_start = last_end + 1
            current_end = current_start + label_side
            current_tuple = (current_start, current_end)
            self._value_group_list.append(current_tuple)

    def _slider_scrolled(self):
        """响应滚动条移动事件"""
        current_index = self._calc_current_index()
        if self.index != current_index:
            self.index = current_index
            self.show_images()
            self.signal_scrolled.emit()

    def _calc_current_index(self):
        """根据滑动条的值计算当前索引"""
        value = self._get_slider_value()
        for index, scroll_tuple in enumerate(self._value_group_list, start=1):
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
