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
        self.page_index = 1  # 当前显示的页码（从1开始）
        self.page_size_mode = None  # 显示模式（适合页面/适合宽度/适合高度/实际大小）

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

    def fit_width(self):
        if self.page_size_mode is not PageSizeMode.FitWidth:
            self.page_size_mode = PageSizeMode.FitWidth
        self.label_image.update_image_size(PageSizeMode.FitWidth,self.size().width())
    def fit_height(self):
        if self.page_size_mode is not PageSizeMode.FitHieght:
            self.page_size_mode = PageSizeMode.FitHieght
        self.label_image.update_image_size(PageSizeMode.FitHieght,self.size().height())
    def fit_widget(self):
        if self.page_size_mode is not PageSizeMode.FitPage:
            self.page_size_mode = PageSizeMode.FitPage
        self.label_image.update_image_size(PageSizeMode.FitPage,self.size())
    def full_size(self):
        if self.page_size_mode is not PageSizeMode.FullSize:
            self.page_size_mode = PageSizeMode.FullSize
        self.label_image.update_image_size(PageSizeMode.FullSize)


if __name__ == '__main__':
    app = QApplication()
    ui = ViewerSinglePage()
    ui.show()
    app.exec()
