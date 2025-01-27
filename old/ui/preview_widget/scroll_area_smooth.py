# 实现平滑滚动的scrollArea
# 滚轮的平滑滚动：二次缓出动画曲线。
# 自动播放的平滑滚动：滚动到滑动条底部，按预计滚动距离/预设滚动速度计算出动画总时长，动画曲线为线性。
# 自动播放时，使用滚轮则中断自动播放，并切换动画曲线；切换自动播放速度时，暂停动画，重新计算预计动画时长后重新设置并启动动画。



class ScrollBarSmooth(QScrollBar):
    """实现平滑滚动的滚动条（在两个value间插值）"""
    signal_scroll_end = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._last_speed = None
        self._default_animal_duration = 400

        # 设置插值动画
        self.animal = QPropertyAnimation()
        self.animal.setTargetObject(self)
        self.animal.setPropertyName(b"value")
        self.animal.setEasingCurve(QEasingCurve.OutQuad)  # 设置动画的缓动曲线为二次缓出
        self.animal.setDuration(self._default_animal_duration)  # 动画时间 毫秒
        self.animal.finished.connect(self.signal_scroll_end.emit)

        # 设置方向
        self.reverse = False

    def set_direction(self, reverse: bool):
        """设置方向"""
        self.reverse = reverse

    def start_autoplay(self, speed):
        """开始自动播放"""
        if self._last_speed == speed:
            return
        else:
            self.setEnabled(False)  # 开始自动播放后禁用滚动条，防止滚动事件与自动播放事件冲突
            self._last_speed = speed
            self.animal.stop()
            self.animal.setEasingCurve(QEasingCurve.Linear)
            if self.reverse:
                calc_duration = int((self.value() - 0) / (1 / speed * 100) * 1000)
                self.animal.setDuration(calc_duration)
                self.setValue(0)
            else:
                calc_duration = int((self.maximum() - self.value()) / (1 / speed * 100) * 1000)
                self.animal.setDuration(calc_duration)
                self.setValue(self.maximum())

    def quit_autoplay(self):
        """退出自动播放"""
        self.setEnabled(True)
        self._last_speed = None
        self.animal.stop()
        self.animal.setEasingCurve(QEasingCurve.OutQuad)
        self.animal.setDuration(self._default_animal_duration)

