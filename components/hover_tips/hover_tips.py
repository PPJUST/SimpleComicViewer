import lzytools._qt_pyside6
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget, QApplication, QHBoxLayout


class HoverTips(QWidget):
    """显示操作提示信息（单例）"""

    _instance = None
    _is_init = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, parent=None):
        if not self._is_init:
            super().__init__(parent)
            self._is_init = True

            self.setFixedWidth(300)
            self.layout = QHBoxLayout(self)

            # 添加长文本控件（过长时隐藏超限部分为...）
            self.label_tips = lzytools._qt_pyside6.LabelHiddenOverLengthText()
            self.layout.addWidget(self.label_tips)

            # 添加显示隐藏定时器
            self.timer_showed = QTimer()
            self.timer_showed.setInterval(2000)
            self.timer_showed.setSingleShot(True)
            self.timer_showed.timeout.connect(self.hide)

            self.show_tips('启动测试')

    def show_tips(self, tips: str):
        """显示操作提示信息"""
        self.show()
        self.label_tips.setText(tips)
        self.timer_showed.start()


if __name__ == '__main__':
    app = QApplication()
    ui = HoverTips()
    ui.show()
    app.exec()
