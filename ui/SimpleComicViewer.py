from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QAction, QResizeEvent, QKeySequence
from PySide6.QtWidgets import QMainWindow

from constant import _ICON_ARROW_LEFT, _ICON_ARROW_RIGHT
from module.function_config_get import GetSetting
from module.function_config_reset import ResetSetting
from thread.thread_listen_socket import ThreadListenSocket
from thread.thread_wait_time import ThreadWaitTime
from ui.dialog_option import DialogOption
from ui.label_hover_other_info import LabelHoverOtherInfo
from ui.preview_widget.widget_preview_control import WidgetPreviewControl
from ui.ui_src.ui_main import Ui_MainWindow
from ui.widget_below_control import WidgetBelowControl
from ui.widget_hidden_button import *
from ui.widget_playlist import WidgetPlaylist
from ui.widget_top_control import WidgetTopControl


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

        # 左边的切页按钮
        self.button_left = WidgetHiddenButton(self)
        self.button_left.set_icon(_ICON_ARROW_LEFT)
        self.button_left.clicked.connect(self.to_previous_page)
        self.button_left.rightClicked.connect(self.to_previous_comic)
        self.button_left.reset_xy(
            20, self.height() // 2 - self.button_left.height() // 2)

        # 右边的切页按钮
        self.button_right = WidgetHiddenButton(self)
        self.button_right.set_icon(_ICON_ARROW_RIGHT)
        self.button_right.clicked.connect(self.to_next_page)
        self.button_right.rightClicked.connect(self.to_next_comic)
        self.button_right.reset_xy(self.width() - self.button_right.width() - 20,
                                   self.height() // 2 - self.button_right.height() // 2)

        # 下方的控制条组件
        self.widget_below_control = WidgetBelowControl(self)
        self.widget_below_control.signal_previous_page.connect(
            self.to_previous_page)
        self.widget_below_control.signal_next_page.connect(self.to_next_page)
        self.widget_below_control.signal_previous_item.connect(
            self.to_previous_comic)
        self.widget_below_control.signal_next_item.connect(self.to_next_comic)
        self.widget_below_control.signal_open_playlist.connect(
            self.open_comic_list)
        self.widget_below_control.signal_open_option.connect(self.open_option)
        self.widget_below_control.signal_autoplay.connect(self.autoplay)
        self.widget_below_control.reset_xy(self.width() // 2 - self.widget_below_control.width() // 2,
                                           self.height() - self.widget_below_control.height() - 40)

        # 左上的控制条组件
        self.widget_top_control = WidgetTopControl(self)
        self.widget_top_control.signal_preview_mode_changed.connect(
            self.reload_preview_widget)
        self.widget_top_control.reset_xy(20, 20)

        # 预览控件
        self.widget_preview_control = WidgetPreviewControl(self)
        self.ui.horizontalLayout.addWidget(self.widget_preview_control)
        self.widget_preview_control.signal_stop_autoplay.connect(
            self.change_icon_stop_autoplay)
        self.widget_preview_control.signal_show_info.connect(self.show_info)

        # 右下角的悬浮播放列表
        self.widget_playlist = WidgetPlaylist(self)
        self.widget_playlist.raise_()
        self.widget_playlist.hide()

        # 设置左下角的其他信息悬浮label
        self.label_hover_other_info = LabelHoverOtherInfo(self)
        self.label_hover_other_info.raise_()  # 使该label显示在widget之上

        # 初始传参处理
        self._comic_list = args
        if args:
            self.accept_args(args)

        # 绑定快捷键
        self.bind_hotkey()
        # 监听本地端口
        self.listen_socket()

    def listen_socket(self):
        """监听本地端口"""
        self.thread_listen = ThreadListenSocket()
        self.thread_listen.signal_args.connect(self.accept_args)
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
        action_autoplay_1.triggered.connect(self.change_autoplay_speed_down)
        self.addAction(action_autoplay_1)
        action_autoplay_2 = QAction('X', self)
        action_autoplay_2.setShortcut(QKeySequence(Qt.Key_X))
        action_autoplay_2.triggered.connect(self.change_autoplay_speed_reset)
        self.addAction(action_autoplay_2)
        action_autoplay_3 = QAction('C', self)
        action_autoplay_3.setShortcut(QKeySequence(Qt.Key_C))
        action_autoplay_3.triggered.connect(self.change_autoplay_speed_up)
        self.addAction(action_autoplay_3)

        # 模式切换
        action_view_1 = QAction('ctrl+1', self)
        action_view_1.setShortcut(QKeySequence.fromString('ctrl+1'))
        action_view_1.triggered.connect(
            lambda: self.change_preview_mode('mode_1'))
        self.addAction(action_view_1)
        action_view_2 = QAction('ctrl+2', self)
        action_view_2.setShortcut(QKeySequence.fromString('ctrl+2'))
        action_view_2.triggered.connect(
            lambda: self.change_preview_mode('mode_2'))
        self.addAction(action_view_2)
        action_view_3 = QAction('ctrl+3', self)
        action_view_3.setShortcut(QKeySequence.fromString('ctrl+3'))
        action_view_3.triggered.connect(
            lambda: self.change_preview_mode('mode_3'))
        self.addAction(action_view_3)
        action_view_4 = QAction('ctrl+4', self)
        action_view_4.setShortcut(QKeySequence.fromString('ctrl+4'))
        action_view_4.triggered.connect(
            lambda: self.change_preview_mode('mode_4'))
        self.addAction(action_view_4)

    def accept_args(self, args):
        current_comic = args[0]
        self.widget_preview_control.set_comic(current_comic)  # 备忘录，先只做单个路径
        self.widget_playlist.add_item(current_comic)  # 备忘录，先只做单个路径

    def change_autoplay_speed_up(self):
        """自动播放加速"""
        self.widget_preview_control.autoplay_speed_up()

    def change_autoplay_speed_down(self):
        """自动播放加减速"""
        self.widget_preview_control.autoplay_speed_down()

    def change_autoplay_speed_reset(self):
        """重置自动播放速度"""
        self.widget_preview_control.reset_autoplay_speed()

    def to_previous_page(self):
        """切换上一页"""
        self.widget_preview_control.to_previous_page()

    def to_next_page(self):
        """切换下一页"""
        self.widget_preview_control.to_next_page()

    def open_comic_list(self):
        """打开漫画列表"""
        if self.widget_playlist.isHidden():
            self.widget_playlist.show()
        else:
            self.widget_playlist.hide()

    def to_previous_comic(self):
        """切换上一本漫画"""
        pass

    def to_next_comic(self):
        """切换下一本漫画"""
        pass

    def open_option(self):
        """打开设置页"""
        option_dialog = DialogOption()
        option_dialog.signal_option_changed.connect(self.option_changed)
        option_dialog.exec()

    def change_preview_mode(self, view_mode: str):
        """切换浏览模式"""
        ResetSetting.current_view_mode(view_mode)
        self.reload_preview_widget()
        self.widget_top_control.set_active_icon(view_mode)

    def reload_preview_widget(self):
        """切换浏览模式后重新加载预览控件"""
        view_mode = GetSetting.current_view_mode_eng()
        self.widget_preview_control.stop_thread_autoplay()
        self.widget_preview_control.set_preview_mode(view_mode)
        self.widget_preview_control.set_comic()
        self.widget_preview_control.reset_autoplay()

    def autoplay(self, is_start: bool):
        """自动播放状态"""
        if is_start:
            self.widget_preview_control.start_thread_autoplay()
        else:
            self.widget_preview_control.stop_thread_autoplay()

    def option_changed(self):
        """修改了设置选项，重新加载预览视图"""
        self.reload_preview_widget()

    def change_icon_stop_autoplay(self):
        self.widget_below_control.reset_autoplay_state()

    def update_preview_size(self):
        """更新预览控件的大小"""
        self.widget_preview_control.reset_preview_size()

    def show_info(self, text: str):
        self.label_hover_other_info.show_information(text)

    def resizeEvent(self, event: QResizeEvent) -> None:
        """重设悬浮组件的位置"""
        super().resizeEvent(event)
        # 左边的切页按钮，x轴离边框20，y轴居中
        self.button_left.reset_xy(
            20, self.height() // 2 - self.button_left.height() // 2)
        # 右边的切页按钮，x轴离边框20，y轴居中
        self.button_right.reset_xy(self.width() - self.button_right.width() - 20,
                                   self.height() // 2 - self.button_right.height() // 2)
        # 下方的控制条组件，x轴居中，y轴离边框40
        self.widget_below_control.reset_xy(self.width() // 2 - self.widget_below_control.width() // 2,
                                           self.height() - self.widget_below_control.height() - 40)
        # 左上的控制条组件，x轴离边框20，y轴离边框20
        self.widget_top_control.reset_xy(20, 20)
        # 右下角的播放列表组件 备忘录
        # self.widget_playlist.reset_xy(100, 100)
        # 左下角的信息组件
        self.label_hover_other_info.reset_xy(1, self.height() - 20)
        # 保存界面大小到配置文件
        ResetSetting.app_size(self.width(), self.height())

        # 启动延迟缩放计时器
        self.timer_resize.start(500)  # 延迟500毫秒

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
            self.accept_args(drop_paths)
