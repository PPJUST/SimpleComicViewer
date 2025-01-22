from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication

from common.comic_info import ComicInfo
from common.image_info import ImageInfo
from common.mode_image_size import ModeImageSize
from components.label_image import LabelImage
from components.viewer_frame import ViewerFrame


class ViewerSinglePage(ViewerFrame):
    """预览控件——单页"""
    imageInfoShowed = Signal(ImageInfo, name='当前显示的图片信息类')

    def __init__(self, parent=None):
        super().__init__(parent)
        # 设置图片显示控件
        self.label_image = LabelImage()
        self.layout.addWidget(self.label_image)

        # 设置参数

    def set_comic(self, comic_info: ComicInfo):
        """设置漫画类
        :param comic_info: ComicInfo类"""
        super().set_comic(comic_info)
        self.show_image()

    def show_image(self):
        image_path = self.comic_info.image_list[self.page_index - 1]
        angle = self.comic_info.get_rotate_angle(image_path)  # 旋转角度
        image_info = ImageInfo(self.comic_info, image_path)  # 图片信息类
        image_info.set_page_index(self.page_index)
        self.label_image.set_image(image_info, angle)
        self._update_image_size()

        self.imageInfoShowed.emit(image_info)

    def previous_page(self):
        if self.page_index > 1:
            self.page_index -= 1
            self.show_image()

    def next_page(self):
        if self.page_index < self.comic_info.page_count:
            self.page_index += 1
            self.show_image()

    def keep_width(self):
        super().keep_width()
        self.label_image.show_image(ModeImageSize.Fixed)

    def fit_width(self):
        super().fit_width()
        self.label_image.show_image(ModeImageSize.FitWidth, self.size().width())

    def fit_height(self):
        super().fit_height()
        self.label_image.show_image(ModeImageSize.FitHeight, self.size().height())

    def fit_widget(self):
        super().fit_widget()
        self.label_image.show_image(ModeImageSize.FitPage, self.size())

    def full_size(self):
        super().full_size()
        self.label_image.show_image(ModeImageSize.FullSize)

    def zoom_in(self):
        super().zoom_in()
        self.label_image.zoom_in()

    def zoom_out(self):
        super().zoom_in()
        self.label_image.zoom_out()

    def rotate_left(self):
        super().rotate_left()
        # 显示旋转后的图片
        self.label_image.rotate_left()
        self._update_image_size()
        # 更新角度字典
        current_image_path = self.comic_info.image_list[self.page_index - 1]
        self.comic_info.update_rotate_angle(current_image_path, -90)

    def rotate_right(self):
        super().rotate_right()
        # 显示旋转后的图片
        self.label_image.rotate_right()
        self._update_image_size()
        # 更新角度字典
        current_image_path = self.comic_info.image_list[self.page_index - 1]
        self.comic_info.update_rotate_angle(current_image_path, 90)


if __name__ == '__main__':
    app = QApplication()
    ui = ViewerSinglePage()
    ui.show()
    app.exec()
