from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication

from common.comic_info import ComicInfo
from common.image_info import ImageInfo
from common.mode_image_size import ModeImageSize
from components.label_image import LabelImage
from components.viewer_frame import ViewerFrame


class ViewerVerticalScroll(ViewerFrame):
    """预览控件——纵向卷轴"""
    imageInfoShowed = Signal(ImageInfo, name='当前显示的图片信息类')

    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置参数

    def set_comic(self, comic_info: ComicInfo):
        """设置漫画类
        :param comic_info: ComicInfo类"""
        super().set_comic(comic_info)
        self._add_labels()
        self.show_image()

    def _add_labels(self):
        """添加指定个数的图片label"""
        for image_path in self.comic_info.image_list:
            label_image = LabelImage()
            angle = self.comic_info.get_rotate_angle(image_path)  # 旋转角度
            image_info = ImageInfo(self.comic_info, image_path)  # 图片信息类
            label_image.set_image(image_info, angle)
            self.layout.addWidget(label_image)


    def show_image(self):
        self._update_image_size()

    def previous_page(self):
        # 备忘录 直接跳转上一页
        pass

    def next_page(self):
        # 备忘录 直接跳转下一页
        pass

    def keep_width(self):
        super().keep_width()
        for i in range(self.layout.count()):
            label:LabelImage = self.layout.itemAt(i).widget()
            label.show_image(ModeImageSize.Fixed)

    def keep_width_single_page(self, label:LabelImage):
        """更新单页大小"""
        label.show_image(ModeImageSize.Fixed)
    def fit_width(self):
        super().fit_width()
        for i in range(self.layout.count()):
            label:LabelImage = self.layout.itemAt(i).widget()
            label.show_image(ModeImageSize.FitWidth, self.size().width())

    def fit_width_single_page(self, label:LabelImage):
        """更新单页大小"""
        label.show_image(ModeImageSize.FitWidth, self.size().width())


    def zoom_in(self):
        super().zoom_in()
        for i in range(self.layout.count()):
            label:LabelImage = self.layout.itemAt(i).widget()
            label.zoom_in()


    def zoom_out(self):
        super().zoom_in()
        for i in range(self.layout.count()):
            label:LabelImage = self.layout.itemAt(i).widget()
            label.zoom_out()

    def rotate_left(self):
        super().rotate_left()
        # 获取当前页码的Label
        label :LabelImage= None
        # 显示旋转后的图片
        label.rotate_left()
        if self.page_size_mode is ModeImageSize.Fixed:
            self.keep_width_single_page(label)
        elif self.page_size_mode is ModeImageSize.FitWidth:
            self.fit_width_single_page(label)
        # 更新角度字典
        current_image_path = label.image_info.path
        self.comic_info.update_rotate_angle(current_image_path, -90)

    def rotate_right(self):
        super().rotate_right()
        # 获取当前页码的Label
        label :LabelImage= None
        # 显示旋转后的图片
        label.rotate_right()
        if self.page_size_mode is ModeImageSize.Fixed:
            self.keep_width_single_page(label)
        elif self.page_size_mode is ModeImageSize.FitWidth:
            self.fit_width_single_page(label)
        # 更新角度字典
        current_image_path = label.image_info.path
        self.comic_info.update_rotate_angle(current_image_path, 90)
    def clear(self):
        super().clear()
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

if __name__ == '__main__':
    app = QApplication()
    ui = ViewerVerticalScroll()
    ui.show()
    app.exec()
