# 主窗口
# 备忘录 读取数据时加个dialog放进度条
import sys
from typing import Union

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMainWindow

from constant import _ICON_ARROW_LEFT, _ICON_ARROW_RIGHT, _MARGIN_MEDIUM, _MARGIN_SMALL, _PLAYLIST_HEIGHT
from module import function_comic
from module.function_config_get import GetSetting
from module.function_config_reset import ResetSetting
from thread.thread_listen_socket import ThreadListenSocket
from thread.thread_wait_time import ThreadWaitTime
from ui.dialog_option import DialogOption
from ui.label_hover_run_info import LabelHoverRunInfo
from ui.menu_main import MenuMain
from ui.preview_widget.widget_preview_control import WidgetPreviewControl
from ui.ui_src.ui_main import Ui_MainWindow
from ui.widget_change_preview import WidgetChangePreview
from ui.widget_comic_control import WidgetComicControl
from ui.widget_hidden_button import *
from ui.widget_playlist import WidgetPlaylist


class SimpleComicViewer(QMainWindow):
    def __init__(self, args, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)

        # 延迟定时器，用于延迟改变预览控件大小
        self.timer_resize = QTimer()
        self.timer_resize.setSingleShot(True)  # 设置单次触发
        self.timer_resize.timeout.connect(self.update_preview_size)

        # 延时线程，用于延迟隐藏按钮
        self.thread_wait_time = ThreadWaitTime()

        # 左下角的显示运行信息的悬浮label（单例模式，在此处设置唯一实例）
        self.label_hover_run_info = LabelHoverRunInfo(self)
        self.label_hover_run_info.raise_()  # 使该label显示在widget之上

        # 中部左边的切页按钮
        self.button_left = WidgetHiddenButton(self)
        self.button_left.set_icon(_ICON_ARROW_LEFT)
        self.button_left.clicked.connect(self.to_previous_page)
        self.button_left.rightClicked.connect(self.to_previous_comic)
        self.button_left.reset_xy(_MARGIN_MEDIUM, self.height() // 2 - self.button_left.height() // 2)

        # 中部右边的切页按钮
        self.button_right = WidgetHiddenButton(self)
        self.button_right.set_icon(_ICON_ARROW_RIGHT)
        self.button_right.clicked.connect(self.to_next_page)
        self.button_right.rightClicked.connect(self.to_next_comic)
        self.button_right.reset_xy(self.width() - self.button_right.width() - _MARGIN_MEDIUM,
                                   self.height() // 2 - self.button_right.height() // 2)

        # 中部下方的漫画控制条组件
        self.widget_below_control = WidgetComicControl(self)
        self.widget_below_control.signal_previous_page.connect(self.to_previous_page)
        self.widget_below_control.signal_next_page.connect(self.to_next_page)
        self.widget_below_control.signal_previous_item.connect(self.to_previous_comic)
        self.widget_below_control.signal_next_item.connect(self.to_next_comic)
        self.widget_below_control.signal_open_playlist.connect(self.open_playlist)
        self.widget_below_control.signal_open_option.connect(self.open_option)
        self.widget_below_control.signal_autoplay.connect(self.set_autoplay_state)
        self.widget_below_control.reset_xy(self.width() // 2 - self.widget_below_control.width() // 2,
                                           self.height() - self.widget_below_control.height() - _MARGIN_SMALL)

        # 左上角的切换预览视图的组件
        self.widget_change_preview = WidgetChangePreview(self)
        self.widget_change_preview.signal_preview_mode_changed.connect(self.reload_preview_widget)
        self.widget_change_preview.reset_xy(_MARGIN_MEDIUM, _MARGIN_SMALL)

        # 预览控件
        self.widget_preview_control = WidgetPreviewControl(self)
        self.ui.horizontalLayout.addWidget(self.widget_preview_control)
        self.widget_preview_control.signal_stop_autoplay.connect(self.reset_autoplay_state)

        # 紧贴主窗口右下角的悬浮播放列表
        self.widget_playlist = WidgetPlaylist()
        self.widget_playlist.signal_double_click.connect(self.accept_arg)
        self.widget_playlist.signal_clear_preview.connect(self.clear_display)
        self.widget_playlist.raise_()
        self.widget_playlist.hide()

        # 设置右键菜单
        self.menu = MenuMain()
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.open_context_menu)
        self.menu.signal_open_previous_comic.connect(lambda: self.to_previous_comic(dont_check_random=True))
        self.menu.signal_open_next_comic.connect(lambda: self.to_next_comic(dont_check_random=True))
        self.menu.signal_open_random_comic.connect(self.to_random_comic)
        self.menu.signal_choose_comic_folder.connect(self.accept_arg)
        self.menu.signal_choose_comic_archive.connect(self.accept_arg)
        self.menu.signal_open_file.connect(self.widget_playlist.open_active_item_file)
        self.menu.signal_remove_queue.connect(self.widget_playlist.remove_active_item_queue)
        self.menu.signal_delete_file.connect(lambda: self.widget_playlist.remove_active_item_queue(True))
        self.menu.signal_open_option.connect(self.open_option)
        # self.menu.signal_open_about.connect()
        self.menu.signal_quit.connect(sys.exit)

        # 初始传参处理
        self._comic_list = args
        if args:
            self.accept_arg(args)

        # 绑定快捷键
        self.bind_hotkey()
        # 监听本地端口
        self.listen_socket()

    def listen_socket(self):
        """监听本地端口，接收实时拖入的路径list"""
        self.thread_listen = ThreadListenSocket()
        self.thread_listen.signal_args.connect(self.accept_arg)
        self.thread_listen.start()

    def bind_hotkey(self):
        """绑定快捷键"""
        # 上一页
        action_pre_1 = QAction('PageUp', self)
        action_pre_1.setShortcut(QKeySequence(Qt.Key_PageUp))
        action_pre_1.triggered.connect(self.to_previous_page)
        self.addAction(action_pre_1)
        action_pre_2 = QAction('左箭头', self)
        action_pre_2.setShortcut(QKeySequence(Qt.Key_Left))
        action_pre_2.triggered.connect(self.to_previous_page)
        self.addAction(action_pre_2)
        action_pre_3 = QAction('上箭头', self)
        action_pre_3.setShortcut(QKeySequence(Qt.Key_Up))
        action_pre_3.triggered.connect(self.to_previous_page)
        self.addAction(action_pre_3)

        # 下一页
        action_next_1 = QAction('PageDown', self)
        action_next_1.setShortcut(QKeySequence(Qt.Key_PageDown))
        action_next_1.triggered.connect(self.to_next_page)
        self.addAction(action_next_1)
        action_next_2 = QAction('右箭头', self)
        action_next_2.setShortcut(QKeySequence(Qt.Key_Right))
        action_next_2.triggered.connect(self.to_next_page)
        self.addAction(action_next_2)
        action_next_3 = QAction('下箭头', self)
        action_next_3.setShortcut(QKeySequence(Qt.Key_Down))
        action_next_3.triggered.connect(self.to_next_page)
        self.addAction(action_next_3)

        # 自动翻页
        action_autoplay_1 = QAction('Z', self)
        action_autoplay_1.setShortcut(QKeySequence(Qt.Key_Z))
        action_autoplay_1.triggered.connect(self.autoplay_speed_down)
        self.addAction(action_autoplay_1)
        action_autoplay_2 = QAction('X', self)
        action_autoplay_2.setShortcut(QKeySequence(Qt.Key_X))
        action_autoplay_2.triggered.connect(self.reset_autoplay_speed)
        self.addAction(action_autoplay_2)
        action_autoplay_3 = QAction('C', self)
        action_autoplay_3.setShortcut(QKeySequence(Qt.Key_C))
        action_autoplay_3.triggered.connect(self.autoplay_speed_up)
        self.addAction(action_autoplay_3)

        # 模式切换
        action_view_1 = QAction('ctrl+1', self)
        action_view_1.setShortcut(QKeySequence.fromString('ctrl+1'))
        action_view_1.triggered.connect(lambda: self.change_preview_mode('mode_1'))
        self.addAction(action_view_1)
        action_view_2 = QAction('ctrl+2', self)
        action_view_2.setShortcut(QKeySequence.fromString('ctrl+2'))
        action_view_2.triggered.connect(lambda: self.change_preview_mode('mode_2'))
        self.addAction(action_view_2)
        action_view_3 = QAction('ctrl+3', self)
        action_view_3.setShortcut(QKeySequence.fromString('ctrl+3'))
        action_view_3.triggered.connect(lambda: self.change_preview_mode('mode_3'))
        self.addAction(action_view_3)
        action_view_4 = QAction('ctrl+4', self)
        action_view_4.setShortcut(QKeySequence.fromString('ctrl+4'))
        action_view_4.triggered.connect(lambda: self.change_preview_mode('mode_4'))
        self.addAction(action_view_4)

    def accept_arg(self, arg: Union[str, list]):
        """接收传参"""
        # 统一为list
        arg_list = []
        if type(arg) is str:
            arg_list.append(arg)
        else:
            arg_list = arg
        # 提取漫画文件夹/压缩包
        comics = function_comic.extract_comic(arg_list)
        if comics:
            # 添加到播放列表
            self.add_playlist(comics)
            # 显示第一个漫画
            self.show_comic(comics[0])
        else:
            self.clear_display()

    def show_comic(self, comic_path: str):
        """显示指定漫画"""
        self.label_hover_run_info.show_information(f'打开漫画 - {comic_path}')
        self.update_app_title(comic_path)
        self.widget_preview_control.set_comic(comic_path)
        self.widget_playlist.add_item(comic_path)
        self.widget_playlist.set_active_item(comic_path)

    def add_playlist(self, comic_paths: list):
        """添加到播放列表"""
        for path in comic_paths:
            self.widget_playlist.add_item(path)

    def clear_display(self):
        """清除显示的图像"""
        self.label_hover_run_info.show_information('清除显示')
        self.update_app_title()
        self.widget_preview_control.clear_preview()

    def autoplay_speed_up(self):
        """加速自动播放"""
        self.widget_preview_control.autoplay_speed_up()

    def autoplay_speed_down(self):
        """减速自动播放"""
        self.widget_preview_control.autoplay_speed_down()

    def reset_autoplay_speed(self):
        """重置自动播放速度"""
        self.widget_preview_control.reset_autoplay_speed()

    def to_previous_page(self):
        """切换上一页"""
        self.widget_preview_control.to_previous_page()

    def to_next_page(self):
        """切换下一页"""
        self.widget_preview_control.to_next_page()

    def open_playlist(self):
        """打开播放列表"""
        if self.widget_playlist.isHidden():
            self.widget_playlist.show()
        else:
            self.widget_playlist.hide()

    def to_previous_comic(self, dont_check_random=False):
        """切换上一本漫画"""
        if dont_check_random:
            self.widget_playlist.open_previous_item()
        else:
            if GetSetting.random_play():
                self.to_random_comic()
            else:
                self.widget_playlist.open_previous_item()

    def to_next_comic(self, dont_check_random=False):
        """切换下一本漫画"""
        if dont_check_random:
            self.widget_playlist.open_next_item()
        else:
            if GetSetting.random_play():
                self.to_random_comic()
            else:
                self.widget_playlist.open_next_item()

    def to_random_comic(self):
        """切换随机漫画"""
        self.widget_playlist.open_random_item()

    def open_option(self):
        """打开设置页"""
        option_dialog = DialogOption()
        option_dialog.signal_option_changed.connect(self.reload_preview_widget)
        option_dialog.exec()

    def change_preview_mode(self, view_mode: str):
        """切换浏览模式"""
        ResetSetting.current_view_mode(view_mode)
        self.reload_preview_widget()
        self.widget_change_preview.set_active_icon(view_mode)

    def reload_preview_widget(self):
        """重新加载预览控件"""
        self.widget_preview_control.reload_child_preview_widget()

    def set_autoplay_state(self, is_start: bool):
        """启用/终止自动播放"""
        if is_start:
            self.widget_preview_control.start_thread_autoplay()
        else:
            self.widget_preview_control.stop_thread_autoplay()

    def reset_autoplay_state(self):
        """重置自动播放线程状态"""
        self.widget_below_control.reset_autoplay_state()

    def update_preview_size(self):
        """更新预览控件的大小"""
        self.widget_preview_control.reset_preview_size()

    def move_playlist_xy(self):
        """移动外部播放列表，使其贴合主窗口右下角"""
        geometry = self.geometry()
        x_lr = geometry.x() + geometry.width()
        y_lr = geometry.y() + geometry.height()

        self.widget_playlist.reset_xy(x_lr + 5, y_lr - _PLAYLIST_HEIGHT)  # +5为大致的程序边框宽度

    def update_app_title(self, path=None):
        """更新程序标题，显示当前路径"""
        self.setWindowTitle(f'SimpleComicViewer - {path}')

    def open_context_menu(self, pos):
        self.menu.exec_(self.mapToGlobal(pos))

    def resizeEvent(self, event):
        """重写事件，更新各个悬浮组件的位置"""
        super().resizeEvent(event)
        # 左边的切页按钮，x轴离边框m，y轴居中
        self.button_left.reset_xy(_MARGIN_MEDIUM, self.height() // 2 - self.button_left.height() // 2)
        # 右边的切页按钮，x轴离边框m，y轴居中
        self.button_right.reset_xy(self.width() - self.button_right.width() - _MARGIN_MEDIUM,
                                   self.height() // 2 - self.button_right.height() // 2)
        # 下方的控制条组件，x轴居中，y轴离边框s
        self.widget_below_control.reset_xy(self.width() // 2 - self.widget_below_control.width() // 2,
                                           self.height() - self.widget_below_control.height() - _MARGIN_SMALL)
        # 左上的控制条组件，x轴离边框m，y轴离边框s
        self.widget_change_preview.reset_xy(_MARGIN_MEDIUM, _MARGIN_SMALL)
        # 左下角的信息组件
        self.label_hover_run_info.reset_xy(0, self.height() - self.label_hover_run_info.height())
        # 保存界面大小到配置文件
        ResetSetting.app_size(self.width(), self.height())

        # 启动延迟缩放计时器
        self.timer_resize.start(GetSetting.hide_wait_time_small() * 100)  # 延迟毫秒

    def moveEvent(self, event):
        """重写移动事件，用于保持外部播放列表窗口的相对位置"""
        super().moveEvent(event)
        self.move_playlist_xy()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        """重写拖入事件"""
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            drop_paths = [url.toLocalFile() for url in urls]
            self.accept_arg(drop_paths)

    def closeEvent(self, event):
        """重写关闭时间，同步关闭外部播放列表窗口"""
        if self.widget_playlist:
            self.widget_playlist.close()
