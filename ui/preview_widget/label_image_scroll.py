# 显示图片的label，作为滚动预览控件的子控件

from module import function_normal
from ui.preview_widget.label_image_page import LabelImagePage


class LabelImage(LabelImagePage):
    """显示图片的label，滚动预览控件的子控件"""

    def __init__(self, scroll_type: str, parent=None):
        """:param scroll_type: 预览控件的滚动类型，横向h/纵向v"""
        super().__init__(parent)

        self._scroll_type = scroll_type  # 预览控件的滚动类型，v/h
        self._is_show_image = False  # 是否已经显示图像

    def show_image(self):
        """显示图片"""
        function_normal.print_function_info()
        if self._is_show_image:
            return
        super().show_image()
        self._is_show_image = True

    def hide_image(self):
        """隐藏图片"""
        self._clear_image()

    def refresh_image(self):
        """刷新图片（更新大小）"""
        function_normal.print_function_info()
        self._clear_image()
        self.show_image()

    def _change_label_size(self):
        """修改label的大小，以匹配视图模式"""
        if self._scroll_type == 'v':  # 以label的宽为基准
            label_size = self._calc_size_by_width()
        elif self._scroll_type == 'h':  # 以label的高为基准
            label_size = self._calc_size_by_height()
        self.setFixedSize(label_size)

    def _clear_image(self):
        """清除图片"""
        super()._clear_image()
        self._is_show_image = False
