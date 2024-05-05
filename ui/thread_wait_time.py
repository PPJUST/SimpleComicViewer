# 等待指定时间后发送信号的的子线程
import time

from PySide6.QtCore import QThread, Signal

from module.function_config_get import GetSetting


class ThreadWaitTime(QThread):
    """等待指定时间后发送信号的的子线程"""
    signal_start = Signal()
    signal_end = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self._is_loop = False  # 是否循环
        self._WAIT_TIME = None  # 等待时间（秒）
        self._end_time = 0  # 发送结束信号的时间点
        self.load_setting()

    def load_setting(self):
        """加载设置"""
        self._WAIT_TIME = GetSetting.hide_wait_time()

    def run(self):
        self.signal_start.emit()
        self._end_time = time.time() + self._WAIT_TIME
        while True:
            time.sleep(0.1)
            if self._is_loop:
                continue
            current_time = time.time()
            if current_time > self._end_time:
                self.signal_end.emit()
                break

    def reset_end_time(self):
        """重置结束时间"""
        self._end_time = time.time() + self._WAIT_TIME

    def enable_loop(self):
        """开启循环"""
        self._is_loop = True

    def disable_loop(self):
        """关闭循环"""
        self._is_loop = False
