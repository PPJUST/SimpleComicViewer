from PySide6.QtCore import QTimer, Signal

from components.viewer_frame._viewer_frame import _ViewerFrame

_MIN_SPEED = 0.1  # 限制的最慢自动播放速度
_MAX_SPEED = 5.0  # 限制的最快自动播放速度


class ViewerFrameAutoplay(_ViewerFrame):
    """预览控件框架"""
    StopAutoPlay = Signal(name='在自动播放运行时，进行手动翻页则停止自动播放')
    StartAutoPlay = Signal(name='自动播放开始信号')

    def __init__(self, parent=None, layout='horizontal'):
        super().__init__(parent, layout)
        # 设置自动播放计时器
        self.timer_autoplay = QTimer()  # 自动播放的计时器
        self.speed_autoplay: float = 1.0  # 自动播放的速度 n秒/页
        self.timer_autoplay.timeout.connect(self._next_page_autoplay)
        self.timer_autoplay.setInterval(int(self.speed_autoplay * 1000))

    def start_autoplay(self):
        """开始自动播放"""
        self.timer_autoplay.start()
        self.StartAutoPlay.emit()

    def is_autoplay_running(self) -> bool:
        """是否正在自动播放"""
        return self.timer_autoplay.isActive()

    def set_autoplay_speed(self, add_speed: float):
        """设置自动播放的速度
        :param add_speed: 1位小数，变动的自动播放速度"""
        self.speed_autoplay = round(self.speed_autoplay + add_speed, 1)
        # 处理超限
        if self.speed_autoplay < _MIN_SPEED:
            self.speed_autoplay = _MIN_SPEED
        if self.speed_autoplay > _MAX_SPEED:
            self.speed_autoplay = _MAX_SPEED

        self.timer_autoplay.setInterval(int(self.speed_autoplay * 1000))
        return self.speed_autoplay

    def reset_autoplay_speed(self):
        """重置自动播放的速度"""
        self.speed_autoplay = 1.0
        self.timer_autoplay.setInterval(int(self.speed_autoplay * 1000))
        return self.speed_autoplay

    def stop_autoplay(self):
        """停止自动播放"""
        self.timer_autoplay.stop()
        self.StopAutoPlay.emit()

    def _autoplay_end_when_bottom(self):
        """自动播放到尾页/底部时停止"""
        if self.page_index == self.comic_info.page_count:
            self.stop_autoplay()
            return False
        else:
            return True

    def _next_page_autoplay(self):
        """自动播放专用的下一页操作"""
        if self._autoplay_end_when_bottom():
            self.next_page()
