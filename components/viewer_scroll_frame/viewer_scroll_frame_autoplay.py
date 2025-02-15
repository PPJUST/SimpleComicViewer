from PySide6.QtWidgets import QApplication

from components.viewer_scroll_frame._viewer_scroll_frame import _ViewerScrollFrame

_PRELOAD_PAGE = 5


class ViewerScrollFrameAutoplay(_ViewerScrollFrame):
    """卷轴模式框架"""

    def __init__(self, parent=None, layout='horizontal'):
        super().__init__(parent, layout)
        # 绑定滑动条信号
        self.scrollbar.AutoPlayStop.connect(self.StopAutoPlay.emit)

    def start_autoplay(self):
        # 根据播放速度，计算滑动到底部/右端所需时间
        scroll_distance = self.scrollbar.maximum() - self.scrollbar.value()
        speed = self.speed_autoplay * 100  # 100倍率
        animal_duration = int(scroll_distance / speed)
        self.scrollbar.set_type_linear(self.scrollbar.maximum(), animal_duration)
        self.StartAutoPlay.emit()

    def is_autoplay_running(self):
        return self.scrollbar.is_autoplay_running()

    def set_autoplay_speed(self, add_speed: float):
        super().set_autoplay_speed(add_speed)
        # 卷轴视图时需要重新开始自动播放才能刷新播放速度
        if self.is_autoplay_running():
            self.stop_autoplay()
            self.start_autoplay()

    def reset_autoplay_speed(self):
        super().reset_autoplay_speed()
        # 卷轴视图时需要重新开始自动播放才能刷新播放速度
        if self.is_autoplay_running:
            self.stop_autoplay()
            self.start_autoplay()

    def stop_autoplay(self):
        self.scrollbar.set_type_smooth()
        self.StopAutoPlay.emit()


if __name__ == '__main__':
    app = QApplication()
    ui = ViewerScrollFrameAutoplay()
    ui.show()
    app.exec()
