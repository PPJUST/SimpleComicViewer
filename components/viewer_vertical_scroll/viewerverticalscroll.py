from PySide6.QtWidgets import QApplication

from components.viewer_frame import ViewerFrame


class ViewerVerticalScroll(ViewerFrame):
    """预览控件——纵向卷轴"""

    def __init__(self, parent=None):
        super().__init__(parent)


if __name__ == '__main__':
    app = QApplication()
    ui = ViewerVerticalScroll()
    ui.show()
    app.exec()
