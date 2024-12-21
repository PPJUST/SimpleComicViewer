# 播放等待动画的dialog

from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QDialog

from constant import _ICON_WAIT_GIF
from ui.ui_src.ui_dialog_wait_animation import Ui_Dialog


class DialogWaitAnimation(QDialog):
    """播放等待动画的dialog"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 添加动图对象
        self.movie_icon = QMovie(_ICON_WAIT_GIF)  # 动图对象，用于显示GIF
        self.ui.label.setMovie(self.movie_icon)

    def play(self):
        self.movie_icon.start()
        self.show()

    def stop(self):
        self.movie_icon.stop()
        self.close()
