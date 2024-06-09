# 实现平滑滚动的scrollArea
# 滚轮的平滑滚动：二次缓出动画曲线。
# 自动播放的平滑滚动：滚动到滑动条底部，按预计滚动距离/预设滚动速度计算出动画总时长，动画曲线为线性。
# 自动播放时，使用滚轮则中断自动播放，并切换动画曲线；切换自动播放速度时，暂停动画，重新计算预计动画时长后重新设置并启动动画。

from PySide6.QtCore import Signal, QEasingCurve, QPropertyAnimation
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QScrollBar, QScrollArea


class ScrollAreaSmooth(QScrollArea):
    """实现平滑滚动的scrollArea"""
    signal_stop_autoplay = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        # 替换滚动条
        self.scrollbar_h = ScrollBarSmooth()
        self.scrollbar_v = ScrollBarSmooth()
        self.scrollbar_h.setOrientation(Qt.Horizontal)
        self.scrollbar_v.setOrientation(Qt.Vertical)
        self.setVerticalScrollBar(self.scrollbar_v)
        self.setHorizontalScrollBar(self.scrollbar_h)

    def set_direction(self, reverse:bool):
        """设置方向"""
        self.scrollbar_h.set_direction(reverse)
        self.scrollbar_v.set_direction(reverse)
    def start_autoplay(self, speed):
        if self.scrollbar_h.isVisible():
            self.scrollbar_h.start_autoplay(speed)
        elif self.scrollbar_v.isVisible():
            self.scrollbar_v.start_autoplay(speed)

    def stop_autoplay(self):
        self.scrollbar_h.quit_autoplay()
        self.scrollbar_v.quit_autoplay()

    def wheelEvent(self, e):
        self.stop_autoplay()
        self.signal_stop_autoplay.emit()
        if self.scrollbar_h.isVisible():
            self.scrollbar_h.scroll_value(-e.angleDelta().y())
        elif self.scrollbar_v.isVisible():
            self.scrollbar_v.scroll_value(-e.angleDelta().y())


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

    def set_direction(self, reverse:bool):
        """设置方向"""
        self.reverse = reverse

    def start_autoplay(self, speed):
        """开始自动播放"""
        if self._last_speed == speed:
            return
        else:
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
        self._last_speed = None
        self.animal.stop()
        self.animal.setEasingCurve(QEasingCurve.OutQuad)
        self.animal.setDuration(self._default_animal_duration)

    def setValue(self, value: int):
        if value == self.value():
            return

        # 停止动画
        self.animal.stop()
        self.signal_scroll_end.emit()

        # 重新开始动画
        self.animal.setStartValue(self.value())
        self.animal.setEndValue(value)
        self.animal.start()

    def scroll_value(self, value: int):
        """滚动指定距离"""
        value += self.value()
        self._scroll_to_value(value)

    def _scroll_to_value(self, value: int):
        """滚动到指定位置"""
        value = min(self.maximum(), max(self.minimum(), value))  # 防止超限
        self.setValue(value)

    def mousePressEvent(self, e):
        self.animal.stop()
        super().mousePressEvent(e)

    def mouseReleaseEvent(self, e):
        self.animal.stop()
        super().mouseReleaseEvent(e)

    def mouseMoveEvent(self, e):
        self.animal.stop()
        super().mouseMoveEvent(e)
