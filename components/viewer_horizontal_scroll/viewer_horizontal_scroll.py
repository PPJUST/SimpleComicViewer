from PySide6.QtWidgets import QApplication

from components.viewer_scroll_frame import ViewerScrollFrame


class ViewerHorizontalScroll(ViewerScrollFrame):
    """预览控件——横向卷轴"""

    def __init__(self, parent=None):
        super().__init__(parent=parent, layout='horizontal')


if __name__ == '__main__':
    app = QApplication()
    ui = ViewerHorizontalScroll()
    ui.show()
    app.exec()
