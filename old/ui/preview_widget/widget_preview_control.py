# 漫画预览控件控制中心

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout

from module import function_normal
from module.class_comic_info import ComicInfo
from module.function_config_get import GetSetting
from thread.thread_autoplay import ThreadAutoPlay
from ui.label_hover_comic_info import LabelHoverComicInfo
from ui.label_hover_run_info import LabelHoverRunInfo
from ui.preview_widget.scroll_area_preview import ScrollAreaPreview
from ui.preview_widget.scroll_area_preview_reverse import ScrollAreaPreviewReverse
from ui.preview_widget.widget_preview_double import WidgetPreviewDouble
from ui.preview_widget.widget_preview_single import WidgetPreviewSingle


class WidgetPreviewControl(QWidget):
    """漫画预览控件控制中心"""
    signal_stop_autoplay = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        # ui设置
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        # 设置自动播放线程
        self.thread_autoplay = ThreadAutoPlay()
        self.thread_autoplay.signal_next.connect(self._get_thread_signal_autoplay)

        # 设置左上角的漫画信息悬浮label
        self.label_hover_comic_info = LabelHoverComicInfo(self)
        self.installEventFilter(self.label_hover_comic_info)
        self.label_hover_comic_info.raise_()  # 使该label显示在widget之上

        # 初始化
        self.child_preview_widget = None  # 预览子控件
        self.max_index = None  # 最大索引
        self.comic_info = None  # 漫画信息类

        # 加载预览子控件
        self._load_child_preview_widget()

        # 加载信息显示控件（单例模式，实例在主程序中）
        self.label_hover_run_info = LabelHoverRunInfo()

    def set_comic(self, comic_path: str = None):
        """加载漫画数据"""
        function_normal.print_function_info()
        if comic_path:
            self.comic_info = ComicInfo(comic_path)
            self.max_index = self.comic_info.page_count

        self.child_preview_widget.set_comic(self.comic_info)
        self.label_hover_comic_info.update_info_by_comic(self.comic_info)
        self.label_hover_comic_info.raise_()

    def start_thread_autoplay(self):
        """开始自动播放线程"""
        function_normal.print_function_info()
        self.label_hover_run_info.show_information('开始自动播放')
        self.thread_autoplay.start()

    def stop_thread_autoplay(self):
        """停止自动播放线程"""
        function_normal.print_function_info()
        if self.thread_autoplay.isRunning():
            self.label_hover_run_info.show_information('停止自动播放')
            self.thread_autoplay.stop_play()
            self.signal_stop_autoplay.emit()

            # 如果是滚动模式，则还需要停止滚动视图的动画
            if isinstance(self.child_preview_widget, ScrollAreaPreview):
                self.child_preview_widget.stop_autoplay()

    def reload_child_preview_widget(self):
        """重新加载预览控件"""
        function_normal.print_function_info()
        self.label_hover_run_info.show_information('加载预览控件')
        view_mode = GetSetting.current_view_mode_eng()
        self.stop_thread_autoplay()
        self._set_preview_mode(view_mode)
        self._reset_autoplay_setting()
        if self.comic_info:
            self.set_comic()

    def clear_preview(self):
        """清空预览控件"""
        self._clear_preview_layout()

    def to_previous_page(self):
        """切换下一页（单页/双页视图）"""
        function_normal.print_function_info()
        self.child_preview_widget.to_previous_page()

    def to_next_page(self):
        """切换下一页（单页/双页视图）"""
        function_normal.print_function_info()
        self.child_preview_widget.to_next_page()

    def autoplay_speed_up(self):
        """自动播放加速"""
        function_normal.print_function_info()
        self.thread_autoplay.speed_up()

    def autoplay_speed_down(self):
        """自动播放减速"""
        function_normal.print_function_info()
        self.thread_autoplay.speed_down()

    def reset_autoplay_speed(self):
        """重置自动播放速度"""
        function_normal.print_function_info()
        self.thread_autoplay.reset_speed()

    def reset_preview_size(self):
        """重设预览控件大小"""
        function_normal.print_function_info()
        self.child_preview_widget.reset_preview_size()

    def _reset_autoplay_setting(self):
        """重置自动播放的设置参数"""
        function_normal.print_function_info()
        self.thread_autoplay.reset_setting()

    def _set_preview_mode(self, view_mode=None):
        """设置预览模式"""
        function_normal.print_function_info()
        if not view_mode:
            view_mode = GetSetting.current_view_mode_eng()
        self._reset_autoplay_setting()
        self._load_child_preview_widget(view_mode)

    def _get_thread_signal_autoplay(self, speed):
        """接收自动播放线程的信号，执行对应的方法"""
        function_normal.print_function_info()
        # 如果是当前是单页/双页视图
        if isinstance(self.child_preview_widget, (WidgetPreviewSingle, WidgetPreviewDouble)):
            if self.child_preview_widget.index < self.max_index:
                self.to_next_page()
            else:  # 页数超限，终止自动播放
                self.stop_thread_autoplay()
                self.signal_stop_autoplay.emit()
        # 如果当前是滚动视图
        elif isinstance(self.child_preview_widget, ScrollAreaPreview):
            if not self.child_preview_widget.is_scroll_end():
                self._start_scroll_autoplay(speed)
            else:  # 滚动条已到底部，终止自动播放
                self.stop_thread_autoplay()
                self.signal_stop_autoplay.emit()

    def _start_scroll_autoplay(self, speed):
        """启动滚动视图的自动播放"""
        function_normal.print_function_info()
        self.child_preview_widget.start_autoplay(speed)

    def _load_child_preview_widget(self, mode=None):
        """加载预览子控件"""
        if not mode:
            mode = GetSetting.current_view_mode_eng()
        if mode == 'mode_1':
            self._load_preview_widget_single()
        elif mode == 'mode_2':
            self._load_preview_widget_double()
        elif mode == 'mode_3':
            self._load_preview_widget_scroll('v')
        elif mode == 'mode_4':
            self._load_preview_widget_scroll('h')
        elif mode == 'mode_5':
            self._load_preview_widget_double()  # 备忘录 反向视图
        elif mode == 'mode_6':
            self._load_preview_widget_scroll_reverse()

    def _load_preview_widget_single(self):
        """加载预览子控件-单页模式"""
        function_normal.print_function_info()
        self._clear_preview_layout()
        self.child_preview_widget = WidgetPreviewSingle(self)
        self.child_preview_widget.signal_page_changed.connect(self._update_hover_label_info)
        self.layout.addWidget(self.child_preview_widget)

    def _load_preview_widget_double(self):
        """加载预览子控件-双页模式"""
        function_normal.print_function_info()
        self._clear_preview_layout()
        self.child_preview_widget = WidgetPreviewDouble(self)
        self.child_preview_widget.signal_page_changed.connect(self._update_hover_label_info)
        self.layout.addWidget(self.child_preview_widget)

    def _load_preview_widget_scroll(self, scroll_type: str):
        """加载预览子控件-滚动模式
        :param scroll_type: 滚动类型，横向h/纵向v"""
        function_normal.print_function_info()
        self._clear_preview_layout()
        self.child_preview_widget = ScrollAreaPreview(scroll_type, self)
        self.child_preview_widget.signal_scrolled.connect(self._update_hover_label_info)
        self.child_preview_widget.signal_stop_autoplay.connect(self.stop_thread_autoplay)
        self.layout.addWidget(self.child_preview_widget)

    def _load_preview_widget_scroll_reverse(self):
        """加载预览子控件-滚动模式"""
        function_normal.print_function_info()
        self._clear_preview_layout()
        self.child_preview_widget = ScrollAreaPreviewReverse(parent=self)
        self.child_preview_widget.signal_scrolled.connect(self._update_hover_label_info)
        self.child_preview_widget.signal_stop_autoplay.connect(self.stop_thread_autoplay)
        self.layout.addWidget(self.child_preview_widget)

    def _clear_preview_layout(self):
        """清空布局内的控件"""
        while self.layout.count():
            item = self.layout.takeAt(0)
            item_widget = item.widget()
            if item_widget is not None:
                item_widget.deleteLater()

    def _update_hover_label_info(self):
        """更新悬浮信息框"""
        self.label_hover_comic_info.update_current_page(
            self.child_preview_widget.index)
        self.label_hover_comic_info.raise_()
