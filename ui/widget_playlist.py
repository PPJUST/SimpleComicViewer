# 播放列表控件

# 备忘录 右键菜单 1.打开 2.打开路径 3.删除队列
# 备忘录 当前项高亮


from typing import Union

from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget, QHeaderView

from constant import _ICON_CHECKED_GRAY, _ICON_ARCHIVE, _ICON_FOLDER
from module.class_comic_info import ComicInfo


class WidgetPlaylist(QTableWidget):
    """播放列表控件"""
    signal_double_click = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        # 设置ui
        columns = ['已阅', '类型', '标题', '页数', '大小']
        self.setColumnCount(len(columns))
        self.setHorizontalHeaderLabels(columns)

        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.resize(self.sizeHint())

    def add_item(self, comic: Union[str, ComicInfo]):
        """添加项目"""
        if type(comic) is str:
            comic = ComicInfo(comic)

        # 插入空行
        index_row = self.rowCount()
        self.insertRow(index_row)

        # 添加列数据
        # 列1 已阅图标
        item_checked = QTableWidgetItem()
        item_checked.setData(Qt.DecorationRole, QIcon(_ICON_CHECKED_GRAY))
        item_checked.setFlags(item_checked.flags() & ~Qt.ItemIsEditable)
        self.setItem(index_row, 0, item_checked)
        # 列2 文件类型图标
        item_filetype = QTableWidgetItem()
        if comic.filetype == 'folder':
            item_filetype.setData(Qt.DecorationRole, QIcon(_ICON_FOLDER))
        elif comic.filetype == 'archive':
            item_filetype.setData(Qt.DecorationRole, QIcon(_ICON_ARCHIVE))
        item_filetype.setFlags(item_filetype.flags() & ~Qt.ItemIsEditable)
        self.setItem(index_row, 1, item_filetype)
        # 列3 标题
        item_filetitle = QTableWidgetItem(comic.filetitle)
        item_filetitle.setFlags(item_filetitle.flags() & ~Qt.ItemIsEditable)
        self.setItem(index_row, 2, item_filetitle)
        # 列4 页数
        item_page = QTableWidgetItem(str(comic.page_count))
        item_page.setFlags(item_page.flags() & ~Qt.ItemIsEditable)
        self.setItem(index_row, 3, item_page)
        # 列5 文件大小
        size_mb = round(comic.filesize / 1024 / 1024, 2)
        item_filesize = QTableWidgetItem(str(size_mb))
        item_filesize.setFlags(item_filesize.flags() & ~Qt.ItemIsEditable)
        self.setItem(index_row, 4, item_filesize)
