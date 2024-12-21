import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QPoint


class FloatingWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 可选，设置透明背景
        self.setFixedSize(100, 50)
        self.label = QLabel("悬浮控件 A", self)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 200);")  # 设置背景颜色
        self.label.setAlignment(Qt.AlignCenter)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("悬浮控件示例")

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.labelB = QLabel("控件 B，调整大小", self)
        self.labelB.setStyleSheet("background-color: lightgray;")
        self.layout.addWidget(self.labelB)

        self.floatingWidget = FloatingWidget(self)

        # 当控件 B 的大小改变时更新浮动控件的位置
        self.labelB.resizeEvent = self.updateFloatingWidgetPosition

        # 初始位置
        self.updateFloatingWidgetPosition()

    def updateFloatingWidgetPosition(self, event=None):
        # 获取控件 B 的位置和大小
        b_rect = self.labelB.geometry()
        # 设置浮动控件 A 的位置
        new_x = b_rect.x() + (b_rect.width() - self.floatingWidget.width()) / 2
        new_y = b_rect.y() - self.floatingWidget.height()  # 控件 B 之上
        self.floatingWidget.move(new_x, new_y)
        self.floatingWidget.show()  # 确保浮动控件显示


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.resize(300, 200)
    mainWin.show()
    sys.exit(app.exec())