from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout
from lzytools._qt_pyside6 import ScrollBarSmooth
from common.comic_info import ComicInfo
from common.image_info import ImageInfo
from common.mode_image_size import ModeImageSize
from components.label_image import LabelImage
from components.viewer_frame import ViewerFrame


class ViewerVerticalScroll(ViewerFrame):
    """预览控件——纵向卷轴"""
    imageInfoShowed = Signal(ImageInfo, name='当前显示的图片信息类')

    def __init__(self, parent=None):
        super().__init__(parent,layout='vertical')
        # 替换滑动条
        self.scrollbar = ScrollBarSmooth(self)
        print(self.layout)
        if  isinstance(self.layout, QHBoxLayout) :
            print(1)
            self.scrollbar.setOrientation(Qt.Horizontal)
            self.setHorizontalScrollBar(self.scrollbar)
        elif isinstance(self.layout, QVBoxLayout)  :
            print(2)
            self.scrollbar.setOrientation(Qt.Vertical)
            self.setVerticalScrollBar(self.scrollbar)



        self.verticalScrollBar().valueChanged.connect(self._index_changed)

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
        super().show_image()
        self._update_image_size()

        self._index_changed()

    def previous_page(self):
        super().previous_page()
        previous_index = self.page_index-1
        spacing = self.layout.spacing()

        # 计算第一个label顶部到上一个label顶部的高度（即上二个label底部+间隔）
        previous_height = 0
        for i in range(previous_index-1):
            label = self.layout.itemAt(i).widget()
            previous_height += label.height()+spacing

        self.verticalScrollBar().setValue(previous_height)

    def next_page(self):
        super().next_page()
        previous_index = self.page_index + 1
        spacing = self.layout.spacing()

        # 计算第一个label顶部到下一个label顶部的高度（即当前label底部+间隔）
        previous_height = 0
        for i in range(previous_index - 1):
            label = self.layout.itemAt(i).widget()
            previous_height += label.height() + spacing

        self.verticalScrollBar().setValue(previous_height)

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
        label :LabelImage= self._get_first_showed_label()
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
        label :LabelImage= self._get_first_showed_label()
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

    def _get_first_showed_label(self):
        """获取页面上显示的第一个label"""
        spacing = self.layout.spacing()
        # 提取当前滑动条的值
        bar_value = self.verticalScrollBar().value()
        # 遍历控件，提取滑动条值对应的label
        height_total = 0
        for i in range(self.layout.count()):
            label:LabelImage = self.layout.itemAt(i).widget()
            height_label = label.height()
            if height_total <= bar_value < height_total+height_label + spacing:
                return label
            else:
                height_total += height_label +spacing

    def _index_changed(self):
        """显示的索引改变时发生信号"""
        current_label = self._get_first_showed_label()
        current_image = current_label.image_info
        current_index = current_image.page_index
        if current_index!= self.page_index:
            self.page_index = current_index
            self.imageInfoShowed.emit(current_image)
    def wheelEvent(self, event):
        self.scrollbar.scroll_value(-event.angleDelta().y())




if __name__ == '__main__':
    app = QApplication()
    ui = ViewerVerticalScroll()
    ui.show()
    app.exec()
