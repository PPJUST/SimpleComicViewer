# 支持右键点击信号和自动隐藏事件的button

from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QToolButton

from ui.thread_wait_time import ThreadWaitTime


class ToolButtonRightClickAndHidden(QToolButton):
    """支持右键点击信号和自动隐藏事件的button"""
    rightClicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.setMouseTracking(True)
        self.setMinimumSize(24, 24)
        self.customContextMenuRequested.connect(self._send_right_click_signal)

        # 设置延迟隐藏的子线程
        self.thread_wait = None

    def set_wait_thread(self, thread: ThreadWaitTime):
        """设置延迟线程"""
        self.thread_wait = thread
        self.thread_wait.signal_start.connect(self.show)
        self.thread_wait.signal_end.connect(self.hide)

    def set_icon(self, icon):
        self.setIcon(QIcon(icon))

    def _send_right_click_signal(self):
        """发送右键点击信号"""
        self.rightClicked.emit()

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
