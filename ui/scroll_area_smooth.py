# 实现平滑滚动的scrollarea

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class ScrollAreaSmooth(QScrollArea):
    """平滑滚动的scrollarea"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # 替换滚动条
        self.scrollbar_h = ScrollBarSmooth()
        self.scrollbar_v = ScrollBarSmooth()
        self.scrollbar_h.setOrientation(Qt.Horizontal)
        self.scrollbar_v.setOrientation(Qt.Vertical)
        self.setVerticalScrollBar(self.scrollbar_v)
        self.setHorizontalScrollBar(self.scrollbar_h)

    def set_scroll_animation(self, direction, duration: int):
        """设置滚动动画持续时间
        :param direction: 滚动方向，Qt.Horizontal 或 Qt.Vertical
        :param duration: 滚动时间（动画时间）
        """
        scrollbar = self.scrollbar_h if direction == Qt.Horizontal else self.scrollbar_v
        scrollbar.animal.setDuration(duration)

    def set_animal_type_linear(self):
        self.scrollbar_h.set_animal_type_linear()
        self.scrollbar_v.set_animal_type_linear()

    def set_animal_type_outquad(self):
        self.scrollbar_h.set_animal_type_outquad()
        self.scrollbar_v.set_animal_type_outquad()

    def set_animal_duration(self, duration: float):
        self.scrollbar_h.set_animal_duration(duration)
        self.scrollbar_v.set_animal_duration(duration)

    def reset_animal_duration(self):
        self.scrollbar_h.reset_animal_duration()
        self.scrollbar_v.reset_animal_duration()

    def wheelEvent(self, e):
        if e.modifiers() == Qt.NoModifier:
            self.scrollbar_v.scroll_value(-e.angleDelta().y())
        else:
            self.scrollbar_h.scroll_value(-e.angleDelta().x())


class ScrollBarSmooth(QScrollBar):
    """实现平滑滚动的滚动条（在两个value间插值）"""
    signal_scroll_end = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # 设置插值动画
        self.animal = QPropertyAnimation()
        self.animal.setTargetObject(self)
        self.animal.setPropertyName(b"value")
        self.animal.setEasingCurve(QEasingCurve.OutQuad)  # 设置动画的缓动曲线为二次缓出
        self.animal.setDuration(400)  # 动画时间 毫秒
        self.animal.finished.connect(self.signal_scroll_end.emit)

    def set_animal_type_linear(self):
        """设置动画为线性变化"""
        self.animal.setEasingCurve(QEasingCurve.Linear)

    def set_animal_type_outquad(self):
        """设置动画为二次缓出"""
        self.animal.setEasingCurve(QEasingCurve.OutQuad)

    def set_animal_duration(self, duration: float):
        """设置动画时间"""
        self.animal.setDuration(int(duration*1000))  # 接收的单位是秒，*1000转为毫秒；+10是为了防止定时器的延迟问题导致动画启动时点延迟导致的不流畅
        print('self.animal.duration()', self.animal.duration())

    def reset_animal_duration(self):
        """重置动画时间"""
        self.animal.setDuration(400)

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
