# 播放列表控件
import os
import random
from typing import Union

import send2trash
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QMenu, QTableWidgetItem, QTableWidget, QHeaderView

from constant import (_ICON_CHECKED_GRAY, _ICON_ARCHIVE, _ICON_FOLDER, _ICON_CHECKED_GREEN, _ICON_WARNING,
                      _PLAYLIST_WIDTH, _PLAYLIST_HEIGHT, _PLAYLIST_COLUMN_MAX_HEIGHT)
from module.class_comic_info import ComicInfo
from ui.label_hover_run_info import LabelHoverRunInfo


class WidgetPlaylist(QTableWidget):
    """播放列表控件"""
    signal_double_click = Signal(str)
    signal_clear_preview = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        # 设置标题行
        columns = ['已阅', '类型', '标题', '页数', '大小', '路径']
        self.setColumnCount(len(columns))
        self.setHorizontalHeaderLabels(columns)

        # 设置ui
        self.setFixedSize(_PLAYLIST_WIDTH, _PLAYLIST_HEIGHT)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setVerticalScrollMode(QTableWidget.ScrollPerPixel)
        self.setHorizontalScrollMode(QTableWidget.ScrollPerPixel)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        # 设置列宽
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.horizontalHeader().setMaximumSectionSize(_PLAYLIST_COLUMN_MAX_HEIGHT)

        # 绑定双击信号
        self.itemDoubleClicked.connect(self._double_click_item)

        # 设置右键菜单
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self._show_context_menu)

        # 加载信息显示控件（单例模式，实例在主程序中）
        self.label_hover_run_info = LabelHoverRunInfo()

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

    def set_active_item(self, comic_path):
        """高亮当前项目"""
        for row in range(self.rowCount()):
            item_path = self.item(row, 5)
            path = item_path.text()
            if path == comic_path:
                self.item(row, 0).setData(Qt.DecorationRole, QIcon(_ICON_CHECKED_GREEN))
                self._highlight_row(row)
                break

    def open_next_item(self):
        """打开下一行项目"""
        target_row = self._last_active_row + 1
        if target_row < self.rowCount():
            self._active_row_item(target_row)

    def open_previous_item(self):
        """打开上一行项目"""
        target_row = self._last_active_row - 1
        if target_row >= 0:
            self._active_row_item(target_row)

    def open_random_item(self):
        """打开随机项目"""
        if self.rowCount() > 1:
            while True:
                random_row = random.randint(0, self.rowCount() - 1)
                if random_row != self._last_active_row:
                    self._active_row_item(random_row)
                    break

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
        item_filetitle.setToolTip(comic_info.filetitle)
        self.setItem(index_row, 2, item_filetitle)
        # 列4 页数
        item_page = QTableWidgetItem(str(comic_info.page_count))
        item_page.setFlags(item_page.flags() & ~Qt.ItemIsEditable)
        self.setItem(index_row, 3, item_page)
        # 列5 文件大小
        size_mb = round(comic_info.filesize / 1024 / 1024, 2)
        item_filesize = QTableWidgetItem(f'{size_mb}MB')
        item_filesize.setFlags(item_filesize.flags() & ~Qt.ItemIsEditable)
        self.setItem(index_row, 4, item_filesize)
        # 列6 文件路径
        item_filepath = QTableWidgetItem(comic_info.path)
        item_filepath.setFlags(item_filepath.flags() & ~Qt.ItemIsEditable)
        item_filepath.setToolTip(comic_info.path)
        self.setItem(index_row, 5, item_filepath)

    def _double_click_item(self, item):
        """双击行项目"""
        if item:
            # 提取行号
            row = item.row()
            filepath = self._get_item_path(item)
            # 检测行项目对应的路径是否存在
            if not self._is_path_exists(filepath):
                self._lowlight_row(row)
            else:
                if row != self._last_active_row:
                    # 发送信号
                    self.signal_double_click.emit(filepath)
                    # 高亮行
                    self._highlight_row(row)
                # 提取列号
                column = item.column()
                if column == 5:  # 双击的是路径单元格，则打开对应路径文件
                    self._open_file(filepath)

    def _active_row_item(self, row: int):
        """将指定行设为活动项"""
        filepath = self._get_row_path(row)
        # 检测行项目对应的路径是否存在
        if not self._is_path_exists(filepath):
            self._lowlight_row(row)
        # 发送信号
        self.signal_double_click.emit(filepath)
        # 高亮行
        self._highlight_row(row)

    def _highlight_row(self, row: int):
        """高亮行"""
        if row == self._last_active_row:
            return
        # 修改图标
        self.item(row, 0).setData(Qt.DecorationRole, QIcon(_ICON_CHECKED_GREEN))
        # 修改文本颜色
        for col in range(self.columnCount()):
            self.item(row, col).setForeground(Qt.blue)
            self.item(self._last_active_row, col).setForeground(Qt.black)
        # 更新选中行变量
        self._last_active_row = row

    def _lowlight_row(self, row: int):
        """低亮行"""
        # 修改图标
        self.item(row, 0).setData(Qt.DecorationRole, QIcon(_ICON_WARNING))
        self.item(row, 1).setData(Qt.DecorationRole, QIcon(_ICON_WARNING))
        # 修改文本颜色
        for col in range(self.columnCount()):
            self.item(row, col).setForeground(Qt.gray)
        # 设置禁止选中该行
        for col in range(self.columnCount()):
            self.item(row, col).setFlags(self.item(row, col).flags() & ~Qt.ItemIsSelectable)

    def _remove_queue_item(self, item: QTableWidgetItem, is_delete_file=False):
        """移除队列项目"""
        row = item.row()
        filepath = self._get_row_path(row)
        self.removeRow(row)
        self.label_hover_run_info.show_information(f'移除队列项 - {filepath}')

        # 如果当前预览的行就是被移除的行，则切换预览
        if self._last_active_row == row:
            if self.rowCount() == 0:  # 删除后队列为空，则清除主窗口预览
                self.signal_clear_preview.emit()
            elif self.rowCount() > row:  # 下方行数够，则切换下一项
                self._active_row_item(row)
            else:  # 否则切换上一项
                self._active_row_item(row - 1)

        if is_delete_file:
            self._delete_file(filepath)

    def _show_context_menu(self, pos):
        """右键菜单"""
        item = self.itemAt(pos)
        if item is not None:  # 判断是否右键点击在单元格上
            menu = QMenu()
            menu.adjustSize()

            action_preview = QAction('浏览', menu)
            action_preview.triggered.connect(lambda: self._double_click_item(item))
            menu.addAction(action_preview)

            action_open_file = QAction('打开本地文件', menu)
            action_open_file.triggered.connect(lambda: self._open_file(self._get_item_path(item)))
            menu.addAction(action_open_file)

            action_remove_queue = QAction('删除队列', menu)
            action_remove_queue.triggered.connect(lambda: self._remove_queue_item(item))
            menu.addAction(action_remove_queue)

            action_delete_file = QAction('删除本地文件', menu)
            action_delete_file.triggered.connect(lambda: self._remove_queue_item(item, is_delete_file=True))
            menu.addAction(action_delete_file)

            menu.exec_(self.mapToGlobal(pos))

    @staticmethod
    def _open_file(path):
        """打开指定路径文件"""
        os.startfile(path)

    def _delete_file(self, path):
        """删除本地文件"""
        send2trash.send2trash(path)
        self.label_hover_run_info.show_information(f'删除本地文件 - {path}')

    def _get_item_path(self, item: QTableWidgetItem):
        """提取item对应行项目的文件路径"""
        row = item.row()
        item_path = self.item(row, 5)
        filepath = item_path.text()

        return filepath

    def _get_row_path(self, row: int):
        """提取指定行项目的文件路径"""
        item_path = self.item(row, 5)
        filepath = item_path.text()

        return filepath

    def _is_item_exists(self, path):
        """指定路径是否已经存在在视图中"""
        for row in range(self.rowCount()):
            item_path = self.item(row, 5)
            if item_path.text().upper() == path.upper():
                return True

    @staticmethod
    def _is_path_exists(path):
        """对应的路径文件是否存在"""
        if os.path.exists(path):
            return True
        else:
            return False
