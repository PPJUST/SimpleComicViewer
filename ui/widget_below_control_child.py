# 主界面下方的控制栏组件的子控件，用于编写隐藏事件

from PySide6.QtCore import Signal
from PySide6.QtWidgets import *

from constant import _ICON_ARROW_LEFT, _ICON_ARROW_RIGHT, _ICON_LIST, _ICON_OPTION, _ICON_PLAY, _ICON_STOP
from ui.thread_wait_time import ThreadWaitTime
from ui.ui_src.ui_widget_below_control_child import Ui_Form


class WidgetBelowControlChild(QWidget):
    """主界面下方的控制栏组件的子控件，用于编写隐藏事件"""
    signal_previous_page = Signal()  # 切换上一页
    signal_next_page = Signal()  # 切换下一页
    signal_open_list = Signal()  # 打开漫画列表
    signal_open_option = Signal()  # 打开设置
    signal_previous_item = Signal()  # 切换上一本漫画
    signal_next_item = Signal()  # 切换下一本漫画
    signal_auto_play = Signal(bool)  # 自动播放/自动滚动开关

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # ui设置
        self.setMouseTracking(True)
        self._reset_button_size()
        self._reset_icon()

        # 初始化
        self._load_setting()
        self._auto_play = False

        # 设置延迟隐藏的子线程
        self.thread_wait = None

        # 点击按钮后发送信号
        self.ui.toolButton_previous.clicked.connect(
            self.signal_previous_page.emit)
        self.ui.toolButton_next.clicked.connect(self.signal_next_page.emit)
        self.ui.toolButton_previous.rightClicked.connect(
            self.signal_previous_item.emit)
        self.ui.toolButton_next.rightClicked.connect(
            self.signal_next_item.emit)
        self.ui.toolButton_list.clicked.connect(self.signal_open_list.emit)
        self.ui.toolButton_option.clicked.connect(self.signal_open_option.emit)
        self.ui.toolButton_play.clicked.connect(self._change_auto_play_state)

        # 临时禁用按钮，暂时未做该功能 备忘录
        self.ui.toolButton_option.setEnabled(False)
        self.ui.toolButton_list.setEnabled(False)

    def set_wait_thread(self, thread: ThreadWaitTime):
        """设置延迟线程"""
        self.thread_wait = thread
        self.thread_wait.signal_start.connect(self.show)
        self.thread_wait.signal_end.connect(self.hide)

    def _load_setting(self):
        """加载设置"""
        pass

    def _change_auto_play_state(self):
        """自动播放开关状态"""
        self._auto_play = not self._auto_play
        self.signal_auto_play.emit(self._auto_play)
        self._update_play_icon()

    def reset_auto_play_state(self):
        """重置自动播放开关状态"""
        self._auto_play = False
        self._update_play_icon()

    def _reset_button_size(self):
        """设置按钮的大小"""
        self.ui.toolButton_previous.setMinimumSize(24, 24)
        self.ui.toolButton_play.setMinimumSize(24, 24)
        self.ui.toolButton_next.setMinimumSize(24, 24)
        self.ui.toolButton_option.setMinimumSize(24, 24)
        self.ui.toolButton_list.setMinimumSize(24, 24)

    def _reset_icon(self):
        """设置图标"""
        self.ui.toolButton_previous.set_icon(_ICON_ARROW_LEFT)
        self.ui.toolButton_play.set_icon(_ICON_PLAY)
        self.ui.toolButton_next.set_icon(_ICON_ARROW_RIGHT)
        self.ui.toolButton_option.set_icon(_ICON_OPTION)
        self.ui.toolButton_list.set_icon(_ICON_LIST)

    def _update_play_icon(self):
        """更新自动播放图标"""
        if self._auto_play:
            self.ui.toolButton_play.set_icon(_ICON_STOP)
        else:
            self.ui.toolButton_play.set_icon(_ICON_PLAY)

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
