# 主界面下方的控制栏组件，用于中转子控件的信号和继承隐藏事件

from PySide6.QtCore import Signal
from PySide6.QtWidgets import *

from ui.thread_wait_time import ThreadWaitTime
from ui.widget_below_control_child import WidgetBelowControlChild


class WidgetBelowControl(QWidget):
    """主界面下方的控制栏组件，用于中转子控件的信号和继承隐藏事件"""
    signal_previous_page = Signal()
    signal_next_page = Signal()
    signal_open_list = Signal()
    signal_open_option = Signal()
    signal_previous_item = Signal()
    signal_next_item = Signal()
    signal_auto_play = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.widget = WidgetBelowControlChild()
        self.layout.addWidget(self.widget)
        self.installEventFilter(self.widget)
        self.widget.raise_()  # 使该label显示在widget之上

        # 固定size大小，用于setGeometry方法设置相对位置
        self._size = self.sizeHint()

        # 中转子控件信号
        self.widget.signal_previous_page.connect(
            self.signal_previous_page.emit)
        self.widget.signal_next_page.connect(self.signal_next_page.emit)
        self.widget.signal_previous_item.connect(
            self.signal_previous_item.emit)
        self.widget.signal_next_item.connect(self.signal_next_item.emit)
        self.widget.signal_open_list.connect(self.signal_open_list.emit)
        self.widget.signal_open_option.connect(self.signal_open_option.emit)
        self.widget.signal_auto_play.connect(self.signal_auto_play.emit)

    def reset_xy(self, x: int, y: int):
        """重设坐标轴位置"""
        self.setGeometry(x, y, self._size.width(), self._size.height())

    def set_wait_thread(self, thread: ThreadWaitTime):
        """设置延迟线程"""
        self.widget.set_wait_thread(thread)

    def reset_auto_play_state(self):
        """重置自动播放状态"""
        self.widget.reset_auto_play_state()
