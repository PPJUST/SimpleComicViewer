from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout
from lzytools._qt_pyside6 import ScrollBarSmooth

from common.comic_info import ComicInfo
from common.image_info import ImageInfo
from common.mode_image_size import ModeImageSize
from components.label_image import LabelImage
from components.viewer_frame import ViewerFrame

_PRELOAD_PAGE = 5


class _ViewerScrollFrame(ViewerFrame):
    """卷轴模式框架"""

    def __init__(self, parent=None, layout='horizontal'):
        super().__init__(parent, layout)
        # 替换滑动条
        self.scrollbar = ScrollBarSmooth(self)
        if isinstance(self.layout, QHBoxLayout):
            self.scrollbar.setOrientation(Qt.Horizontal)
            self.setHorizontalScrollBar(self.scrollbar)
        elif isinstance(self.layout, QVBoxLayout):
            self.scrollbar.setOrientation(Qt.Vertical)
            self.setVerticalScrollBar(self.scrollbar)
        # 绑定滑动条信号
        self.scrollbar.valueChanged.connect(self._index_changed)
        self.scrollbar.MoveFinished.connect(self._reset_scroll_arg)

        # 设置参数
        self._base_index = 1  # 卷轴视图特殊使用，初始滚动时的对应页码
        self._change_index = 0  # 卷轴视图特殊使用，滚动变更的页码

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
            self.layout.addWidget(label_image, alignment=Qt.AlignmentFlag.AlignCenter)

    def show_image(self):
        super().show_image()
        self._update_size()

        self._index_changed()

    def previous_page(self):
        super().previous_page()
        self._change_index -= 1
        previous_index = self._base_index + self._change_index

        self._move_to_page(previous_index)

    def next_page(self):
        super().next_page()
        self._change_index += 1
        previous_index = self._base_index + self._change_index

        self._move_to_page(previous_index)

    def _move_to_page(self, page: int):
        """移动到指定页码"""
        # 处理超限
        if page < 1:
            page = 1
            self._reset_scroll_arg()
        elif page > self.comic_info.page_count:
            page = self.comic_info.page_count
            self._reset_scroll_arg()

        # 移动到指定页码
        spacing = self.layout.spacing()
        total = 0
        for i in range(page - 1):
            label = self.layout.itemAt(i).widget()
            if isinstance(self.layout, QHBoxLayout):  # 横向布局找宽度
                total += label.width() + spacing
            elif isinstance(self.layout, QVBoxLayout):  # 纵向布局找高度
                total += label.height() + spacing

        self.scrollbar.setValue(total)

    def keep_width(self):
        super().keep_width()
        preload_range = self.calc_preload_range()
        for i in range(self.layout.count()):
            label: LabelImage = self.layout.itemAt(i).widget()
            if i + 1 in preload_range:  # i为索引，range为页码范围，需要+1
                label.set_label_size(ModeImageSize.Fixed, self.size())  # 修改label大小并显示图片
            else:
                label.set_label_size(ModeImageSize.Fixed, self.size(), is_show_image=False)  # 修改label大小但不显示图片

    def keep_width_single_page(self, label: LabelImage):
        """更新单页尺寸"""
        label.set_label_size(ModeImageSize.Fixed, self.size())

    def fit_width(self):
        super().fit_width()
        preload_range = self.calc_preload_range()
        for i in range(self.layout.count()):
            label: LabelImage = self.layout.itemAt(i).widget()
            if i + 1 in preload_range:  # i为索引，range为页码范围，需要+1
                label.set_label_size(ModeImageSize.FitWidth, self.size())  # 修改label大小并显示图片
            else:
                label.set_label_size(ModeImageSize.FitWidth, self.size(), is_show_image=False)  # 修改label大小但不显示图片

    def fit_width_single_page(self, label: LabelImage):
        """更新单页尺寸"""
        label.set_label_size(ModeImageSize.FitWidth, self.size())

    def fit_height(self):
        super().fit_height()
        preload_range = self.calc_preload_range()
        for i in range(self.layout.count()):
            label: LabelImage = self.layout.itemAt(i).widget()
            if i + 1 in preload_range:  # i为索引，range为页码范围，需要+1
                label.set_label_size(ModeImageSize.FitHeight, self.size())  # 修改label大小并显示图片
            else:
                label.set_label_size(ModeImageSize.FitHeight, self.size(), is_show_image=False)  # 修改label大小但不显示图片

    def fit_height_single_page(self, label: LabelImage):
        """更新单页尺寸"""
        label.set_label_size(ModeImageSize.FitHeight, self.size())

    def zoom_in(self):
        super().zoom_in()
        preload_range = self.calc_preload_range()
        for i in range(self.layout.count()):
            label: LabelImage = self.layout.itemAt(i).widget()
            if i + 1 in preload_range:  # i为索引，range为页码范围，需要+1
                label.zoom_in()  # 修改label大小并显示图片
            else:
                label.zoom_in(is_show_image=False)  # 修改label大小但不显示图片

    def zoom_out(self):
        super().zoom_in()
        preload_range = self.calc_preload_range()
        for i in range(self.layout.count()):
            label: LabelImage = self.layout.itemAt(i).widget()
            if i + 1 in preload_range:  # i为索引，range为页码范围，需要+1
                label.zoom_out()  # 修改label大小并显示图片
            else:
                label.zoom_out(is_show_image=False)  # 修改label大小但不显示图片

    def rotate_left(self):
        super().rotate_left()
        # 获取当前页码的Label
        label: LabelImage = self._get_first_showed_label()
        # 显示旋转后的图片
        label.rotate_left()
        if self.page_size_mode is ModeImageSize.Fixed:
            self.keep_width_single_page(label)
        elif self.page_size_mode is ModeImageSize.FitWidth:
            self.fit_width_single_page(label)
        elif self.page_size_mode is ModeImageSize.FitHeight:
            self.fit_height_single_page(label)
        # 更新角度字典
        current_image_path = label.image_info.path
        self.comic_info.update_rotate_angle(current_image_path, -90)

    def rotate_right(self):
        super().rotate_right()
        # 获取当前页码的Label
        label: LabelImage = self._get_first_showed_label()
        # 显示旋转后的图片
        label.rotate_right()
        if self.page_size_mode is ModeImageSize.Fixed:
            self.keep_width_single_page(label)
        elif self.page_size_mode is ModeImageSize.FitWidth:
            self.fit_width_single_page(label)
        elif self.page_size_mode is ModeImageSize.FitHeight:
            self.fit_height_single_page(label)
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

    def _get_first_showed_label(self):
        """获取页面上显示的第一个label"""
        spacing = self.layout.spacing()
        # 提取当前滑动条的值
        bar_value = self.scrollbar.value()
        # 遍历控件，提取滑动条值对应的label
        total = 0
        for i in range(self.layout.count()):
            label: LabelImage = self.layout.itemAt(i).widget()
            if isinstance(self.layout, QHBoxLayout):  # 横向布局找宽度
                label_height_or_width = label.width()
            elif isinstance(self.layout, QVBoxLayout):  # 纵向布局找高度
                label_height_or_width = label.height()
            if total <= bar_value < total + label_height_or_width + spacing:
                return label
            else:
                total += label_height_or_width + spacing

    def _index_changed(self):
        """显示的索引改变时发生信号"""
        current_label = self._get_first_showed_label()
        current_image = current_label.image_info
        current_index = current_image.page_index
        if current_index != self.page_index:
            self.page_index = current_index
            self.imageInfoShowed.emit(current_image)
            self._preload_images()

    def _preload_images(self):
        """预载图像"""
        preload_range = self.calc_preload_range()
        for i in range(self.layout.count()):
            label: LabelImage = self.layout.itemAt(i).widget()
            if i + 1 in preload_range:  # i为索引，range为页码范围，需要+1
                label.show_image()
            else:
                label.clear_image()

    def _reset_scroll_arg(self):
        """卷轴视图特殊使用，滚动动画结束后重置页码参数"""
        self._base_index = self.page_index
        self._change_index = 0

    def calc_preload_range(self) -> range:
        """计算预载页码范围
        :return: range(预载下限页码, 预载上限页码)"""
        range_left = int(self.page_index - _PRELOAD_PAGE / 2)
        range_right = int(self.page_index + _PRELOAD_PAGE / 2)
        # 处理超限
        if range_left < 1:
            range_right = range_right + (1 - range_left)
            range_left = 1
        if range_right > self.comic_info.page_count:
            range_right = self.comic_info.page_count

        return range(range_left, range_right + 1)


if __name__ == '__main__':
    app = QApplication()
    ui = _ViewerScrollFrame()
    ui.show()
    app.exec()
