from PySide6.QtCore import Signal, Qt, QEasingCurve
from PySide6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout
from lzytools._qt_pyside6 import ScrollBarSmooth

from common.comic_info import ComicInfo
from common.image_info import ImageInfo
from common.mode_image_size import ModeImageSize
from components.label_image import LabelImage
from components.viewer_frame import ViewerFrame


class ViewerScrollFrame(ViewerFrame):
    """卷轴模式框架"""
    imageInfoShowed = Signal(ImageInfo, name='当前显示的图片信息类')

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
        previous_index = self.page_index - 1
        spacing = self.layout.spacing()

        # 计算第一个label顶部/左端到上一个label底部/右端的高度/宽度（即上二个label底部/右端+间隔）
        total = 0
        for i in range(previous_index - 1):
            label = self.layout.itemAt(i).widget()
            if isinstance(self.layout, QHBoxLayout):  # 横向布局找宽度
                total += label.width() + spacing
            elif isinstance(self.layout, QVBoxLayout):  # 纵向布局找高度
                total += label.height() + spacing

        self.scrollbar.setValue(total)

    def next_page(self):
        super().next_page()
        previous_index = self.page_index + 1
        spacing = self.layout.spacing()

        # 计算第一个label顶部到下一个label顶部的高度（即当前label底部+间隔）
        # 计算第一个label顶部/左端到下一个label底部/右端的高度/宽度（即当前label底部/右端+间隔）
        total = 0
        for i in range(previous_index - 1):
            label = self.layout.itemAt(i).widget()
            if isinstance(self.layout, QHBoxLayout):  # 横向布局找宽度
                total += label.width() + spacing
            elif isinstance(self.layout, QVBoxLayout):  # 纵向布局找高度
                total += label.height() + spacing

        self.scrollbar.setValue(total)

    def keep_width(self):
        super().keep_width()
        for i in range(self.layout.count()):
            label: LabelImage = self.layout.itemAt(i).widget()
            label.show_image(ModeImageSize.Fixed)

    def keep_width_single_page(self, label: LabelImage):
        """更新单页大小"""
        label.show_image(ModeImageSize.Fixed)

    def fit_width(self):
        super().fit_width()
        for i in range(self.layout.count()):
            label: LabelImage = self.layout.itemAt(i).widget()
            label.show_image(ModeImageSize.FitWidth, self.size().width())

    def fit_width_single_page(self, label: LabelImage):
        """更新单页大小"""
        label.show_image(ModeImageSize.FitWidth, self.size().width())

    def fit_height(self):
        super().fit_height()
        for i in range(self.layout.count()):
            label: LabelImage = self.layout.itemAt(i).widget()
            label.show_image(ModeImageSize.FitWidth, self.size().height())

    def fit_height_single_page(self, label: LabelImage):
        """更新单页大小"""
        label.show_image(ModeImageSize.FitWidth, self.size().height())

    def zoom_in(self):
        super().zoom_in()
        for i in range(self.layout.count()):
            label: LabelImage = self.layout.itemAt(i).widget()
            label.zoom_in()

    def zoom_out(self):
        super().zoom_in()
        for i in range(self.layout.count()):
            label: LabelImage = self.layout.itemAt(i).widget()
            label.zoom_out()

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

    def autoplay_start(self):
        # 设置滚动动画为线性
        self.scrollbar.set_scroll_type_liner()
        # 根据播放速度，计算滑动到底部/右端所需时间
        scroll_distance = self.scrollbar.maximum() - self.scrollbar.value()
        speed = self.speed_autoplay * 100  # 100倍率
        animal_duration = int(scroll_distance / speed)
        self.scrollbar.set_animal_duration(animal_duration * 1000)
        # 开始滑动
        self.scrollbar._scroll_to_value(self.scrollbar.maximum())

    def is_autoplay_running(self):
        # 通过判断滑动动画来判断是否正在进行自动播放
        if self.scrollbar.animal.easingCurve().type() == QEasingCurve.Linear:
            return True
        else:
            return False

    def set_autoplay_speed(self, add_speed: float):
        super().set_autoplay_speed(add_speed)
        # 卷轴视图时需要重新开始自动播放才能刷新播放速度
        if self.is_autoplay_running:
            self.autoplay_stop()
            self.autoplay_start()

    def reset_autoplay_speed(self):
        super().reset_autoplay_speed()
        # 卷轴视图时需要重新开始自动播放才能刷新播放速度
        if self.is_autoplay_running:
            self.autoplay_stop()
            self.autoplay_start()

    def autoplay_stop(self):
        # 还原滚动动画
        self.scrollbar.set_scroll_type_smooth()
        # 还原滚动动画时间
        self.scrollbar.animal.setDuration(400)
        # 停止滑动
        self.scrollbar.scroll_value(0)

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

    def wheelEvent(self, event):
        self.scrollbar.scroll_value(-event.angleDelta().y())


if __name__ == '__main__':
    app = QApplication()
    ui = ViewerScrollFrame()
    ui.show()
    app.exec()
