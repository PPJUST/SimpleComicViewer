from PySide6.QtWidgets import QScrollArea

from common.image_info import ImageInfo
from common.mode_image_size import ModeImageSize
from components.label_image import LabelImage


class LabelImageScroll(LabelImage):
    """显示图片的控件，专用于卷轴视图"""

    def __init__(self, image_info: ImageInfo = None, parent=None):
        super().__init__(image_info, parent)

    def _check_size_scrollbar(self, width, height, size_mode: ModeImageSize):
        """在指定边宽超过label父控件边宽，而显示滑动条时，考虑滑动条的宽度
        在卷轴视图中，固定减去滑动条宽度"""
        parent: QScrollArea = self.parentWidget().parentWidget().parentWidget()
        scrollbar_width = parent.verticalScrollBar().width()

        if size_mode is ModeImageSize.FitWidth:
            # 适应宽度模式
            new_width = width - scrollbar_width
            new_height = new_width * height / width
            width, height = new_width, new_height
        elif size_mode is ModeImageSize.FitHeight:
            # 适应高度模式
            new_height = height - scrollbar_width
            new_width = new_height * width / height
            width, height = new_width, new_height

        return width, height
