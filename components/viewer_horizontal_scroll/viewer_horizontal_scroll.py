import lzytools._qt_pyside6
from PySide6.QtWidgets import *

from components.label_image import LabelImage
from components.viewer_frame import ViewerFrame


class ViewerHorizontalScroll(ViewerFrame):
    """预览控件——横向卷轴"""

    def __init__(self, parent=None):
        super().__init__(parent)


if __name__ == '__main__':
    app = QApplication()
    ui = ViewerHorizontalScroll()
    ui.show()
    app.exec()