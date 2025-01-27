import lzytools._qt_pyside6
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QApplication

from common.comic_info import ComicInfo
from common.image_info import ImageInfo
from components.hover_image_info.icon_base64 import _IMAGE, _ARCHIVE
from components.hover_image_info.ui_image_info import Ui_Form


class HoverImageInfo(QWidget):
    """显示图片信息"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 添加长文本控件（过长时隐藏超限部分为...）
        self.label_comic_filepath = lzytools._qt_pyside6.LabelHiddenOverLengthText()
        self.ui.verticalLayout_comic_filepath.addWidget(self.label_comic_filepath)
        self.label_comic_filename = lzytools._qt_pyside6.LabelHiddenOverLengthText()
        self.ui.verticalLayout_comic_filename.addWidget(self.label_comic_filename)
        self.label_image_filename = lzytools._qt_pyside6.LabelHiddenOverLengthText()
        self.ui.verticalLayout_image_filename.addWidget(self.label_image_filename)

        self._set_icon()

        # 设置参数
        self.comic_info: ComicInfo = None  # 漫画信息类
        self.image_info: ImageInfo = None  # 图片信息类

    def set_comic(self, comic_info: ComicInfo):
        self.comic_info = comic_info
        self.label_comic_filepath.setText(comic_info.path)
        self.label_comic_filepath.setToolTip(comic_info.path)
        self.label_comic_filename.setText(comic_info.filename)
        self.label_comic_filename.setToolTip(comic_info.filename)
        self.ui.label_comic_filesize.setText(f'{round(comic_info.filesize / 1024 / 1024, 2)} MB')
        self.ui.label_comic_page_count.setText(f'{comic_info.page_count} 页')

    def set_image(self, image_info: ImageInfo):
        self.image_info = image_info
        self.label_image_filename.setText(image_info.filename)
        self.ui.label_image_filesize.setText(f'{round(image_info.filesize / 1024 / 1024, 2)} MB')
        self.ui.label_image_size.setText(f'{image_info.size[0]} x {image_info.size[1]} px')
        self.ui.label_page_index.setText(f'{image_info.page_index}/{self.comic_info.page_count}')

    def _set_icon(self):
        self.ui.label_image_icon.setPixmap(lzytools._qt_pyside6.base64_to_pixmap(_IMAGE).scaled(QSize(16, 16)))
        self.ui.label_comic_icon.setPixmap(lzytools._qt_pyside6.base64_to_pixmap(_ARCHIVE).scaled(QSize(16, 16)))

    def enterEvent(self, event):
        super().enterEvent(event)
        self.label_comic_filepath.setVisible(True)
        self.label_comic_filename.setVisible(True)
        self.label_image_filename.setVisible(True)
        self.ui.label_comic_icon.setVisible(True)
        self.ui.label_image_icon.setVisible(True)
        self.ui.label_comic_filesize.setVisible(True)
        self.ui.label_comic_page_count.setVisible(True)
        self.ui.label_image_filesize.setVisible(True)
        self.ui.label_image_size.setVisible(True)
        self.ui.label_page_index.setVisible(True)
        self.ui.label_2.setVisible(True)
        self.ui.label_3.setVisible(True)
        self.ui.label_4.setVisible(True)
        self.ui.label_5.setVisible(True)
        self.ui.label_7.setVisible(True)
        self.ui.label_8.setVisible(True)
        self.ui.label_9.setVisible(True)
        self.ui.label_10.setVisible(True)
        self.ui.label_11.setVisible(True)
        self.ui.label_12.setVisible(True)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.label_comic_filepath.setVisible(False)
        self.label_comic_filename.setVisible(False)
        self.label_image_filename.setVisible(False)
        self.ui.label_comic_icon.setVisible(False)
        self.ui.label_image_icon.setVisible(False)
        self.ui.label_comic_filesize.setVisible(False)
        self.ui.label_comic_page_count.setVisible(False)
        self.ui.label_image_filesize.setVisible(False)
        self.ui.label_image_size.setVisible(False)
        self.ui.label_page_index.setVisible(False)
        self.ui.label_2.setVisible(False)
        self.ui.label_3.setVisible(False)
        self.ui.label_4.setVisible(False)
        self.ui.label_5.setVisible(False)
        self.ui.label_7.setVisible(False)
        self.ui.label_8.setVisible(False)
        self.ui.label_9.setVisible(False)
        self.ui.label_10.setVisible(False)
        self.ui.label_11.setVisible(False)
        self.ui.label_12.setVisible(False)


if __name__ == '__main__':
    app = QApplication()
    ui = HoverImageInfo()
    ui.show()
    app.exec()
