# 主界面左上方的控制栏组件的子控件，用于中转子控件的信号和继承隐藏事件

from PySide6.QtCore import Signal
from PySide6.QtWidgets import *

from ui.thread_wait_time import ThreadWaitTime
from ui.widget_top_control_child import WidgetTopControlChild


class WidgetTopControl(QWidget):
    """主界面左上方的控制栏组件的子控件，用于中转子控件的信号和继承隐藏事件"""
    signal_preview_mode_changed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.widget = WidgetTopControlChild()
        self.layout.addWidget(self.widget)
        self.installEventFilter(self.widget)
        self.widget.raise_()  # 使该label显示在widget之上

        # 固定size大小，用于setGeometry方法设置相对位置
        self._size = self.sizeHint()

        # 中转子控件信号
        self.widget.signal_preview_mode_changed.connect(
            self.signal_preview_mode_changed.emit)

    def reset_xy(self, x: int, y: int):
        """重设坐标轴位置"""
        self.setGeometry(x, y, self._size.width(), self._size.height())

    def set_wait_thread(self, thread: ThreadWaitTime):
        """设置延迟线程"""
        self.widget.set_wait_thread(thread)
