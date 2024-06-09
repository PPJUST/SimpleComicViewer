# 预览控件，滚动显示漫画图像（右->左）

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QSizePolicy, QHBoxLayout, QWidget, QVBoxLayout

from module import function_normal
from module.class_comic_info import ComicInfo
from module.function_config_get import GetSetting
from ui.preview_widget.label_image_scroll import LabelImageScroll
from ui.preview_widget.scroll_area_preview import ScrollAreaPreview
from ui.preview_widget.scroll_area_smooth import ScrollAreaSmooth


class ScrollAreaPreviewReverse(ScrollAreaPreview):
    """预览控件，滚动显示漫画图像（右->左）"""
    signal_scrolled = Signal()

    def __init__(self, scroll_type='h', parent=None):
        """:param scroll_type: 滚动类型，横向h/纵向v"""
        super().__init__(scroll_type, parent)
        self.set_direction(True)

    def is_scroll_end(self):
        """是否已经滚动到底部"""
        scroll_bar_position = self.horizontalScrollBar().value()
        max_position = 0

        return scroll_bar_position == max_position


    def _create_empty_labels(self):
        """按照图像大小预先创建空的label"""
        self._clear_labels()
        for image_path in self._comic_info.page_list:
            label = LabelImageScroll(self._scroll_type, self.widget)
            label.set_comic(self._comic_info.path, self._comic_info.filetype)
            label.set_image(image_path)
            label._load_pixmap()  # 备忘录，暂时先读取全部图像，之后做在子线程中读取
            self.layout.insertWidget(0, label)
        # 更新索引列表
        self._update_index_list()



    def _update_index_list(self):
        """更新索引列表"""
        self._value_group_list.clear()
        for index in range(self.layout.count()):
            label = self.layout.itemAt(index).widget()
            if self._scroll_type == 'h':
                self._insert_index_list(label.width())
            elif self._scroll_type == 'v':
                self._insert_index_list(label.height())

        # 创建空label时是反序的，所以索引列表也需要反序
        self._value_group_list.reverse()
        print(' self._value_group_list', self._value_group_list)



