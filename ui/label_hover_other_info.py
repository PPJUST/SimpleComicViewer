# 自动隐藏的悬浮在主页面左下角的文字信息label，用于操作提示等
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QLabel


class LabelHoverOtherInfo(QLabel):
    """自动隐藏的悬浮在主页面左下角的文字信息label，用于操作提示等"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # ui设置
        self.setMouseTracking(True)
        self.setGeometry(10, parent.height() - 20, 200, 20)
        self.setStyleSheet("color: blue;")
        self.setWordWrap(True)
        self.hide()

        # 延迟定时器，用于x秒后隐藏
        self.timer = QTimer()
        self.timer.setSingleShot(True)  # 设置单次触发
        self.timer.timeout.connect(self.hide)

    def show_information(self, text: str):
        """显示信息"""
        self.setText(text)
        self.show()
        self.timer.start(1000)  # 延迟500毫秒

    def reset_xy(self, x: int, y: int):
        """重设坐标轴位置"""
        self.setGeometry(x, y, 200, 20)
