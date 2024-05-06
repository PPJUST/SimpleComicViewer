# 主界面左上方的控制栏组件的子控件，用于编写隐藏事件

from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *

from constant import (_ICON_DOUBLE_PAGE, _ICON_DOUBLE_PAGE_RED,
                      _ICON_SCROLL_HORIZONTAL, _ICON_SCROLL_HORIZONTAL_RED,
                      _ICON_SCROLL_VERTICAL, _ICON_SCROLL_VERTICAL_RED,
                      _ICON_SINGLE_PAGE, _ICON_SINGLE_PAGE_RED)
from module import function_normal
from module.function_config_get import GetSetting
from module.function_config_reset import ResetSetting
from ui.thread_wait_time import ThreadWaitTime
from ui.ui_src.ui_widget_top_control_child import Ui_Form


class WidgetTopControlChild(QWidget):
    """主界面左上方的控制栏组件的子控件，用于编写隐藏事件"""
    signal_preview_mode_changed = Signal()  # 改变预览模式

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # ui设置
        self.setMouseTracking(True)
        self._reset_icon_preview_button()
        self._reset_button_size()

        # 初始化
        self._mode_preview = None
        self.thread_wait = None
        self._load_setting()

        # 点击按钮后发送信号
        self.ui.toolButton_preview_single.clicked.connect(
            lambda: self._click_preview_button('mode_1'))
        self.ui.toolButton_preview_double.clicked.connect(
            lambda: self._click_preview_button('mode_2'))
        self.ui.toolButton_preview_v.clicked.connect(
            lambda: self._click_preview_button('mode_3'))
        self.ui.toolButton_preview_h.clicked.connect(
            lambda: self._click_preview_button('mode_4'))

    def set_wait_thread(self, thread: ThreadWaitTime):
        """设置延迟线程"""
        self.thread_wait = thread
        self.thread_wait.signal_start.connect(self.show)
        self.thread_wait.signal_end.connect(self.hide)

    def _load_setting(self):
        """加载设置"""
        self._mode_preview = GetSetting.current_view_mode_eng()
        self._change_preview_mode()

    def _click_preview_button(self, mode: str):
        """点击预览视图按钮"""
        function_normal.print_function_info()
        if self._mode_preview != mode:
            self._mode_preview = mode
            self._change_preview_mode()

    def _change_preview_mode(self):
        """改变预览模式"""
        function_normal.print_function_info()
        # 修改图标
        self.update_icon()
        # 修改设置
        ResetSetting.current_view_mode(self._mode_preview)
        # 发送信号
        self.signal_preview_mode_changed.emit()

    def update_icon(self, preview_mode=None):
        self._reset_icon_preview_button()
        if not preview_mode:
            preview_mode = self._mode_preview
        if preview_mode == 'mode_1':
            self.ui.toolButton_preview_single.setIcon(
                QIcon(_ICON_SINGLE_PAGE_RED))
        elif preview_mode == 'mode_2':
            self.ui.toolButton_preview_double.setIcon(
                QIcon(_ICON_DOUBLE_PAGE_RED))
        elif preview_mode == 'mode_3':
            self.ui.toolButton_preview_v.setIcon(
                QIcon(_ICON_SCROLL_VERTICAL_RED))
        elif preview_mode == 'mode_4':
            self.ui.toolButton_preview_h.setIcon(
                QIcon(_ICON_SCROLL_HORIZONTAL_RED))

    def _reset_icon_preview_button(self):
        """设置按钮图标"""
        self.ui.toolButton_preview_single.setIcon(QIcon(_ICON_SINGLE_PAGE))
        self.ui.toolButton_preview_double.setIcon(QIcon(_ICON_DOUBLE_PAGE))
        self.ui.toolButton_preview_v.setIcon(QIcon(_ICON_SCROLL_VERTICAL))
        self.ui.toolButton_preview_h.setIcon(QIcon(_ICON_SCROLL_HORIZONTAL))

    def _reset_button_size(self):
        """设置按钮的大小"""
        self.ui.toolButton_preview_single.setMinimumSize(24, 24)
        self.ui.toolButton_preview_double.setMinimumSize(24, 24)
        self.ui.toolButton_preview_v.setMinimumSize(24, 24)
        self.ui.toolButton_preview_h.setMinimumSize(24, 24)

    def eventFilter(self, obj, event):
        if event.type() == event.Enter:
            if not self.thread_wait.isRunning():
                self.thread_wait.start()
            self.thread_wait.enable_loop()
        elif event.type() == event.Leave:
            self.thread_wait.reset_end_time()
            self.thread_wait.disable_loop()
            if not self.thread_wait.isRunning():
                self.thread_wait.start()
        return super().eventFilter(obj, event)
