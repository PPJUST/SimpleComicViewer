# 预览控件，滚动显示漫画图像（右->左）

from module.class_comic_info import ComicInfo
from ui.preview_widget.label_image_scroll import LabelImageScroll
from ui.preview_widget.scroll_area_preview import ScrollAreaPreview


class ScrollAreaPreviewReverse(ScrollAreaPreview):
    """预览控件，滚动显示漫画图像（右->左）"""

    def __init__(self, scroll_type='h', parent=None):
        """:param scroll_type: 滚动类型，横向h/纵向v"""
        super().__init__(scroll_type, parent)
        self.set_direction(True)

    def set_comic(self, comic_info: ComicInfo):
        """设置漫画数据"""
        super().set_comic(comic_info)
        self._move_slider_absolute(99999999)  # 滚动到最右侧

    def is_scroll_end(self):
        """是否已经滚动到底部"""
        scroll_bar_position = self.horizontalScrollBar().value()
        max_position = 0

        return scroll_bar_position == max_position

    def _create_empty_labels(self):
        """按照图像大小预先创建空的label"""
        self._clear_labels()
        for index, image_path in enumerate(self._comic_info.page_list):
            label = LabelImageScroll(self._scroll_type, self.widget)
            label.set_comic(self._comic_info.path, self._comic_info.filetype)
            label.set_image(image_path)
            label.set_index(index)
            label._load_pixmap()  # 备忘录，暂时先读取全部图像，之后做在子线程中读取
            self.layout.insertWidget(0, label)
        # 更新索引列表
        self._update_index_list()

    def _update_index_list(self):
        """更新索引列表"""
        self._value_group_list.clear()
        for index in range(self.layout.count()):
            label = self.layout.itemAt(index).widget()
            self._insert_index_list(label.width())

        # 创建空label时是反序的，所以索引列表也需要反序
        self._value_group_list.reverse()
