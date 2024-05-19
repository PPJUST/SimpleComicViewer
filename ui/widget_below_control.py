# 主界面下方的控制栏组件

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QVBoxLayout, QWidget

from constant import _ICON_ARROW_LEFT, _ICON_ARROW_RIGHT, _ICON_LIST, _ICON_OPTION, _ICON_PLAY, _ICON_STOP
from thread.thread_wait_time import ThreadWaitTime
from ui.ui_src.ui_widget_below_control_child import Ui_Form


class WidgetBelowControl(QWidget):
    """主界面下方的控制栏组件（主程序使用的控件，用于中转子控件的信号和继承隐藏事件）"""
    signal_previous_page = Signal()
    signal_next_page = Signal()
    signal_open_playlist = Signal()
    signal_open_option = Signal()
    signal_previous_item = Signal()
    signal_next_item = Signal()
    signal_autoplay = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.widget = WidgetBelowControlChild()
        self.layout.addWidget(self.widget)
        self.installEventFilter(self.widget)
        self.widget.raise_()  # 使该label显示在widget之上

        # 固定size大小，用于setGeometry方法设置相对位置
        self._size = self.sizeHint()

        # 中转子控件信号
        self.widget.signal_previous_page.connect(
            self.signal_previous_page.emit)
        self.widget.signal_next_page.connect(self.signal_next_page.emit)
        self.widget.signal_previous_item.connect(
            self.signal_previous_item.emit)
        self.widget.signal_next_item.connect(self.signal_next_item.emit)
        self.widget.signal_open_playlist.connect(
            self.signal_open_playlist.emit)
        self.widget.signal_open_option.connect(self.signal_open_option.emit)
        self.widget.signal_autoplay.connect(self.signal_autoplay.emit)

    def reset_xy(self, x: int, y: int):
        """重设坐标轴位置"""
        self.setGeometry(x, y, self._size.width(), self._size.height())

    def reset_autoplay_state(self):
        """重置自动播放状态"""
        self.widget.reset_autoplay_state()


class WidgetBelowControlChild(QWidget):
    """主界面下方的控制栏组件（作为子控件，用于编写隐藏事件）"""
    signal_previous_page = Signal()  # 切换上一页
    signal_next_page = Signal()  # 切换下一页
    signal_open_playlist = Signal()  # 打开列表
    signal_open_option = Signal()  # 打开设置
    signal_previous_item = Signal()  # 切换上一本漫画
    signal_next_item = Signal()  # 切换下一本漫画
    signal_autoplay = Signal(bool)  # 自动播放/自动滚动开关

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # ui设置
        self.setMouseTracking(True)
        self._load_button_size()
        self._load_icon()

        # 初始化
        self._autoplay = False  # 自动播放的状态

        # 设置延迟隐藏的子线程
        self.thread_wait = ThreadWaitTime()
        self.thread_wait.signal_start.connect(self.show)
        self.thread_wait.signal_end.connect(self.hide)

        # 连接信号
        self.ui.toolButton_previous.clicked.connect(
            self.signal_previous_page.emit)
        self.ui.toolButton_next.clicked.connect(self.signal_next_page.emit)
        self.ui.toolButton_previous.rightClicked.connect(
            self.signal_previous_item.emit)
        self.ui.toolButton_next.rightClicked.connect(
            self.signal_next_item.emit)
        self.ui.toolButton_playlist.clicked.connect(
            self.signal_open_playlist.emit)
        self.ui.toolButton_option.clicked.connect(self.signal_open_option.emit)
        self.ui.toolButton_autoplay.clicked.connect(
            self._change_autoplay_state)

    def reset_autoplay_state(self):
        """重置自动播放开关状态"""
        self._autoplay = False
        self._update_autoplay_icon()

    def _change_autoplay_state(self):
        """切换自动播放状态"""
        self._autoplay = not self._autoplay
        self.signal_autoplay.emit(self._autoplay)
        self._update_autoplay_icon()

    def _load_button_size(self):
        """重置按钮的大小"""
        self.ui.toolButton_previous.setMinimumSize(24, 24)
        self.ui.toolButton_autoplay.setMinimumSize(24, 24)
        self.ui.toolButton_next.setMinimumSize(24, 24)
        self.ui.toolButton_option.setMinimumSize(24, 24)
        self.ui.toolButton_playlist.setMinimumSize(24, 24)

    def _load_icon(self):
        """设置图标"""
        self.ui.toolButton_previous.set_icon(_ICON_ARROW_LEFT)
        self.ui.toolButton_autoplay.set_icon(_ICON_PLAY)
        self.ui.toolButton_next.set_icon(_ICON_ARROW_RIGHT)
        self.ui.toolButton_option.set_icon(_ICON_OPTION)
        self.ui.toolButton_playlist.set_icon(_ICON_LIST)

    def _update_autoplay_icon(self):
        """更新自动播放图标"""
        if self._autoplay:
            self.ui.toolButton_autoplay.set_icon(_ICON_STOP)
        else:
            self.ui.toolButton_autoplay.set_icon(_ICON_PLAY)

    def eventFilter(self, obj, event):
        """隐藏事件"""
        if event.type() == event.Enter:
            if not self.thread_wait.isRunning():
                self.thread_wait.start()
            self.thread_wait.enable_loop()
        elif event.type() == event.Leave:
            self.thread_wait.reset_end_time()
            self.thread_wait.disable_loop()
            if not self.thread_wait.isRunning():
                self.thread_wait.start()
        return super().eventFilter(obj, event)
