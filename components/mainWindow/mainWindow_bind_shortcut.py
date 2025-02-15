from PySide6.QtCore import Qt
from PySide6.QtGui import QShortcut, QKeySequence

from components.mainWindow._mainWindow_viewer import _MainWindowViewer


class MainWindowShortcut(_MainWindowViewer):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 绑定快捷键
        # 切换上一页
        shortcut_1_1 = QShortcut(QKeySequence(Qt.Key_PageUp), self)
        shortcut_1_1.activated.connect(self._viewer_previous_page)
        shortcut_1_2 = QShortcut(QKeySequence(Qt.Key_Left), self)
        shortcut_1_2.activated.connect(self._viewer_previous_page)
        shortcut_1_3 = QShortcut(QKeySequence(Qt.Key_Up), self)
        shortcut_1_3.activated.connect(self._viewer_previous_page)
        # 切换下一页
        shortcut_1_4 = QShortcut(QKeySequence(Qt.Key_PageDown), self)
        shortcut_1_4.activated.connect(self._viewer_next_page)
        shortcut_1_5 = QShortcut(QKeySequence(Qt.Key_Right), self)
        shortcut_1_5.activated.connect(self._viewer_next_page)
        shortcut_1_6 = QShortcut(QKeySequence(Qt.Key_Down), self)
        shortcut_1_6.activated.connect(self._viewer_next_page)

        # 自动播放
        shortcut_2_1 = QShortcut(QKeySequence(Qt.Key_Space), self)
        shortcut_2_1.activated.connect(self._viewer_change_autoplay_state)
        shortcut_2_1 = QShortcut(QKeySequence(Qt.Key_Z), self)
        shortcut_2_1.activated.connect(lambda: self._viewer_set_autoplay_speed(-0.1))
        shortcut_2_1 = QShortcut(QKeySequence(Qt.Key_X), self)
        shortcut_2_1.activated.connect(self._viewer_reset_autoplay_speed)
        shortcut_2_1 = QShortcut(QKeySequence(Qt.Key_C), self)
        shortcut_2_1.activated.connect(lambda: self._viewer_set_autoplay_speed(0.1))
