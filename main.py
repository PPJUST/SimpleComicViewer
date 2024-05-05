import sys

from PySide6.QtGui import *

from module.function_config_get import GetSetting
from constant import _ICON_ARROW_LEFT, _ICON_ARROW_RIGHT, _ICON_MAIN
from module import function_config_normal
from ui.dialog_option import DialogOption
from ui.ui_src.ui_main import Ui_MainWindow
from ui.widget_below_control import WidgetBelowControl
from ui.widget_hidden_button import *
from ui.widget_preview_control import WidgetPreviewControl
from ui.widget_top_control import WidgetTopControl


class SCV(QMainWindow):
    def __init__(self, arg, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)

        # 初始传参处理
        self._comic_list = arg
        if self._comic_list:
            self._current_comic = self._comic_list[0]  # 备忘录，先只做单个路径
        else:
            self._current_comic = None

        # 延迟定时器，用于延迟改变预览控件大小
        self.timer_resize = QTimer()
        self.timer_resize.setSingleShot(True)  # 设置单次触发
        self.timer_resize.timeout.connect(self.update_preview_size)

        # 延时线程
        self.thread_wait_time = ThreadWaitTime()

        # 左边的切页按钮
        self.button_left = WidgetHiddenButton(_ICON_ARROW_LEFT, self)
        self.button_left.clicked.connect(self.to_previous_page)
        self.button_left.rightClicked.connect(self.to_previous_comic)
        self.button_left.set_wait_thread(self.thread_wait_time)
        self.button_left.reset_xy(20, self.height() // 2 - self.button_left.height() // 2)

        # 右边的切页按钮
        self.button_right = WidgetHiddenButton(_ICON_ARROW_RIGHT, self)
        self.button_right.clicked.connect(self.to_next_page)
        self.button_right.rightClicked.connect(self.to_next_comic)
        self.button_right.set_wait_thread(self.thread_wait_time)
        self.button_right.reset_xy(self.width() - self.button_right.width() - 20,
                                   self.height() // 2 - self.button_right.height() // 2)

        # 下方的控制条组件
        self.widget_below_control = WidgetBelowControl(self)
        self.widget_below_control.signal_previous_page.connect(self.to_previous_page)
        self.widget_below_control.signal_next_page.connect(self.to_next_page)
        self.widget_below_control.signal_previous_item.connect(self.to_previous_comic)
        self.widget_below_control.signal_next_item.connect(self.to_next_comic)
        self.widget_below_control.signal_open_list.connect(self.open_comic_list)
        self.widget_below_control.signal_open_option.connect(self.open_option)
        self.widget_below_control.signal_auto_play.connect(self.auto_play)
        self.widget_below_control.set_wait_thread(self.thread_wait_time)
        self.widget_below_control.reset_xy(self.width() // 2 - self.widget_below_control.width() // 2,
                                           self.height() - self.widget_below_control.height() - 40)

        # 左上的控制条组件
        self.widget_top_control = WidgetTopControl(self)
        self.widget_top_control.signal_preview_mode_changed.connect(self.change_preview_mode)
        self.widget_top_control.set_wait_thread(self.thread_wait_time)
        self.widget_top_control.reset_xy(20, 20)

        # 预览控件
        self.preview_control_widget = WidgetPreviewControl(self)
        self.ui.horizontalLayout.addWidget(self.preview_control_widget)
        self.preview_control_widget.signal_stop_auto_play.connect(self.change_icon_stop_auto_play)

        # 如果启动时带参数，则直接预览
        if self._current_comic:
            self.preview_control_widget.load_comic(self._current_comic)  # 备忘录，先只做单个路径

    def to_previous_page(self):
        """切换上一页"""
        self.preview_control_widget.to_previous_page()

    def to_next_page(self):
        """切换下一页"""
        self.preview_control_widget.to_next_page()

    def open_comic_list(self):
        """打开漫画列表"""
        pass

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

    def change_preview_mode(self):
        """切换浏览模式"""
        view_mode = GetSetting.current_view_mode_eng()
        self.preview_control_widget.stop_auto_play()
        self.preview_control_widget.load_child_preview_widget(view_mode)
        self.preview_control_widget.load_comic()
        self.preview_control_widget.set_auto_play_type(view_mode)

    def auto_play(self, is_start: bool):
        """自动播放状态"""
        if is_start:
            self.preview_control_widget.start_auto_play()
        else:
            self.preview_control_widget.stop_auto_play()

    def option_changed(self):
        """修改了设置选项，重新加载预览视图"""
        self.change_preview_mode()

    def change_icon_stop_auto_play(self):
        self.widget_below_control.reset_auto_play_state()

    def update_preview_size(self):
        """更新预览控件的大小"""
        self.preview_control_widget.reset_preview_size()

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        # 设置悬浮组件的位置
        # 左边的切页按钮，x轴离边框20，y轴居中
        self.button_left.reset_xy(20, self.height() // 2 - self.button_left.height() // 2)
        # 右边的切页按钮，x轴离边框20，y轴居中
        self.button_right.reset_xy(self.width() - self.button_right.width() - 20,
                                   self.height() // 2 - self.button_right.height() // 2)
        # 下方的控制条组件，x轴居中，y轴离边框40
        self.widget_below_control.reset_xy(self.width() // 2 - self.widget_below_control.width() // 2,
                                           self.height() - self.widget_below_control.height() - 40)
        # 左上的控制条组件，x轴离边框20，y轴离边框20
        self.widget_top_control.reset_xy(20, 20)

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
            self._current_comic = drop_paths[0]  # 备忘录，先只做单个路径
            self.preview_control_widget.load_comic(self._current_comic)


def main(arg):
    function_config.create_default_config()

    app = QApplication()
    app.setStyle('Fusion')
    # 设置白色背景色
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(255, 255, 255))
    app.setPalette(palette)
    show_ui = SCV(arg)
    show_ui.show()
    show_ui.setWindowIcon(QIcon(_ICON_MAIN))

    app.exec()


if __name__ == "__main__":
    try:
        args = sys.argv[1:]  # 备忘录 先只做单个路径
    except:
        args = []
    main(args)
