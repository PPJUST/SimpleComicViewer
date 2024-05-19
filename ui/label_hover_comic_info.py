# 自动隐藏的悬浮在其他控件左上角的文字信息label，用于显示漫画信息
from PySide6.QtWidgets import QLabel

from module.class_comic_info import ComicInfo


class LabelHoverComicInfo(QLabel):
    """自动隐藏的悬浮在其他控件左上角的文字信息label，用于显示漫画信息
    隐藏事件用法说明：
    hover_label = LabelHover(widget)
    widget.installEventFilter(hover_label)"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # ui设置
        self.setMouseTracking(True)
        self.setGeometry(10, 10, 200, 100)
        self.setStyleSheet("color: red;")
        self.setWordWrap(True)
        self.hide()

        # 初始化
        self._filename = ''
        self._current_page = 0
        self._total_page = 0

    def update_filename(self, text):
        """更新信息"""
        self._filename = text
        self._show_info()

    def update_current_page(self, value):
        """更新信息"""
        self._current_page = value
        self._show_info()

    def update_total_page(self, value):
        """更新信息"""
        self._total_page = value
        self._show_info()

    def update_info_by_comic(self, comic_info: ComicInfo):
        """通过ComicInfo类更新信息"""
        self._filename = comic_info.filename
        self._total_page = comic_info.page_count
        self._show_info()

    def _show_info(self):
        """显示信息"""
        text = f'{self._filename}\n{self._current_page}/{self._total_page}'
        self.setText(text)

    def eventFilter(self, obj, event):
        if event.type() == event.Enter:
            self.show()
            return True
        elif event.type() == event.Leave:
            self.hide()
            return True
        return super().eventFilter(obj, event)
