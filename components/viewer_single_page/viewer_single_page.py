from PySide6.QtWidgets import *

from common.size_mode import PageSizeMode
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

    def set_comic(self, comic_path: str):
        """设置漫画类
        :param comic_path: 漫画路径"""
        super().set_comic(comic_path)
        self.show_image()

    def show_image(self):
        self.label_image.set_image(self.comic.image_list[self.page_index - 1])

    def previous_page(self):
        if self.page_index > 1:
            self.page_index -= 1
            self.show_image()

    def next_page(self):
        if self.page_index < self.comic.page_count:
            self.page_index += 1
            self.show_image()

    def keep_size(self):
        super().keep_size()
        self.label_image.update_image_size(PageSizeMode.Fixed)

    def fit_width(self):
        super().fit_width()
        self.label_image.update_image_size(PageSizeMode.FitWidth, self.size().width())

    def fit_height(self):
        super().fit_height()
        self.label_image.update_image_size(PageSizeMode.FitHieght, self.size().height())

    def fit_widget(self):
        super().fit_widget()
        self.label_image.update_image_size(PageSizeMode.FitPage, self.size())

    def full_size(self):
        super().full_size()
        self.label_image.update_image_size(PageSizeMode.FullSize)

    def zoom_in(self):
        super().zoom_in()
        self.label_image.zoom_in()

    def zoom_out(self):
        super().zoom_in()
        self.label_image.zoom_out()

    def rotate_left(self):
        super().rotate_left()
        self.label_image.rotate_left()
        self._update_image_size()

    def rotate_right(self):
        super().rotate_right()
        self.label_image.rotate_right()
        self._update_image_size()


if __name__ == '__main__':
    app = QApplication()
    ui = ViewerSinglePage()
    ui.show()
    app.exec()
