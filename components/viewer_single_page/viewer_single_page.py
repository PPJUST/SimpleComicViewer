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

        # 设置参数
        self.page_index = 1  # 当前显示的页码（从1开始）
        self.page_size_mode = None  #

    def set_comic(self, comic_path: str):
        """设置漫画类
        :param comic_path: 漫画路径"""
        super().set_comic(comic_path)
        self.show_image()

    def show_image(self):
        """显示图片"""
        self.label_image.set_image(self.comic.image_list[self.page_index - 1])

    def previous_page(self):
        """上一页"""
        if self.page_index > 1:
            self.page_index -= 1
            self.show_image()

    def next_page(self):
        """下一页"""
        if self.page_index < self.comic.page_count:
            self.page_index += 1
            self.show_image()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.label_image._image_size_fit_height(self.size().height())

if __name__ == '__main__':
    app = QApplication()
    ui = ViewerSinglePage()
    ui.show()
    app.exec()
