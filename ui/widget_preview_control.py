# 漫画预览控件控制中心

from PySide6.QtCore import *
from PySide6.QtWidgets import *

from module import function_normal
from module.class_comic_info import ComicInfo
from module.function_config_get import GetSetting
from ui.label_hover_comic_info import LabelHoverComicInfo
from ui.show_comic.scroll_area_comic_preview import ScrollAreaComicPreview
from ui.show_comic.widget_comic_preview_double import WidgetComicPreviewDouble
from ui.show_comic.widget_comic_preview_single import WidgetComicPreviewSingle
from ui.thread_auto_play import ThreadAutoPlay


class WidgetPreviewControl(QWidget):
    """漫画预览控件控制中心"""
    signal_stop_auto_play = Signal()
    signal_show_info = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        # ui设置
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        # 设置自动播放线程
        self.thread_auto_play = ThreadAutoPlay()
        self.thread_auto_play.signal_next.connect(self._get_autoplay_signal)
        self.thread_auto_play.signal_speed_info.connect(self.signal_show_info.emit)

        # 设置左上角的漫画信息悬浮label
        self.label_hover_comic_info = LabelHoverComicInfo(self)
        self.installEventFilter(self.label_hover_comic_info)
        self.label_hover_comic_info.raise_()  # 使该label显示在widget之上

        # 初始化
        self.child_preview_widget = None  # 预览子控件
        self.max_index = None
        self.comic_info = None
        self.load_child_preview_widget()

    def load_child_preview_widget(self, view_mode=None):
        """加载设置"""
        function_normal.print_function_info()
        if not view_mode:
            view_mode = GetSetting.current_view_mode_eng()
        self.reset_autoplay_setting()
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
        function_normal.print_function_info()
        if comic_path:
            self.comic_info = ComicInfo(comic_path)
            self.max_index = self.comic_info.page_count

        if self.comic_info:
            self.child_preview_widget.load_comic(self.comic_info)
            self.label_hover_comic_info.update_info_by_comic(self.comic_info)
            self.label_hover_comic_info.raise_()

    def start_autoplay(self):
        """开始自动播放线程"""
        function_normal.print_function_info()
        self.thread_auto_play.start()

    def stop_autoplay(self):
        """停止自动播放线程"""
        function_normal.print_function_info()
        self.thread_auto_play.stop_play()
        self.signal_stop_auto_play.emit()

        if isinstance(self.child_preview_widget, ScrollAreaComicPreview):
            self.child_preview_widget.stop_autoplay()

    def _get_autoplay_signal(self, speed):
        """接收自动播放线程的信号，执行对应的方法"""
        function_normal.print_function_info()
        if isinstance(self.child_preview_widget, (WidgetComicPreviewSingle, WidgetComicPreviewDouble)):
            if self.child_preview_widget.index < self.max_index:
                self.to_next_page()
            else:
                self.stop_autoplay()
                self.signal_stop_auto_play.emit()
        elif isinstance(self.child_preview_widget, ScrollAreaComicPreview):
            if not self.child_preview_widget.is_scroll_end():
                self._scroll_autoplay(speed)
            else:
                self.stop_autoplay()
                self.signal_stop_auto_play.emit()

    def to_previous_page(self):
        """切换下一页（单页/双页视图）"""
        function_normal.print_function_info()
        self.child_preview_widget.previous_page()

    def to_next_page(self):
        """切换下一页（单页/双页视图）"""
        function_normal.print_function_info()
        self.child_preview_widget.next_page()

    def _scroll_autoplay(self, speed):
        """滚动视图的自动播放"""
        function_normal.print_function_info()
        self.child_preview_widget.start_autoplay(speed)

    def reset_autoplay_setting(self):
        """初始化自动播放线程设置"""
        function_normal.print_function_info()
        self.thread_auto_play.reset_setting()

    def speed_up_autoplay(self):
        """加速自动播放"""
        function_normal.print_function_info()
        self.thread_auto_play.speed_up()

    def speed_down_autoplay(self):
        """减速自动播放"""
        function_normal.print_function_info()
        self.thread_auto_play.speed_down()

    def reset_autoplay_speed(self):
        """重置自动播放速度"""
        function_normal.print_function_info()
        self.thread_auto_play.reset_speed()

    def reset_preview_size(self):
        """重设预览控件大小"""
        function_normal.print_function_info()
        self.child_preview_widget.reset_preview_size()

    def _load_preview_widget_single(self):
        """显示预览控件"""
        function_normal.print_function_info()
        self._clear_preview_layout()
        self.child_preview_widget = WidgetComicPreviewSingle(self)
        self.child_preview_widget.signal_page_changed.connect(
            self._update_label_info)
        self.layout.addWidget(self.child_preview_widget)

    def _load_preview_widget_double(self):
        """显示预览控件"""
        function_normal.print_function_info()
        self._clear_preview_layout()
        self.child_preview_widget = WidgetComicPreviewDouble(self)
        self.child_preview_widget.signal_page_changed.connect(
            self._update_label_info)
        self.layout.addWidget(self.child_preview_widget)

    def _load_preview_widget_scroll(self, scroll_type: str):
        """显示预览控件
        :param scroll_type: 滚动类型，横向h/纵向v"""
        function_normal.print_function_info()
        self._clear_preview_layout()
        self.child_preview_widget = ScrollAreaComicPreview(scroll_type, self)
        self.child_preview_widget.signal_scrolled.connect(self._update_label_info)
        self.child_preview_widget.signal_stop_autoplay.connect(self.stop_autoplay)
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
        self.label_hover_comic_info.update_current_page(self.child_preview_widget.index)
        self.label_hover_comic_info.raise_()
