from PySide6.QtCore import Signal, QSize
from PySide6.QtWidgets import QApplication

from common.comic_info import ComicInfo
from common.image_info import ImageInfo
from common.mode_image_size import ModeImageSize
from components.label_image import LabelImage
from components.viewer_frame import ViewerFrame


class ViewerDoublePage(ViewerFrame):
    """预览控件——双页"""
    imageInfoShowed = Signal(ImageInfo, name='当前显示的图片信息类')

    def __init__(self, parent=None):
        super().__init__(parent)
        # 设置图片显示控件
        self.label_image_left = LabelImage()
        self.layout.addWidget(self.label_image_left)
        self.label_image_right = LabelImage()
        self.layout.addWidget(self.label_image_right)

        # 设置参数
        self.page_size_mode = ModeImageSize.FitHeight

    def set_comic(self, comic_info: ComicInfo):
        """设置漫画类
        :param comic_info: ComicInfo类"""
        super().set_comic(comic_info)
        self.show_image()

    def show_image(self):
        super().show_image()
        # 设置左页
        image_path_left = self.comic_info.image_list[self.page_index - 1]
        angle = self.comic_info.get_rotate_angle(image_path_left)  # 旋转角度
        image_info_left = ImageInfo(self.comic_info, image_path_left)  # 图片信息类
        self.label_image_left.set_image(image_info_left, angle)
        # 设置右页
        image_path_right = self.comic_info.image_list[self.page_index]
        angle = self.comic_info.get_rotate_angle(image_path_right)  # 旋转角度
        image_info_right = ImageInfo(self.comic_info, image_path_right)  # 图片信息类
        self.label_image_right.set_image(image_info_right, angle)

        self._update_image_size()
        self.imageInfoShowed.emit(image_info_left)

    def previous_page(self):
        super().previous_page()
        if self.page_index > 1:
            self.page_index -= 2
            self.show_image()

    def next_page(self):
        super().next_page()
        if self.page_index < self.comic_info.page_count:
            self.page_index += 2
            self.show_image()

    def fit_height(self):
        super().fit_height()
        # 提取原始尺寸
        left_image_width, left_image_height = self.label_image_left.image_info.size
        right_image_width, right_image_height = self.label_image_right.image_info.size
        page_height = self.height()
        # 计算新宽度
        new_width_left = int(page_height / left_image_height * left_image_width)
        new_width_right = int(page_height / right_image_height * right_image_width)

        self.label_image_left.show_image(ModeImageSize.FitPage, QSize(new_width_left, page_height))
        self.label_image_right.show_image(ModeImageSize.FitPage, QSize(new_width_right, page_height))

    def fit_widget(self):
        super().fit_widget()
        # 双页逻辑：在页面上同时显示两张图片，先以统一其高度，然后保持纵横比计算最终的宽高
        # 提取原始尺寸
        left_image_width, left_image_height = self.label_image_left.image_info.size
        right_image_width, right_image_height = self.label_image_right.image_info.size
        page_height = self.height()
        page_width = self.width()
        # 计算两张图片统一高度时的新宽度
        temp_width_left = page_height / left_image_height * left_image_width
        temp_width_right = page_height / right_image_height * right_image_width
        joined_width = temp_width_left + temp_width_right
        # 计算新的高度
        new_height = int(page_width / joined_width * page_height)
        new_width_left = new_height / left_image_height * left_image_width
        new_width_right = new_height / right_image_height * right_image_width

        self.label_image_left.show_image(ModeImageSize.FitPage, QSize(new_width_left, new_height))
        self.label_image_right.show_image(ModeImageSize.FitPage, QSize(new_width_right, new_height))

    def clear(self):
        super().clear()
        self.label_image_left.clear()
        self.label_image_right.clear()

    def wheelEvent(self, event):
        """设置鼠标滚轮切页"""
        # 获取鼠标滚轮滚动的角度
        angle = event.angleDelta().y()
        # 根据角度的正负区分滚轮向上向下操作
        if angle > 0:  # 向上
            self.previous_page()
        else:  # 向下
            self.next_page()


if __name__ == '__main__':
    app = QApplication()
    ui = ViewerDoublePage()
    ui.show()
    app.exec()
