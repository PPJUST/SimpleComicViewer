# 漫画预览控件控制中心

from PySide6.QtCore import *
from PySide6.QtWidgets import *

from module import function_config, function_normal
from module.class_comic_info import ComicInfo
from ui.label_hover_info import LabelHover
from ui.show_comic.scroll_area_comic_preview import ScrollAreaComicPreview
from ui.show_comic.widget_comic_preview_double import WidgetComicPreviewDouble
from ui.show_comic.widget_comic_preview_single import WidgetComicPreviewSingle
from ui.thread_auto_play import ThreadAutoPlay


class WidgetPreviewControl(QWidget):
    """漫画预览控件控制中心"""
    signal_stop_auto_play = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        # ui设置
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        # 设置自动播放线程
        self.thread_auto_play = ThreadAutoPlay()
        self.thread_auto_play.signal_next.connect(self.auto_play)

        # 设置悬浮label
        self.hover_label = LabelHover(self)
        self.installEventFilter(self.hover_label)
        self.hover_label.raise_()  # 使该label显示在widget之上

        # 初始化
        self.child_preview_widget = None  # 预览子控件
        self.max_index = None
        self.comic_info = None
        self.load_child_preview_widget()

    def load_child_preview_widget(self, view_mode=None):
        """加载设置"""
        if not view_mode:
            view_mode = function_config.GetSetting.current_view_mode_eng()
        self.set_auto_play_type(view_mode)
        if view_mode == 'mode_1':
            self._load_preview_widget_single()
        elif view_mode == 'mode_2':
            self._load_preview_widget_double()
        elif view_mode == 'mode_3':
            self._load_preview_widget_scroll('v')
        elif view_mode == 'mode_4':
            self._load_preview_widget_scroll('h')

    def load_comic(self, comic_path: str = None):
        """加载漫画数据"""
        if comic_path:
            self.comic_info = ComicInfo(comic_path)
            self.max_index = self.comic_info.page_count

        if self.comic_info:
            self.child_preview_widget.load_comic(self.comic_info)
            self.hover_label.update_info_by_comic(self.comic_info)
            self.hover_label.raise_()

    def to_previous_page(self):
        """切换下一页"""
        self.child_preview_widget.previous_page()
        self._update_label_info()

    def to_next_page(self):
        """切换下一页"""
        self.child_preview_widget.next_page()
        self._update_label_info()

    def move_scroll_slider(self, value: int):
        """滚动条移动指定距离"""
        self.child_preview_widget.move_slider_relative(value)
        self._update_label_info()

    def auto_play(self, value=None):
        """自动播放"""
        if isinstance(self.child_preview_widget, (WidgetComicPreviewSingle, WidgetComicPreviewDouble)):
            if self.child_preview_widget.index < self.max_index:
                self.to_next_page()
            else:
                self.stop_auto_play()
                self.signal_stop_auto_play.emit()
        elif isinstance(self.child_preview_widget, ScrollAreaComicPreview):
            if not self.child_preview_widget.is_scroll_end():
                self.move_scroll_slider(value)
            else:
                self.stop_auto_play()
                self.signal_stop_auto_play.emit()

    def start_auto_play(self):
        """开始自动播放"""
        self.thread_auto_play.start()

    def stop_auto_play(self):
        """停止自动播放"""
        self.thread_auto_play.stop_play()

    def set_auto_play_type(self, view_mode):
        """设置自动播放类型"""
        self.thread_auto_play.set_preview_type(view_mode)

    def reset_preview_size(self):
        """重设预览控件大小"""
        self.child_preview_widget.reset_preview_size()

    def _load_preview_widget_single(self):
        """显示预览控件"""
        function_normal.print_function_info()
        self._clear_preview_layout()
        self.child_preview_widget = WidgetComicPreviewSingle(self)
        self.layout.addWidget(self.child_preview_widget)

    def _load_preview_widget_double(self):
        """显示预览控件"""
        function_normal.print_function_info()
        self._clear_preview_layout()
        self.child_preview_widget = WidgetComicPreviewDouble(self)
        self.layout.addWidget(self.child_preview_widget)

    def _load_preview_widget_scroll(self, scroll_type: str):
        """显示预览控件
        :param scroll_type: 滚动类型，横向h/纵向v"""
        function_normal.print_function_info()
        self._clear_preview_layout()
        self.child_preview_widget = ScrollAreaComicPreview(scroll_type, self)
        self.child_preview_widget.signal_scrolled.connect(
            self._update_label_info)
        self.layout.addWidget(self.child_preview_widget)

    def _clear_preview_layout(self):
        """清空布局内的控件"""
        while self.layout.count():
            item = self.layout.takeAt(0)
            item_widget = item.widget()
            if item_widget is not None:
                item_widget.deleteLater()

    def _update_label_info(self):
        """更新悬浮信息框的内容"""
        self.hover_label.update_current_page(self.child_preview_widget.index)
        self.hover_label.raise_()
