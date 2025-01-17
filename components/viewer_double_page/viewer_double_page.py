from PySide6.QtWidgets import QApplication

from components.label_image import LabelImage
from components.viewer_frame import ViewerFrame


class ViewerDoublePage(ViewerFrame):
    """预览控件——双页"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # 设置图片显示控件
        self.label_image_left = LabelImage()
        self.layout.addWidget(self.label_image_left)

        self.label_image_right = LabelImage()
        self.layout.addWidget(self.label_image_right)


if __name__ == '__main__':
    app = QApplication()
    ui = ViewerDoublePage()
    ui.show()
    app.exec()
