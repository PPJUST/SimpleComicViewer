# 支持右键点击信号和自动隐藏事件的button

from thread.thread_wait_time import ThreadWaitTime
from ui.toolButton_right_click import ToolButtonRightClick


class ToolButtonRightClickAndHidden(ToolButtonRightClick):
    """支持右键点击信号和自动隐藏事件的button"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # 设置延迟隐藏的子线程
        self.thread_wait = ThreadWaitTime()
        self.thread_wait.signal_start.connect(self.show)
        self.thread_wait.signal_end.connect(self.hide)

    def eventFilter(self, obj, event):
        """隐藏事件"""
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
