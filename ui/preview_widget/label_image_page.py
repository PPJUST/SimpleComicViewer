# 显示图片的label，作为单页/双页预览控件的子控件

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

from constant import _MARGIN_PREVIEW, _ICON_NO_PIC
from module import function_comic, function_image, function_normal


class LabelImagePage(QLabel):
    """显示图片的label，单页/双页预览控件的子控件"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始化
        self._comic_path = None  # 漫画文件的路径
        self._filetype = None  # 漫画文件的文件类型
        self._image_path = None  # 需显示图像的文件路径
        self._image_size = None  # 需显示图像的文件宽高
        self._image_pixmap = None  # 需显示图像的pixmap对象
        self._max_widget_size = None  # label的最大大小（父控件的大小）

        if parent:
            self.parent_widget = parent
            self._update_max_label_size()
            self.setFixedSize(self._max_widget_size)

        self._load_default_image()

    def set_comic(self, comic_path: str, filetype: str):
        """设置漫画参数
        :param comic_path: 漫画文件的路径
        :param filetype: 漫画文件的类型，archive/folder"""
        function_normal.print_function_info()
        self._comic_path = comic_path
        self._filetype = filetype

    def set_image(self, image_path: str):
        """设置图片参数，并更新label大小"""
        function_normal.print_function_info()
        self._image_path = image_path
        self._image_pixmap = None

        self._get_image_size()
        self._change_label_size()

    def set_parent(self, parent):
        """设置父控件对象，更新label大小
        :param parent: 父控件"""
        function_normal.print_function_info()
        self.parent_widget = parent
        self._update_max_label_size()
        self._get_image_size()
        self._change_label_size()

    def show_image(self):
        """显示图像"""
        function_normal.print_function_info()
        if not self._image_pixmap:
            self._load_pixmap()
        scaled_pixmap = self._image_pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setPixmap(scaled_pixmap)

    def hide_label(self):
        """隐藏label控件"""
        function_normal.print_function_info()
        self._clear_image()
        self.setFixedSize(0, 0)

    def _load_pixmap(self):
        """读取图片，转为pixmap对象"""
        function_normal.print_function_info()
        if self._filetype == 'folder':
            self._image_pixmap = QPixmap(self._image_path)
        elif self._filetype == 'archive':
            img_bytes = function_comic.read_image_in_archive(self._comic_path, self._image_path)
            self._image_pixmap = QPixmap()
            self._image_pixmap.loadFromData(img_bytes)

    def _clear_image(self):
        """清除图片"""
        function_normal.print_function_info()
        self.clear()

    def _update_max_label_size(self):
        """更新label的最大尺寸"""
        function_normal.print_function_info()
        self._max_widget_size = QSize(
            self.parent_widget.width() - _MARGIN_PREVIEW, self.parent_widget.height() - _MARGIN_PREVIEW)

    def _get_image_size(self):
        """提取图片的宽高数据"""
        function_normal.print_function_info()
        if self._filetype == 'folder':
            self._image_size = function_image.get_image_size(self._image_path)
        elif self._filetype == 'archive':
            self._image_size = function_image.get_image_size_from_archive(self._comic_path, self._image_path)

    def _change_label_size(self):
        """修改label的大小，以匹配图像的大小"""
        function_normal.print_function_info()
        # 计算label和图像的宽高比
        label_rate = self._max_widget_size.width() / self._max_widget_size.height()
        image_rate = self._image_size[0] / self._image_size[1]
        # 以对应的宽或高为基准重设大小
        if label_rate > image_rate:  # 以label的高为基准
            label_size = self._calc_size_by_height()
        else:  # 以label的宽为基准
            label_size = self._calc_size_by_width()
        self.setFixedSize(label_size)

    def _calc_size_by_width(self):
        """以label的宽为基准计算新的尺寸"""
        function_normal.print_function_info()
        image_width, image_height = self._image_size
        new_height = int(image_height * self._max_widget_size.width() / image_width)
        new_size = QSize(self._max_widget_size.width(), new_height)
        return new_size

    def _calc_size_by_height(self):
        """以label的高为基准计算新的尺寸"""
        function_normal.print_function_info()
        image_width, image_height = self._image_size
        new_width = int(image_width * self._max_widget_size.height() / image_height)
        new_size = QSize(new_width, self._max_widget_size.height())
        return new_size

    def _load_default_image(self):
        """加载默认图片，用于初始化"""
        function_normal.print_function_info()
        self._image_path = _ICON_NO_PIC
        self._image_pixmap = QPixmap(self._image_path)
        self._image_size = function_image.get_image_size(self._image_path)
        self.show_image()
