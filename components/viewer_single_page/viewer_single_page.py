import lzytools._qt_pyside6
from PySide6.QtWidgets import *

from components.label_image import LabelImage
from components.viewer_frame import ViewerFrame


class ViewerSinglePage(ViewerFrame):
    """预览控件——单页"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # 设置图片显示控件
        self.label_image = LabelImage()
        self.layout.addWidget(self.label_image)



if __name__ == '__main__':
    app = QApplication()
    ui = ViewerSinglePage()
    ui.show()
    app.exec()