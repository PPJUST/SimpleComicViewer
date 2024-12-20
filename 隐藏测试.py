from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *



def  set_auto_hidden(widget:QWidget):
    """设置控件属性：悬停时显示，离开时隐藏"""


    # 设置计时器
    widget.qtimer_hidden = QTimer()
    widget.qtimer_hidden.setInterval(500)
    widget.qtimer_hidden.setSingleShot(True)
    widget.qtimer_hidden.timeout.connnect(widget.hide)

    def set_interval(self, second: float):
        """设置延迟隐藏的时间间隔"""
        self.qtimer_hidden.setInterval(int(second * 1000))

    def enterEvent(self, event):
        super().enterEvent(event)
        self.show()

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.qtimer_hidden.start()
