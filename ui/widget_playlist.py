# 播放列表控件

# 备忘录 右键菜单 1.打开 2.打开路径 3.删除队列
# 备忘录 拖入后需要高亮拖入项
# 双击路径行打开对应路径


from typing import Union

from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget, QHeaderView

from constant import _ICON_CHECKED_GRAY, _ICON_ARCHIVE, _ICON_FOLDER, _ICON_CHECKED_GREEN
from module.class_comic_info import ComicInfo


class WidgetPlaylist(QTableWidget):
    """播放列表控件"""
    signal_double_click = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        # 设置标题行
        columns = ['已阅', '类型', '标题', '页数', '大小', '路径']
        self.setColumnCount(len(columns))
        self.setHorizontalHeaderLabels(columns)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # 设置ui
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(self.sizeHint())

        # 绑定双击信号
        self.itemDoubleClicked.connect(self._double_click_item)

        # 初始化
        self._last_active_row = 0  # 上次选中的行

    def add_item(self, comic: Union[str, ComicInfo]):
        """添加项目"""
        if type(comic) is str:
            comic = ComicInfo(comic)

        if self._is_item_exists(comic.path):
            return
        else:
            self._add_item(comic)

    def reset_xy(self, x: int, y: int):
        """重设坐标轴位置"""
        self.setGeometry(x, y, self.sizeHint().width(), self.sizeHint().height())

    def _add_item(self, comic_info: ComicInfo):
        """添加项目"""
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
        if comic_info.filetype == 'folder':
            item_filetype.setData(Qt.DecorationRole, QIcon(_ICON_FOLDER))
        elif comic_info.filetype == 'archive':
            item_filetype.setData(Qt.DecorationRole, QIcon(_ICON_ARCHIVE))
        item_filetype.setFlags(item_filetype.flags() & ~Qt.ItemIsEditable)
        self.setItem(index_row, 1, item_filetype)
        # 列3 标题
        item_filetitle = QTableWidgetItem(comic_info.filetitle)
        item_filetitle.setFlags(item_filetitle.flags() & ~Qt.ItemIsEditable)
        self.setItem(index_row, 2, item_filetitle)
        # 列4 页数
        item_page = QTableWidgetItem(str(comic_info.page_count))
        item_page.setFlags(item_page.flags() & ~Qt.ItemIsEditable)
        self.setItem(index_row, 3, item_page)
        # 列5 文件大小
        size_mb = round(comic_info.filesize / 1024 / 1024, 2)
        item_filesize = QTableWidgetItem(str(size_mb))
        item_filesize.setFlags(item_filesize.flags() & ~Qt.ItemIsEditable)
        self.setItem(index_row, 4, item_filesize)
        # 列6 文件路径
        item_filepath = QTableWidgetItem(comic_info.path)
        item_filepath.setFlags(item_filepath.flags() & ~Qt.ItemIsEditable)
        self.setItem(index_row, 5, item_filepath)

    def _double_click_item(self, item):
        """双击行项目"""
        if item:
            # 提取行号
            row = item.row()
            # 发送信号
            item_path = self.item(row, 5)
            filepath = item_path.text()
            self.signal_double_click.emit(filepath)
            # 修改图标
            self.item(row, 0).setData(Qt.DecorationRole, QIcon(_ICON_CHECKED_GREEN))
            # 修改文本颜色
            self.item(self._last_active_row, 0).setForeground(Qt.black)
            self.item(self._last_active_row, 1).setForeground(Qt.black)
            self.item(self._last_active_row, 2).setForeground(Qt.black)
            self.item(self._last_active_row, 3).setForeground(Qt.black)
            self.item(self._last_active_row, 4).setForeground(Qt.black)
            self.item(self._last_active_row, 5).setForeground(Qt.black)
            self.item(row, 0).setForeground(Qt.blue)
            self.item(row, 1).setForeground(Qt.blue)
            self.item(row, 2).setForeground(Qt.blue)
            self.item(row, 3).setForeground(Qt.blue)
            self.item(row, 4).setForeground(Qt.blue)
            self.item(row, 5).setForeground(Qt.blue)
            # 更新选中行变量
            self._last_active_row = row

    def _is_item_exists(self, path):
        """指定路径是否已经存在在视图中"""
        for row in range(self.rowCount()):
            item_path = self.item(row, 5)
            if item_path.text().upper() == path.upper():
                return True
